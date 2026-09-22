#!/usr/bin/env python
# coding: utf-8

# # Langchain Basic (Google Gemini)

# ### module install

# In[1]:


# get_ipython().system(' pip install -q -U langchain-google-genai')
# pip install -q -U langchain-google-genai


# In[2]:


import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    if "GEMINI_API_KEY" in os.environ:
        os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]
    else:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")

# model_name = "gemini-1.5-flash"
model_name = "gemini-3.1-flash-lite"


# ## 1.5.5 콜백 및 평가

# ### 콜백 및 토큰 사용량 확인

# In[3]:


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.callbacks import BaseCallbackHandler

# 1. LangChain 콜백 핸들러 정의 (이벤트 로깅)
class LoggingCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print("\n[Callback] LLM 호출이 시작되었습니다.")

    def on_llm_end(self, response, **kwargs):
        print("[Callback] LLM 호출이 완료되었습니다.")

# 콜백 핸들러 등록 및 Gemini 모델 초기화
handler = LoggingCallbackHandler()
llm = ChatGoogleGenerativeAI(model=model_name, temperature=0, callbacks=[handler])

# 모델 호출
response = llm.invoke("프랑스, 영국, 스페인의 수도는?")

# 2. 결과 및 토큰 사용량 출력 (LangChain 표준 usage_metadata 활용)
print("\n--- 모델 응답 ---")
print(response.content)

print("\n--- 토큰 사용량 ---")
if hasattr(response, "usage_metadata") and response.usage_metadata:
    print(f"Input Tokens : {response.usage_metadata.get('input_tokens')}")
    print(f"Output Tokens: {response.usage_metadata.get('output_tokens')}")
    print(f"Total Tokens : {response.usage_metadata.get('total_tokens')}")
else:
    print("Usage Metadata:", response.response_metadata.get("usage_metadata", {}))


# ### 스트리밍 콜백 예제

# In[4]:


from langchain_core.callbacks import StreamingStdOutCallbackHandler

# 실시간 텍스트 스트리밍 출력을 지원하는 콜백 핸들러
streaming_llm = ChatGoogleGenerativeAI(
    model=model_name,
    temperature=0,
    callbacks=[StreamingStdOutCallbackHandler()]
)

print("\n--- 실시간 스트리밍 콜백 출력 ---")
streaming_llm.invoke("대한민국의 사계절 특징을 한 줄씩 간단히 요약해 주세요.")




