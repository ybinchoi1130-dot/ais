#!/usr/bin/env python
# coding: utf-8

# In[1]:


import getpass
import os
import sys

# Windows 콘솔 한글 인코딩 설정
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# from google.colab import userdata
# os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')

if "GOOGLE_API_KEY" not in os.environ:
    if "GEMINI_API_KEY" in os.environ:
        os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]
    else:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")

# model_name = "gemini-1.5-flash"
model_name = "gemini-3.1-flash-lite"


# In[2]:


# from google.colab import drive
# drive.mount('/content/drive')


# In[3]:


# get_ipython().system('pip install -U langchain-community pymupdf faiss-cpu langchain-google-genai')
# pip install -U langchain-community pymupdf faiss-cpu langchain-google-genai


# In[4]:


from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
try:
    from langchain_community.document_loaders import PyMuPDFLoader
except ImportError:
    from langchain.document_loaders import PyMuPDFLoader

try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

try:
    from langchain.embeddings import HypotheticalDocumentEmbedder
except ImportError:
    try:
        from langchain.chains.hyde.base import HypotheticalDocumentEmbedder
    except ImportError:
        from langchain_classic.chains.hyde.base import HypotheticalDocumentEmbedder

try:
    from langchain_core.prompts import PromptTemplate
except ImportError:
    from langchain.prompts import PromptTemplate


# PDF 로드 및 텍스트 분할
# loader = PyMuPDFLoader("/content/drive/MyDrive/Colab Notebooks/pdf/BBS_202402151054353090.pdf")
loader = PyMuPDFLoader("./BBS_202402151054353090.pdf")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)
text_contents = [doc.page_content for doc in texts]

# 임베딩 모델 설정 (Google Gemini 임베딩 모델)
embedding_model_name = "models/gemini-embedding-001"
embeddings = GoogleGenerativeAIEmbeddings(model=embedding_model_name)
# HuggingFace 로컬 임베딩을 사용하는 경우:
# from langchain_community.embeddings import HuggingFaceEmbeddings
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# 벡터 스토어 설정
vectorstore = FAISS.from_texts(text_contents, embeddings)

# Google Gemini 모델 설정
llm = ChatGoogleGenerativeAI(
    model=model_name,  # "gemini-3.1-flash-lite"
    temperature=0.7,
    max_tokens=256
)

# 사용자 정의 프롬프트 템플릿 생성
custom_prompt = PromptTemplate(
    input_variables=["question"],
    template="다음 질문에 대한 가상의 문서를 생성해주세요: {question}\n\n문서:"
)

# HyDE 설정
hyde = HypotheticalDocumentEmbedder.from_llm(
    llm=llm,
    base_embeddings=embeddings,
    custom_prompt=custom_prompt
)

# 쿼리 실행
query = "국내 고령화 전망에 대해 알려주세요"
hyde_embedding = hyde.embed_query(query)

# vectorstore를 사용하여 검색
results = vectorstore.similarity_search_by_vector(hyde_embedding)

# hyde.embed_query() 호출 전후에 중간 결과 출력
print("생성된 가상 문서:")
res = llm.invoke(custom_prompt.format(question=query))
print(getattr(res, "text", res.content))
print("\n생성된 임베딩 (앞부분 10개 요소):", hyde_embedding[:10])

# 결과 출력
print("\n## 관련 문서 검색 결과")
for i, doc in enumerate(results[:5]):  # 상위 5개 결과만 출력
    print(f"\n관련 문서 {i+1}:")
    print(doc.page_content[:100] + "...")
