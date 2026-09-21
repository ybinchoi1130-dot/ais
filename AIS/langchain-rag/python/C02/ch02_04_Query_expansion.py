#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
from google.colab import userdata
os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')


# In[3]:


from google.colab import drive
drive.mount('/content/drive')


# In[4]:


get_ipython().system('pip install -U  langchain-community==0.3.5  pymupdf==1.24.13  faiss-gpu==1.7.2  SQLAlchemy==2.0.35  dataclasses-json==0.6.7  httpx-sse==0.4.0  pydantic-settings==2.6.1  marshmallow==3.23.1  python-dotenv==1.0.1  typing-inspect==0.9.0  mypy-extensions==1.0.0')


# In[5]:


import torch
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# PDF 로드 및 텍스트 분할
loader = PyMuPDFLoader("/content/drive/MyDrive/Colab Notebooks/pdf/BBS_202402151054353090.pdf")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)
text_contents = [doc.page_content for doc in texts]

# 임베딩 모델 설정
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# 벡터 스토어 설정
vectorstore = FAISS.from_texts(text_contents, embeddings)

# Qwen/Qwen2.5-1.5B-Instruct 모델 설정
model_name = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda" if torch.cuda.is_available() else "cpu")
llm = HuggingFacePipeline(
    pipeline=pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=1024,
        do_sample=True,
        temperature=0.3,
        top_p=0.85,
        repetition_penalty=1.2,
        device=0 if torch.cuda.is_available() else -1
    )
)

# Query expansion 함수
def expand_query(original_query):
    expansion_prompt = f"다음 질문을 확장하여 관련된 다양한 키워드와 문구를 간결하게 한국어로 생성해주세요. 설명이나 문장 형태의 답변은 하지 마세요. 원래 질문: '{original_query}'"
    expanded_query = llm(expansion_prompt).split(original_query)[-1]
    return expanded_query

# 원래 쿼리
original_query = "국내 고령화 전망에 대해 알려주세요"

# 쿼리 확장
expanded_query = expand_query(original_query)
print(f"확장된 쿼리: {expanded_query}")

# 확장된 쿼리로 검색 수행
search_results = vectorstore.similarity_search(expanded_query, k=5)

# 결과 출력
for i, doc in enumerate(search_results):
    print(f"관련 문서 {i+1}:")
    print(doc.page_content[:100] + "...\n")

