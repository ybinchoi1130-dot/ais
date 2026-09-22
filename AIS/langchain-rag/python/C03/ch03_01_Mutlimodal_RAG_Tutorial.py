#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


from google.colab import userdata
os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')


# In[3]:


from google.colab import drive
drive.mount('/content/drive')


# In[4]:


# get_ipython().system('pip install -U  langchain==0.3.7  openai==1.55.0  langchain-chroma==0.1.4  langchain-experimental==0.3.3  SQLAlchemy==2.0.35  chromadb==0.5.20  fastapi==0.115.5  dataclasses-json==0.6.7  httpx-sse==0.4.0  pydantic==2.9.2  pydantic-settings==2.6.1')
# pip install -U  langchain==0.3.7  openai==1.55.0  langchain-chroma==0.1.4  langchain-experimental==0.3.3  SQLAlchemy==2.0.35  chromadb==0.5.20  fastapi==0.115.5  dataclasses-json==0.6.7  httpx-sse==0.4.0  pydantic==2.9.2  pydantic-settings==2.6.1


# In[5]:


# get_ipython().system('pip install  unstructured[all-docs]==0.16.6  pillow==11.0.0  pydantic==2.9.2  lxml==5.3.0  matplotlib==3.8.0  chromadb==0.5.20  tiktoken==0.8.0')
# pip install  unstructured[all-docs]==0.16.6  pillow==11.0.0  pydantic==2.9.2  lxml==5.3.0  matplotlib==3.8.0  chromadb==0.5.20  tiktoken==0.8.0


# In[ ]:

"""
get_ipython().system('sudo apt-get update')
get_ipython().system('pip install pdf2image==1.17.0')
get_ipython().system('pip install --user -U nltk==3.9.1')
get_ipython().system('apt-get install -y poppler-utils')
get_ipython().system('apt install -y tesseract-ocr')
get_ipython().system('apt install -y libtesseract-dev')
"""

#%%

# get_ipython().system('sudo apt-get update')
# get_ipython().system('pip install pdf2image==1.17.0')
# get_ipython().system('pip install --user -U nltk==3.9.1')
# get_ipython().system('apt-get install -y poppler-utils')
# get_ipython().system('apt install -y tesseract-ocr')
# get_ipython().system('apt install -y libtesseract-dev')


# In[6]:


# get_ipython().system('pip install --upgrade  nltk==3.9.1  click==8.1.7  joblib==1.4.2  regex==2024.9.11  tqdm==4.66.6')
# pip install --upgrade  nltk==3.9.1  click==8.1.7  joblib==1.4.2  regex==2024.9.11  tqdm==4.66.6

#%%

import nltk, os
nltk.download('punkt')
os.makedirs('/root/nltk_data/tokenizers/punkt/PY3_tab', exist_ok=True)


# In[7]:


from langchain_text_splitters import CharacterTextSplitter
from unstructured.partition.pdf import partition_pdf
import os
os.environ['PATH'] += ':/usr/local/bin/tesseract'

def extract_pdf_elements(path, fname):
    return partition_pdf(
        filename=path + fname,
        extract_images_in_pdf=True,
        infer_table_structure=True,
        chunking_strategy="by_title",
        max_characters=4000,
        new_after_n_chars=3800,
        combine_text_under_n_chars=2000,
        image_output_dir_path=path,
    )


def categorize_elements(raw_pdf_elements):
    tables = []
    texts = []
    for element in raw_pdf_elements:
        if "unstructured.documents.elements.Table" in str(type(element)):
            tables.append(str(element))
        elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
            texts.append(str(element))
    return texts, tables


fpath = "/content/drive/MyDrive/Colab Notebooks/pdf/"
fname = "fire.pdf"

raw_pdf_elements = extract_pdf_elements(fpath, fname)

texts, tables = categorize_elements(raw_pdf_elements)

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=4000, chunk_overlap=0
)
joined_texts = " ".join(texts)
texts_4k_token = text_splitter.split_text(joined_texts)


# In[8]:


figures_path = "/content/figures/"


# In[9]:


# get_ipython().system('pip install  langchain-openai==0.2.9  langchain-core==0.3.19  openai==1.55.0  tiktoken==0.8.0  PyYAML==6.0.2  jsonpatch==1.33  langsmith==0.1.143  packaging==24.2  pydantic==2.9.2  tenacity==9.0.0  typing-extensions==4.12.2  anyio==3.7.1  distro==1.9.0  httpx==0.27.2  jiter==0.7.1  sniffio==1.3.1  tqdm==4.66.6  regex==2024.9.11  requests==2.32.3  exceptiongroup==1.2.2  certifi==2024.8.30  httpcore==1.0.7  h11==0.14.0  jsonpointer==3.0.0  orjson==3.10.11  requests-toolbelt==1.0.0  annotated-types==0.7.0  pydantic-core==2.23.4  charset-normalizer==3.4.0  urllib3==2.2.3')
# pip install  langchain-openai==0.2.9  langchain-core==0.3.19  openai==1.55.0  tiktoken==0.8.0  PyYAML==6.0.2  jsonpatch==1.33  langsmith==0.1.143  packaging==24.2  pydantic==2.9.2  tenacity==9.0.0  typing-extensions==4.12.2  anyio==3.7.1  distro==1.9.0  httpx==0.27.2  jiter==0.7.1  sniffio==1.3.1  tqdm==4.66.6  regex==2024.9.11  requests==2.32.3  exceptiongroup==1.2.2  certifi==2024.8.30  httpcore==1.0.7  h11==0.14.0  jsonpointer==3.0.0  orjson==3.10.11  requests-toolbelt==1.0.0  annotated-types==0.7.0  pydantic-core==2.23.4  charset-normalizer==3.4.0  urllib3==2.2.3


# In[10]:


from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def generate_text_summaries(texts, tables, summarize_texts=False):
    prompt_text = """당신은 테이블과 텍스트를 요약하여 검색에 사용할 수 있도록 돕는 어시스턴트입니다. \
이 요약은 임베딩되어 원문 텍스트 또는 테이블 요소를 검색하는 데 사용됩니다. \
테이블 또는 텍스트를 간결하게 요약하고 검색에 최적화된 내용을 작성하세요. 테이블 또는 텍스트: {element} \
한국어로 작성하세요."""
    prompt = ChatPromptTemplate.from_template(prompt_text)

    model = ChatOpenAI(temperature=0, model="gpt-4o")
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


# In[11]:


import base64
import os

from langchain_core.messages import HumanMessage


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def image_summarize(img_base64, prompt):
    chat = ChatOpenAI(model="gpt-4o", max_tokens=1024)

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
    return msg.content


def generate_img_summaries(path):
    img_base64_list = []

    image_summaries = []

    prompt = """당신은 이미지를 요약하여 검색에 사용할 수 있도록 돕는 어시스턴트입니다.
이 요약은 임베딩되어 원본 이미지를 검색하는 데 사용됩니다.
이미지를 간결하게 요약하고 검색에 최적화된 내용을 작성하세요.
한국어로 작성하세요."""

    for img_file in sorted(os.listdir(path)):
        if img_file.endswith(".jpg"):
            img_path = os.path.join(path, img_file)
            base64_image = encode_image(img_path)
            img_base64_list.append(base64_image)
            image_summaries.append(image_summarize(base64_image, prompt))

    return img_base64_list, image_summaries

img_base64_list, image_summaries = generate_img_summaries(figures_path)


# In[12]:


import uuid

from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.storage import InMemoryStore
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

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

vectorstore = Chroma(
    collection_name="multimodal_rag", embedding_function=OpenAIEmbeddings()
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


# In[13]:


import io
import re

from IPython.display import HTML, display
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from PIL import Image


def plt_img_base64(img_base64):
    image_html = f'<img src="data:image/jpeg;base64,{img_base64}" />'
    display(HTML(image_html))


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
    resized_img.save(buffered, format=img.format)

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
    model = ChatOpenAI(temperature=0, model="gpt-4o", max_tokens=1024)
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


# In[14]:


for i in range(len(img_base64_list)):
  plt_img_base64(img_base64_list[i])


# In[15]:


# Check retrieval
query = "소화전 사용 방법을 알려주세요"
docs = retriever_multi_vector_img.invoke(query, limit=6)


# In[16]:


# We get back relevant images
for i in range(len(docs)):
  plt_img_base64(docs[i])


# In[17]:


plt_img_base64(img_base64_list[19])


# In[18]:


print(image_summaries[19])


# In[19]:


# Run RAG chain
result = chain_multimodal_rag.invoke(query)


# In[20]:


print(result)


# In[20]:




