#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

model_name = "gemini-3.1-flash-lite"

# In[3]:


#from google.colab import drive
# drive.mount('/content/drive')


# In[4]:


# get_ipython().system('pip install -U langchain-community pymupdf faiss-cpu langchain-google-genai')
# pip install -U langchain-community pymupdf faiss-cpu langchain-google-genai


# In[5]:


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
    temperature=0.3,
    max_tokens=1024
)

# Query expansion 함수
def expand_query(original_query):
    expansion_prompt = f"다음 질문을 확장하여 관련된 다양한 키워드와 문구를 간결하게 한국어로 생성해주세요. 설명이나 문장 형태의 답변은 하지 마세요. 원래 질문: '{original_query}'"
    response = llm.invoke(expansion_prompt)
    if hasattr(response, "text") and response.text:
        expanded_query = response.text.strip()
    elif isinstance(response.content, str):
        expanded_query = response.content.strip()
    elif isinstance(response.content, list):
        expanded_query = "".join(part.get("text", "") if isinstance(part, dict) else str(part) for part in response.content).strip()
    else:
        expanded_query = str(response.content).strip()
    return expanded_query

# 원래 쿼리
original_query = "국내 고령화 전망에 대해 알려주세요"

# 쿼리 확장
expanded_query = expand_query(original_query)
print(f"확장된 쿼리: {expanded_query}\n")

# 확장된 쿼리로 검색 수행
search_results = vectorstore.similarity_search(expanded_query, k=5)

# 결과 출력
print("## 검색 결과")
for i, doc in enumerate(search_results):
    print(f"관련 문서 {i+1}:")
    print(doc.page_content[:100] + "...\n")
