#!/usr/bin/env python
# coding: utf-8

# # Langchain Basic (Google Gemini)

# ### module install

# In[ ]:


# get_ipython().system(' pip install -q -U langchain-google-genai langchain-community pypdf faiss-cpu')
# pip install -q -U langchain-google-genai langchain-community pypdf faiss-cpu


# In[ ]:

import getpass
import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

#%%
if "USER_AGENT" not in os.environ:
    os.environ["USER_AGENT"] = "Mozilla/5.0"

if "GOOGLE_API_KEY" not in os.environ:
    if "GEMINI_API_KEY" in os.environ:
        os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]
    else:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")


# ## 1.5.4 인덱스

# TextLoader

# In[ ]:


from langchain_community.document_loaders import TextLoader

# 텍스트 파일을 불러와 하나의 Document로 생성
loader = TextLoader("./ReAct README.md")
document = loader.load()

# 결과 확인
print(document)


# In[ ]:


from langchain_community.document_loaders import WebBaseLoader

# 웹 페이지 로더 설정
url = "https://n.news.naver.com/mnews/article/055/0001207714"
loader = WebBaseLoader(url)

# 웹 페이지 내용을 로드
document = loader.load()

# 결과 확인
print(document)


# In[ ]:


from langchain_community.document_loaders import PyPDFLoader

# PDF 파일 경로 설정
pdf_path = "./2210.03629v3-2.pdf"
loader = PyPDFLoader(pdf_path)

# PDF 파일 내용을 로드
document = loader.load()

# 결과 확인
print(document)


# VectorDatabase
# * embedding 작업이 다소 시간이 걸릴 수 있습니다.

# In[ ]:


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader

# 1. 텍스트 문서 로드
# pdf_path = "./2210.03629v3-2.pdf"
# loader = PyPDFLoader(pdf_path)
loader = TextLoader("./ReAct README.md")
documents = loader.load()

# 2. 문서 내용을 리스트로 변환
texts = [doc.page_content for doc in documents]
print(texts)

# 3. Google Gemini 임베딩 모델로 텍스트 임베딩 생성
# embedding_model_name = "models/embedding-001"
# embedding_model_name = "models/text-embedding-004"
embedding_model_name = "models/gemini-embedding-001"
embedding_model = GoogleGenerativeAIEmbeddings(model=embedding_model_name)
document_embeddings = embedding_model.embed_documents(texts)

# 4. FAISS 벡터 데이터베이스 생성 및 임베딩 저장
vector_db = FAISS.from_texts(texts, embedding_model)

# 5. 데이터베이스 상태 확인
print(f"총 {len(texts)} 개의 문서가 벡터 데이터베이스에 저장되었습니다.")


# In[ ]:


# 6. 쿼리 문장을 임베딩하여 벡터로 변환
query = "What is a document loader?"

# 7. 벡터 데이터베이스에서 쿼리와 유사한 문서 검색
search_results = vector_db.similarity_search(query, k=3)  # 상위 3개의 유사 문서 반환

# 검색 결과 출력
for i, result in enumerate(search_results, 1):
    print(f"유사 문서 {i}:")
    print(result.page_content)
    print()


# Textsplitter

# In[ ]:


from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 텍스트 로더 설정
loader = TextLoader("./ReAct README.md")

# 텍스트 스플리터 설정 (500자 단위로 분할)
splitter = RecursiveCharacterTextSplitter(chunk_size=500)

# 문서를 로드하면서 동시에 분할
documents = loader.load_and_split(text_splitter=splitter)

# 각 청크 확인
for doc in documents:
    print(doc)


# In[ ]:
