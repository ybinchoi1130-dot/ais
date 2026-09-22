#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 필수 라이브러리를 설치합니다.
# LangChain: 문서 로딩 및 텍스트 처리 기능 제공
# PyPDF: PDF 파일을 로드하고 텍스트로 변환하는 데 사용
# LangChain 커뮤니티: 추가적인 기능과 플러그인을 포함한 패키지
get_ipython().system('pip install langchain==0.3.14')
get_ipython().system('pip install pypdf==5.1.0')
get_ipython().system('pip install langchain_community==0.3.14')


# In[ ]:


# 필요한 모듈을 임포트합니다.
import pickle
from langchain.document_loaders import PyPDFLoader  # PDF 파일 로딩 및 텍스트 변환 기능
from langchain.text_splitter import RecursiveCharacterTextSplitter  # 텍스트 청킹을 위한 모듈


# In[ ]:


# PDF 파일을 로드하고 텍스트를 청킹하는 함수 정의
# pdf_path: PDF 파일 경로
# chunk_size: 각 청크의 크기
# chunk_overlap: 청크 간 겹치는 부분
def load_pdf_and_chunk(pdf_path, chunk_size=1024, chunk_overlap=128):
    # 지정된 경로의 PDF 파일을 로드하는 PyPDFLoader 객체 생성
    loader = PyPDFLoader(pdf_path)

    # PDF 파일을 로드하여 텍스트 형식으로 변환
    documents = loader.load()

    # 청킹 설정: 지정된 크기와 겹침을 기준으로 텍스트를 청크 단위로 나눔
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    # 텍스트를 청크 단위로 나누어 chunks 변수에 저장
    chunks = text_splitter.split_documents(documents)
    return chunks

# 청킹할 PDF 파일 경로를 지정하고 청킹 작업을 수행합니다.
pdf_path = "전자금융거래법(법률)(제17354호)(20201210).pdf"
chunks = load_pdf_and_chunk(pdf_path)  # PDF 파일을 청크로 나누고 결과를 chunks에 저장

# 청크된 텍스트 데이터를 저장할 리스트를 생성하고, 청크 내용을 확인하여 저장합니다.
chunk_list = []
for i, chunk in enumerate(chunks):  # 각 청크를 순회하며 결과 확인
    # 청크 인덱스 출력
    print(f"Chunk {i+1}:")

    # 현재 청크의 텍스트 내용 출력
    print(chunk.page_content)

    # chunk_list에 청크 내용을 추가
    chunk_list.append(chunk.page_content)

    # 구분선 출력
    print("-" * 50)


# In[ ]:


# 청킹된 데이터를 pickle을 사용하여 바이너리 파일로 저장합니다.
with open('전자금융거래.pk', 'wb') as f:
    pickle.dump(chunk_list, f)  # chunk_list를 바이너리 파일로 저장

