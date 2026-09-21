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


get_ipython().system('pip install -U  langchain-community==0.3.5  pymupdf==1.24.13  faiss-gpu==1.7.2  SQLAlchemy==2.0.35  dataclasses-json==0.6.7  httpx-sse==0.4.0  langchain-core==0.3.15  langchain==0.3.7  pydantic-settings==2.6.1  marshmallow==3.23.1  python-dotenv==1.0.1  typing-inspect==0.9.0  mypy-extensions==1.0.0')


# In[4]:


import torch
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import HypotheticalDocumentEmbedder
from langchain.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.prompts import PromptTemplate


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
        max_new_tokens=256,  # 생성할 최대 새 토큰 수
        do_sample=True,
        temperature=0.7,
        top_p=0.95,
        device=0 if torch.cuda.is_available() else -1
    )
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
print(llm(custom_prompt.format(question=query)))
print("생성된 임베딩:", hyde_embedding[:10])  # 임베딩의 처음 10개 값만 출력

# 결과 출력
for i, doc in enumerate(results[:5]):  # 상위 5개 결과만 출력
    print(f"관련 문서 {i+1}:")
    print(doc.page_content[:100] + "...\n")

