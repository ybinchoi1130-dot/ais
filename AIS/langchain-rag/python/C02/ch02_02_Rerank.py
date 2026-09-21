#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from google.colab import userdata
os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')


# In[2]:


from google.colab import drive
drive.mount('/content/drive')


# In[3]:


get_ipython().system('pip install -U  langchain-community==0.3.5  pymupdf==1.24.13  faiss-gpu==1.7.2  SQLAlchemy==2.0.35  dataclasses-json==0.6.7  httpx-sse==0.4.0  pydantic-settings==2.6.1  marshmallow==3.23.1  python-dotenv==1.0.1  typing-inspect==0.9.0  mypy-extensions==1.0.0')


# In[4]:


import torch
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# PDF 로드
loader = PyMuPDFLoader("/content/drive/MyDrive/Colab Notebooks/pdf/BBS_202402151054353090.pdf")
documents = loader.load()

# 텍스트 분할
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Document 객체에서 텍스트 내용 추출
text_contents = [doc.page_content for doc in texts]

# 임베딩 모델 설정
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# 벡터 스토어 설정
vectorstore = FAISS.from_texts(text_contents, embeddings)

# BGE Reranker 모델 설정
model_name = "BAAI/bge-reranker-v2-m3"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def rerank_documents(query, docs, top_k=5):
    pairs = [[query, doc.page_content] for doc in docs]
    with torch.no_grad():
        inputs = tokenizer(pairs, padding=True, truncation=True, return_tensors="pt", max_length=512)
        scores = model(**inputs).logits.squeeze(-1)
    ranked_indices = scores.argsort(descending=True)
    reranked_docs = [(docs[i], scores[i].item()) for i in ranked_indices[:top_k]]
    return reranked_docs

# 리트리버 설정
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 20})

# 쿼리 실행
query = "국내 고령화 전망에 대해 알려주세요"

# 기본 검색 결과 출력
print("## 기본 검색 결과")
base_docs = base_retriever.invoke(query)
for i, doc in enumerate(base_docs[:5]):
    print(f"문서 {i+1}:")
    print(doc.page_content[:100] + "...\n")

# 리랭킹 결과 출력
print("\n## 리랭킹 결과")
reranked_docs = rerank_documents(query, base_docs)
for i, (doc, score) in enumerate(reranked_docs):
    print(f"문서 {i+1} (점수: {score:.4f}):")
    print(doc.page_content[:100] + "...\n")

