#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

# In[ ]:


# from google.colab import drive
# drive.mount('/content/drive')


# In[ ]:


# get_ipython().system('pip install -U langchain-community pymupdf faiss-cpu langchain-google-genai')
# pip install -U langchain-community pymupdf faiss-cpu langchain-google-genai

# In[ ]:


import logging
from typing import List
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
    from langchain.retrievers.multi_query import MultiQueryRetriever
except ImportError:
    from langchain_classic.retrievers.multi_query import MultiQueryRetriever

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import BaseOutputParser

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('langchain.retrievers.multi_query')
logger.setLevel(logging.INFO)

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
    template="""당신은 AI 언어 모델 어시스턴트입니다. 사용자가 제공한 질문에 대해 벡터 데이터베이스에서 관련 문서를 검색할 수 있도록 질문을 3가지 다른 버전으로 생성하는 것이 당신의 임무입니다.
사용자의 질문을 다양한 관점에서 재구성하여 거리 기반 유사도 검색의 한계를 극복할 수 있도록 돕는 것이 목표입니다.
각 버전의 질문은 줄바꿈으로 구분하여 작성하세요.
한국어로 작성하세요. 원본 질문: {question}"""
)

# 출력 파서 정의
class LineListOutputParser(BaseOutputParser):
    def parse(self, text: str) -> List[str]:
        return [line.strip() for line in str(text).strip().split("\n") if line.strip()]

# LLM 체인 생성
output_parser = LineListOutputParser()
llm_chain = custom_prompt | llm | output_parser

# 다중 쿼리 리트리버 설정
retriever_from_llm = MultiQueryRetriever(
    retriever=vectorstore.as_retriever(),
    llm_chain=llm_chain,
    parser_key="lines"
)
retriever_from_llm.verbose = True

# 쿼리 실행
query = "국내 고령화 전망에 대해 알려주세요"
results = retriever_from_llm.invoke(query)

# 결과 출력
print("\n## 검색 결과 (다중 쿼리 통합)")
for i, doc in enumerate(results[:5]):  # 상위 5개 결과만 출력
    print(f"\n관련 문서 {i+1}:")
    print(doc.page_content[:100] + "...")
