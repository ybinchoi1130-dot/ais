#!/usr/bin/env python
# coding: utf-8

# # Multimodal RAG Tutorial (Google Gemini)
#%%

"""
기존 RAG와 멀티모달 RAG는 무엇이 다른가?
1. 기존 텍스트 RAG: PDF 속 텍스트만 추출해 쪼개고(Chunking) 임베딩
    하지만 차트, 안전 수칙 그림, 장비 조작 인포그래픽은 텍스트 파서가 무시하거나 
    깨진 글자로 읽어버려 답변할 수 없다.

2. 멀티모달 RAG: 문서에 포함된 도표와 시각 자료(Image)를 함께 보존하고 검색하여, 
    시각 모델(VLM)이 직접 그림을 보고 답변을 생성하도록 만듦

전체 아키텍처 흐름
이 코드가 채택한 방식은 LangChain의 Multi-Vector Retriever 패턴

flowchart TD
    A[PDF 문서] -->|파싱 & 이미지 추출| B[텍스트 / 표 / 이미지 분리]
    
    subgraph 요약 생성
        B -->|Gemini 텍스트 요약| C1[텍스트/표 요약문]
        B -->|Gemini Vision 요약| C2[이미지 요약문]
    end
    
    subgraph Multi-Vector Storage
        C1 -->|Gemini Embedding| D1[(VectorStore: 요약 임베딩)]
        C2 -->|Gemini Embedding| D1
        B -->|doc_id 매핑 보관| D2[(DocStore: 원본 텍스트 & Base64 이미지)]
    end
    
    subgraph 검색 & 질의 파이프라인
        Q[사용자 질문: '소화전 사용 방법'] -->|검색| D1
        D1 -->|doc_id 조회| D2
        D2 -->|검색된 원본 반환| E[분류: 텍스트 vs Base64 이미지]
        E -->|멀티모달 프롬프트 구성| F[ChatGoogleGenerativeAI]
        F --> G[최종 멀티모달 답변 생성]
    end    
"""

#%%
import base64
import getpass
import io
import os
import re
import sys
import uuid
from PIL import Image

# Windows 콘솔 한글 인코딩 설정
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# API 키 설정
if "GOOGLE_API_KEY" not in os.environ:
    if "GEMINI_API_KEY" in os.environ:
        os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]
    else:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")

# model_name = "gemini-2.5-flash"
model_name = "gemini-3.1-flash-lite"

# NLTK 토크나이저 설정
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', quiet=True)
os.makedirs('./nltk_data/tokenizers/punkt/PY3_tab', exist_ok=True)

# 텍스트 스플리터 및 PDF 처리 로직
try:
    from langchain_text_splitters import CharacterTextSplitter
except ImportError:
    from langchain.text_splitter import CharacterTextSplitter


def extract_pdf_elements(path, fname):
    pdf_path = os.path.join(path, fname)
    if not os.path.exists(pdf_path) and os.path.exists(fname):
        pdf_path = fname

    figures_dir = "./figures"
    os.makedirs(figures_dir, exist_ok=True)

    # 1. unstructured의 partition_pdf 시도
    try:
        from unstructured.partition.pdf import partition_pdf
        return partition_pdf(
            filename=pdf_path,
            extract_images_in_pdf=True,
            infer_table_structure=True,
            chunking_strategy="by_title",
            max_characters=4000,
            new_after_n_chars=3800,
            combine_text_under_n_chars=2000,
            image_output_dir_path=figures_dir,
        )
    except Exception as e:
        print(f"[Info] partition_pdf 사용 불가 ({e}). PyMuPDF로 대체하여 페이지 및 이미지를 추출합니다.")
        import pymupdf
        doc = pymupdf.open(pdf_path)
        raw_elements = []
        for i, page in enumerate(doc):
            text = page.get_text().strip()
            if text:
                raw_elements.append(text)

            # 각 페이지를 이미지로 렌더링하여 figures 디렉터리에 저장
            page_img_path = os.path.join(figures_dir, f"figure-page-{i+1}.jpg")
            if not os.path.exists(page_img_path):
                pix = page.get_pixmap(dpi=150)
                pix.save(page_img_path)
        return raw_elements


def categorize_elements(raw_pdf_elements):
    tables = []
    texts = []
    for element in raw_pdf_elements:
        if "unstructured.documents.elements.Table" in str(type(element)):
            tables.append(str(element))
        elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
            texts.append(str(element))
        elif isinstance(element, str) and element.strip():
            texts.append(element)
    return texts, tables


# 파일 경로 설정 (./pdf/ 또는 ./)
fpath = "./pdf/" if os.path.exists("./pdf/fire.pdf") else "./"
fname = "fire.pdf"

raw_pdf_elements = extract_pdf_elements(fpath, fname)
texts, tables = categorize_elements(raw_pdf_elements)

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=4000, chunk_overlap=0
)
joined_texts = " ".join(texts)
texts_4k_token = text_splitter.split_text(joined_texts) if joined_texts else []

figures_path = "./figures/"
os.makedirs(figures_path, exist_ok=True)


# 텍스트 및 테이블 요약 생성
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


def generate_text_summaries(texts, tables, summarize_texts=False):
    if not texts and not tables:
        return [], []

    prompt_text = """당신은 테이블과 텍스트를 요약하여 검색에 사용할 수 있도록 돕는 어시스턴트입니다. \
이 요약은 임베딩되어 원문 텍스트 또는 테이블 요소를 검색하는 데 사용됩니다. \
테이블 또는 텍스트를 간결하게 요약하고 검색에 최적화된 내용을 작성하세요. 테이블 또는 텍스트: {element} \
한국어로 작성하세요."""
    prompt = ChatPromptTemplate.from_template(prompt_text)

    model = ChatGoogleGenerativeAI(temperature=0, model=model_name, max_tokens=4096)
    summarize_chain = {"element": lambda x: x} | prompt | model | StrOutputParser()

    text_summaries = []
    table_summaries = []

    if texts and summarize_texts:
        text_summaries = summarize_chain.batch(texts, {"max_concurrency": 5})
    elif texts:
        text_summaries = texts

    if tables:
        table_summaries = summarize_chain.batch(tables, {"max_concurrency": 5})

    return text_summaries, table_summaries


text_summaries, table_summaries = generate_text_summaries(
    texts_4k_token, tables, summarize_texts=True
)


# 이미지 인코딩 및 요약 생성
from langchain_core.messages import HumanMessage


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def image_summarize(img_base64, prompt):
    chat = ChatGoogleGenerativeAI(model=model_name, max_tokens=4096)

    msg = chat.invoke(
        [
            HumanMessage(
                content=[
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"},
                    },
                ]
            )
        ]
    )
    if isinstance(msg.content, list):
        texts = [item["text"] for item in msg.content if isinstance(item, dict) and "text" in item]
        return "\n".join(texts) if texts else str(msg.content)
    return str(msg.content)


def generate_img_summaries(path):
    img_base64_list = []
    image_summaries = []

    prompt = """당신은 이미지를 요약하여 검색에 사용할 수 있도록 돕는 어시스턴트입니다.
이 요약은 임베딩되어 원본 이미지를 검색하는 데 사용됩니다.
이미지를 간결하게 요약하고 검색에 최적화된 내용을 작성하세요.
한국어로 작성하세요."""

    img_files = [f for f in sorted(os.listdir(path)) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    # figures 폴더에 이미지가 없으면 fire.pdf에서 페이지 렌더링
    if not img_files:
        pdf_file = "fire.pdf" if os.path.exists("fire.pdf") else os.path.join(fpath, fname)
        if os.path.exists(pdf_file):
            import pymupdf
            doc = pymupdf.open(pdf_file)
            for i, page in enumerate(doc):
                img_p = os.path.join(path, f"figure-page-{i+1}.jpg")
                pix = page.get_pixmap(dpi=150)
                pix.save(img_p)
            img_files = [f for f in sorted(os.listdir(path)) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    for img_file in img_files:
        img_path = os.path.join(path, img_file)
        base64_image = encode_image(img_path)
        img_base64_list.append(base64_image)
        print(f"[이미지 요약 중] {img_file} 분석...")
        summary = image_summarize(base64_image, prompt)
        image_summaries.append(summary)

    return img_base64_list, image_summaries


img_base64_list, image_summaries = generate_img_summaries(figures_path)


# MultiVectorRetriever 및 Chroma 벡터스토어 구성
try:
    from langchain.retrievers.multi_vector import MultiVectorRetriever
except ImportError:
    from langchain_classic.retrievers.multi_vector import MultiVectorRetriever

try:
    from langchain_core.stores import InMemoryStore
except ImportError:
    from langchain.storage import InMemoryStore

try:
    from langchain_chroma import Chroma
except ImportError:
    from langchain_community.vectorstores import Chroma

from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def create_multi_vector_retriever(
    vectorstore, text_summaries, texts, table_summaries, tables, image_summaries, images
):
    store = InMemoryStore()
    id_key = "doc_id"

    retriever = MultiVectorRetriever(
        vectorstore=vectorstore,
        docstore=store,
        id_key=id_key,
    )

    def add_documents(retriever, doc_summaries, doc_contents):
        doc_ids = [str(uuid.uuid4()) for _ in doc_contents]
        summary_docs = [
            Document(page_content=s, metadata={id_key: doc_ids[i]})
            for i, s in enumerate(doc_summaries)
        ]
        retriever.vectorstore.add_documents(summary_docs)
        retriever.docstore.mset(list(zip(doc_ids, doc_contents)))

    if text_summaries:
        add_documents(retriever, text_summaries, texts)
    if table_summaries:
        add_documents(retriever, table_summaries, tables)
    if image_summaries:
        add_documents(retriever, image_summaries, images)

    return retriever


embedding_model_name = "models/gemini-embedding-001"
embeddings = GoogleGenerativeAIEmbeddings(model=embedding_model_name)

vectorstore = Chroma(
    collection_name="multimodal_rag", embedding_function=embeddings
)

retriever_multi_vector_img = create_multi_vector_retriever(
    vectorstore,
    text_summaries,
    texts,
    table_summaries,
    tables,
    image_summaries,
    img_base64_list,
)


# 멀티모달 RAG 체인 구성
from langchain_core.runnables import RunnableLambda, RunnablePassthrough


def plt_img_base64(img_base64):
    try:
        from IPython.display import HTML, display
        from IPython import get_ipython
        if get_ipython() is not None:
            image_html = f'<img src="data:image/jpeg;base64,{img_base64}" />'
            display(HTML(image_html))
        else:
            print(f"[이미지 표시 (Base64 길이: {len(img_base64)})]")
    except Exception:
        print(f"[이미지 표시 (Base64 길이: {len(img_base64)})]")


def looks_like_base64(sb):
    return re.match("^[A-Za-z0-9+/]+[=]{0,2}$", sb) is not None


def is_image_data(b64data):
    image_signatures = {
        b"\xff\xd8\xff": "jpg",
        b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a": "png",
        b"\x47\x49\x46\x38": "gif",
        b"\x52\x49\x46\x46": "webp",
    }
    try:
        header = base64.b64decode(b64data)[:8]
        for sig, format in image_signatures.items():
            if header.startswith(sig):
                return True
        return False
    except Exception:
        return False


def resize_base64_image(base64_string, size=(128, 128)):
    img_data = base64.b64decode(base64_string)
    img = Image.open(io.BytesIO(img_data))

    resized_img = img.resize(size, Image.LANCZOS)

    buffered = io.BytesIO()
    fmt = img.format if img.format else "JPEG"
    resized_img.save(buffered, format=fmt)

    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def split_image_text_types(docs):
    b64_images = []
    texts = []
    for doc in docs:
        if isinstance(doc, Document):
            doc = doc.page_content
        if looks_like_base64(doc) and is_image_data(doc):
            doc = resize_base64_image(doc, size=(1300, 600))
            b64_images.append(doc)
        else:
            texts.append(doc)
    return {"images": b64_images, "texts": texts}


def img_prompt_func(data_dict):
    formatted_texts = "\n".join(data_dict["context"]["texts"])
    messages = []

    if data_dict["context"]["images"]:
        for image in data_dict["context"]["images"]:
            image_message = {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image}"},
            }
            messages.append(image_message)

    text_message = {
        "type": "text",
        "text": (
            "당신은 인텔리전트 Q&A 챗봇입니다. \n"
            "사용자가 제공하는 텍스트, 표, 그리고 주로 차트나 그래프 형태의 이미지를 바탕으로 정보를 분석합니다.\n"
            "이 정보를 활용하여 사용자 질문에 관련된 조언을 제공합니다. \n"
            f"사용자가 제공한 질문: {data_dict['question']}\n\n"
            "텍스트나 테이블:\n"
            f"{formatted_texts}"
        ),
    }
    messages.append(text_message)
    return [HumanMessage(content=messages)]


def multi_modal_rag_chain(retriever):
    model = ChatGoogleGenerativeAI(temperature=0, model=model_name, max_tokens=4096)
    chain = (
        {
            "context": retriever | RunnableLambda(split_image_text_types),
            "question": RunnablePassthrough(),
        }
        | RunnableLambda(img_prompt_func)
        | model
        | StrOutputParser()
    )

    return chain


chain_multimodal_rag = multi_modal_rag_chain(retriever_multi_vector_img)


# 질의 및 결과 확인
print(f"\n총 {len(img_base64_list)}개의 이미지가 로드되었습니다.")
for i in range(len(img_base64_list)):
    plt_img_base64(img_base64_list[i])

# Check retrieval
query = "소화전 사용 방법을 알려주세요"
print(f"\n[질의 실행] '{query}'")
docs = retriever_multi_vector_img.invoke(query, limit=6)

print(f"검색된 관련 문서/이미지 수: {len(docs)}")
for i in range(len(docs)):
    plt_img_base64(docs[i])

# 특정 이미지 요약 확인 (소화전 관련 이미지 인덱스)
sample_idx = 19 if len(img_base64_list) > 19 else (3 if len(img_base64_list) > 3 else 0)
print(f"\n[선택된 이미지 ({sample_idx+1}번) 요약 내용]")
print(image_summaries[sample_idx])

# Run RAG chain
print("\n[멀티모달 RAG 최종 응답 결과]")
result = chain_multimodal_rag.invoke(query)

print("\n" + "=" * 50)
print(result)
print("=" * 50)

#%%

"""
 ### 스크립트 실행 결과 요약

    [질의 실행] '소화전 사용 방법을 알려주세요'
    검색된 관련 문서/이미지 수: 4

    [선택된 이미지 (4번) 요약 내용]
    이 이미지는 소방청에 서 제작한 '화재 시 국민행동요령' 안내문입니다. 주요 내용은 다음과 같습니다.
    1. 소화기 사용법 (안전핀 뽑기 -> 노즐 조준 -> 손잡이 움켜쥐기 -> 분말 살포)
    2. 소화전 사용법 (함 문 열기 -> 호스 및 노즐 잡기 -> 밸브 돌리기 -> 방수)
    3. 옷에 불이 붙었을 때 대처법 (멈추기 -> 눈·코·입 보호 -> 엎드리기 -> 구르기)

    [멀티모달 RAG 최종 응답 결과]
    ==================================================
    제공해주신 이미지의 '소화전 사용 방법' 섹션에 따른 단계별 안내입니다. 소화전은 보통 2인 1조로 사용하는 것이 권장됩니다.

    [소화전 사용 방법]
    1. 문 열기: 소화전함의 문을 엽니다.
    2. 호스 및 노즐 준비: 호스를 꺼내고 노즐을 잡습니다. (호스가 꼬이지 않도록 길게 늘어뜨린 후 노즐을 잡고 방수 자세를 취합니다.)
    3. 밸브 열기: 다른 한 사람이 밸브를 돌려 물이 나오는 것을 확인한 후, 먼저 나간 사람의 호스 잡는 것을 도와줍니다.
    4. 방수: 노즐의 끝을 돌려 물의 양을 조절해가며 불을 끕니다.

    주의사항:
    * 2인 1조로 행동하는 것이 안전하며, 호스가 꼬이지 않게 주의해야 합니다.
    * 화재 시 엘리베이터는 이용하지 말고 계단을 통해 대피하는 것이 우선입니다.
    ==================================================
"""    