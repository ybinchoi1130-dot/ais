#!/usr/bin/env python
# coding: utf-8

# In[1]:

import getpass
import json
import os
import re
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

# PDF 로드
# loader = PyMuPDFLoader("/content/drive/MyDrive/Colab Notebooks/pdf/BBS_202402151054353090.pdf")
loader = PyMuPDFLoader("./BBS_202402151054353090.pdf")
documents = loader.load()

# 텍스트 분할
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Document 객체에서 텍스트 내용 추출
text_contents = [doc.page_content for doc in texts]

# 임베딩 모델 설정 (Google Gemini 임베딩 모델)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
# HuggingFace 로컬 임베딩을 사용하는 경우:
# from langchain_community.embeddings import HuggingFaceEmbeddings
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# 벡터 스토어 설정
vectorstore = FAISS.from_texts(text_contents, embeddings)

# Google Gemini 모델 설정
llm = ChatGoogleGenerativeAI(
    model=model_name,  # "gemini-3.1-flash-lite"
    temperature=0,
    max_tokens=1024
)

# Gemini 기반 Reranker 함수
def rerank_documents(query, docs, top_k=5):
    docs_text = "\n\n".join([f"[문서 {i}]: {doc.page_content[:500]}" for i, doc in enumerate(docs)])
    prompt = f"""다음 질의와 각 문서 간의 관련성을 엄밀히 평가하여 0.0에서 1.0 사이의 유사도 점수를 매겨주세요.
관련성이 높은 순서대로 정렬하여 JSON 배열 형식으로만 출력하세요.

질의: {query}

문서 목록:
{docs_text}

출력 형식(반드시 이 JSON 형식만 출력):
[
  {{"index": 0, "score": 0.95}},
  ...
]
"""
    res = llm.invoke(prompt)
    if isinstance(res.content, str):
        text = res.content
    elif isinstance(res.content, list):
        text = "".join(part.get("text", "") if isinstance(part, dict) else str(part) for part in res.content)
    else:
        text = str(res.content)

    match = re.search(r"\[[\s\S]*\]", text)
    if match:
        ranked_list = json.loads(match.group(0))
        reranked_docs = []
        for item in ranked_list[:top_k]:
            idx = item["index"]
            score = float(item["score"])
            reranked_docs.append((docs[idx], score))
        return reranked_docs
    return [(doc, 0.0) for doc in docs[:top_k]]

# (참고) 로컬 HuggingFace BGE Reranker를 사용하는 경우:
# import torch
# from transformers import AutoModelForSequenceClassification, AutoTokenizer
# reranker_model_name = "BAAI/bge-reranker-v2-m3"
# tokenizer = AutoTokenizer.from_pretrained(reranker_model_name)
# model = AutoModelForSequenceClassification.from_pretrained(reranker_model_name)
# def rerank_documents_bge(query, docs, top_k=5):
#     pairs = [[query, doc.page_content] for doc in docs]
#     with torch.no_grad():
#         inputs = tokenizer(pairs, padding=True, truncation=True, return_tensors="pt", max_length=512)
#         scores = model(**inputs).logits.squeeze(-1)
#     ranked_indices = scores.argsort(descending=True)
#     return [(docs[i], scores[i].item()) for i in ranked_indices[:top_k]]

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
