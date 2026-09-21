#!/usr/bin/env python
# coding: utf-8

# 

# In[ ]:


# get_ipython().system('pip install langchain==0.3.14 langchain-community==0.3.14 openai==1.59.4 chromadb==0.6.2 tiktoken==0.8.0 pypdf langchain_openai==0.3.0')
# pip install langchain==0.3.14 langchain-community==0.3.14 openai==1.59.4 chromadb==0.6.2 tiktoken==0.8.0 pypdf langchain_openai==0.3.0


# 

# # 예제2.1

# In[ ]:


import os
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI # 새로운 import 경로
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI

#%%

# os.environ['OPENAI_API_KEY'] ="<OpenAI API 키>" # API 키를 입력하세요.


# # 예제2.2

# In[ ]:


# CoLab 환경

"""
from google.colab import drive
from langchain_community.document_loaders import PyPDFLoader

drive.mount('/content/drive')   #드라이브 마운트

file_path = (
    "/content/drive/MyDrive/wikibooks/마스터파일/코드/2장 코드/이슈리포트 Vol.6 고령화시대 해결을 위한 기술개발.pdf"
)

# file_path = ("./issue-report.pdf")

# pdf load
loader = PyPDFLoader(file_path)  # PyPDFLoader를 통한 문서데이터 로드
pages = []

async for page in loader.alazy_load(): # 비동기로드
    pages.append(page)
"""

#%%

# Spyder 및 Jupyter 환경
import asyncio
import nest_asyncio
from langchain_community.document_loaders import PyPDFLoader

# Spyder/Jupyter 환경의 이벤트 루프 충돌 방지
nest_asyncio.apply()

file_path = ("./issue-report.pdf")

pages = []

# 2. 비동기 처리를 위한 함수 정의
async def load_pdf_asyncly():
    loader = PyPDFLoader(file_path)
    
    # async for는 반드시 async def 함수 내부에 있어야 합니다!
    async for page in loader.alazy_load(): 
        pages.append(page)
        
    print(f"총 {len(pages)} 페이지를 비동기로 로드했습니다.")
    return pages

# 3. 비동기 함수 실행
pages_result = asyncio.run(load_pdf_asyncly())

# In[ ]:


pages[10]


# # 예제2.3

# In[ ]:


text_splitter = CharacterTextSplitter(
    chunk_size=500, # 각 청크의 최대 길이를 500자로 설정합니다.
    chunk_overlap=40,  # 최소한의 중복만 허용하여 문맥의 연속성 유지
    length_function=len,
    separator="\n"
)
# 문서를 청크로 분할
texts = text_splitter.split_documents(pages)


# #예제 2.4

# In[ ]:


print("한 문장의 길이 :", len("첫 번째 문단입니다.")) # --11자

text = """첫 번째 문단입니다.
두 번째 문단입니다.
세 번째 문단입니다.
네 번째 문단입니다.
"""

# 작은 오버랩
text_splitter_small = CharacterTextSplitter(
    chunk_size=30,
    chunk_overlap=5,  # 작은 오버랩
    separator="\n"
)

print("=== 작은 오버랩 (chunk_overlap=5) ===")
chunks = text_splitter_small.split_text(text)
for i, chunk in enumerate(chunks, 1):
    print(f"청크 {i}: {chunk}\n")

#%%

# 큰 오버랩
text_splitter_large = CharacterTextSplitter(
    chunk_size=30,
    chunk_overlap=12,  # 큰 오버랩
    separator="\n"
)

print("=== 큰 오버랩 (chunk_overlap=12) ===")
chunks = text_splitter_large.split_text(text)
for i, chunk in enumerate(chunks, 1):
    print(f"청크 {i}: {chunk}\n")


# In[ ]:


text = """첫 번째 문단입니다.
두 번째 문단입니다.
세 번째 문단입니다.
네 번째 문단입니다."""

text_splitter = CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=15,
    separator="\n"
)

chunks = text_splitter.split_text(text)
for i, chunk in enumerate(chunks, 1):
    print(f"청크 {i}: {chunk}\n")


# # 예제2.5
# 

# In[ ]:


# OpenAI 임베딩 초기화
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
# OpenAI의 text-embedding-ada-002 모델을 사용하여 텍스트를 벡터로 변환하는 객체를 초기화합니다.

# Chroma 벡터 DB 생성
vectordb = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory="chroma_db_v1"  # 벡터 DB 저장 경로
)
# texts의 각 청크를 임베딩하여 Chroma DB에 저장합니다.

# 벡터 DB 저장
vectordb.persist()


# # 예제2.6

# In[ ]:


# 디스크에서 벡터 스토어 로드
vectordb = Chroma(
    persist_directory="chroma_db_v1",
    embedding_function=embeddings
)

# 저장된 데이터 조회 및 출력
print("=== Chroma 벡터 DB에 저장된 데이터 ===")
collection = vectordb._collection
data = collection.get(include=['embeddings', 'documents', 'metadatas'])
print(f"\n1. 컬렉션 크기: {collection.count()} 문서")

# 첫 번째 문서의 임베딩 정보 출력
print("\n2. 첫 번째 문서의 임베딩 정보:")
print(f"벡터 차원: {len(data['embeddings'][0])}")                      # 벡터 차원: 1536
print(f"임베딩 벡터 (앞부분 5개 요소): {data['embeddings'][0][:5]}")   # 임베딩 벡터 (앞부분 5개 요소): [-0.00650233 -0.02214683 -0.00151617 -0.02760713 -0.00187046]

# 문서와 메타데이터 출력 (2개 예시)
print("\n3. 문서 및 메타데이터 (2개):")
for idx, (document, metadata) in enumerate(zip(data['documents'][20:22], data['metadatas'][20:22])):
    print(f"인덱스: {idx}, 문서: {document}, 메타데이터: {metadata}")


# # 예제2.7

# In[ ]:


retriever = vectordb.as_retriever(
    search_type="mmr",      # Maximal Marginal Relevance 검색
    search_kwargs={
        "k": 5,             # 최종 검색 문서 수
        "fetch_k": 8,       # 초기 검색 문서 수
        "lambda_mult": 0.7  # 다양성 가중치 (1에 가까울수록 다양성)
    }
)

# 프롬프트 작성
prompt = ChatPromptTemplate.from_messages([
    ("system", """주어진 문서들을 기반으로 질문에 정확하게 답변해주세요.
    다음 지침을 반드시 따라주세요:
    1. 문서의 정보만을 사용하여 답변하세요
    2. 제품명이 언급된 경우 반드시 포함해서 답변하세요
    3. 제품의 기능과 특징을 구체적으로 설명하세요
    4. 답변에 확신이 없는 경우, 그 부분을 명시적으로 언급하세요

    문맥: {context}"""),
    ("human", "{input}")
])

# GPT-4o-mini 모델을 사용
llm = ChatOpenAI(
    temperature=0,  # 출력이 일정하도록 온도 설정
    max_tokens=400,  # 최대 토큰 수
    model_name="gpt-4o-mini"  # 사용할 모델 이름
)


# # 예제2.8

# In[ ]:


# 단일 문서 처리 체인 생성
document_chain = create_stuff_documents_chain(
    llm=llm,
    prompt=prompt
)

# 검색 및 응답 생성을 위한 최종 체인 생성
qa_chain = create_retrieval_chain(
    retriever=retriever,
    combine_docs_chain=document_chain
)


# # 예제2.9

# In[ ]:


def ask_question(question: str, qa_chain):
    # qa_chain.invoke()는 새로운 형식의 입력을 사용
    result = qa_chain.invoke({
        "input": question  # 'query' 대신 'input' 사용
    })
    print("질문:", question)
    print("\n답변:", result['answer'])  # 'result' 대신 'answer' 키 사용
    # source_documents가 있는 경우에만 출력
    if 'context' in result:
        print("\n참고 문서:")
        documents = result['context']
        for i, doc in enumerate(documents, 1):
            print(f"\n문서 {i}:")
            print(doc.page_content[:500], "...")
            if hasattr(doc, 'metadata'):
                print(f"(페이지: {doc.metadata.get('page', 'Unknown')})")
# 예시 질문
questions = [" 노인들이 일어나도록 도와주는 로봇의 제품 이름은 뭔가요? 그리고 특징을 알려주세요 "]

for question in questions:
    ask_question(question,qa_chain)
    print("\n" + "="*50 + "\n")


# # 실험1. 리트리버의 중요성

# In[ ]:


small_retriever = vectordb.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 2,        # 너무 적은 검색 결과
        "fetch_k": 3,  # 너무 적은 후보군
        "lambda_mult": 0.7
    }
)
# 체인에서 리트리버를 변경
qa_chain = create_retrieval_chain(
    retriever=small_retriever,
    combine_docs_chain=document_chain
)
# 예시 질문
questions = [" 노인들이 일어나도록 도와주는 로봇의 제품 이름은 뭔가요? 그리고 특징을 알려주세요 "]

for question in questions:
    ask_question(question,qa_chain)
    print("\n" + "="*50 + "\n")


# In[ ]:




