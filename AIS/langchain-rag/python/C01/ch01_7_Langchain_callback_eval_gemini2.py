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
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

if "GOOGLE_API_KEY" not in os.environ:
    if "GEMINI_API_KEY" in os.environ:
        os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]
    else:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")

# model_name = "gemini-1.5-flash"
model_name = "gemini-3.1-flash-lite"


# ## 1.5.5 콜백 및 평가

# ### 콜백

# In[3]:


from contextlib import contextmanager
from langchain_core.callbacks import BaseCallbackHandler
from langchain_google_genai import ChatGoogleGenerativeAI


class GeminiCallbackHandler(BaseCallbackHandler):
    """Google Gemini 토큰 사용량 및 비용 추적 콜백 핸들러"""

    def __init__(self):
        self.total_tokens = 0
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.total_cost = 0.0

    def on_llm_end(self, response, **kwargs):
        # 1. generations 내부의 메시지 usage_metadata에서 토큰 정보 추출 (LangChain 표준)
        if hasattr(response, "generations"):
            for gen_list in response.generations:
                for gen in gen_list:
                    msg = getattr(gen, "message", None)
                    if msg and hasattr(msg, "usage_metadata") and msg.usage_metadata:
                        meta = msg.usage_metadata
                        self.prompt_tokens += meta.get("input_tokens", 0)
                        self.completion_tokens += meta.get("output_tokens", 0)
                        self.total_tokens += meta.get("total_tokens", 0)

        # 2. llm_output에서 토큰 정보 추출 (대체 경로)
        if self.total_tokens == 0 and hasattr(response, "llm_output") and response.llm_output:
            usage = response.llm_output.get("token_usage", {})
            self.prompt_tokens += usage.get("prompt_tokens", 0)
            self.completion_tokens += usage.get("completion_tokens", 0)
            self.total_tokens += usage.get("total_tokens", 0)

        # gemini-3.1-flash-lite 기준 예상 비용 계산 (1M 토큰당: 입력 $0.075, 출력 $0.30)
        self.total_cost = (self.prompt_tokens / 1_000_000) * 0.075 + (self.completion_tokens / 1_000_000) * 0.30


@contextmanager
def get_gemini_callback(target_llm=None):
    """OpenAI의 get_openai_callback()과 동일한 방식으로 동작하는 Gemini용 컨텍스트 매니저"""
    if target_llm is None:
        target_llm = globals().get("llm")
    cb = GeminiCallbackHandler()
    if target_llm is not None:
        original_callbacks = list(target_llm.callbacks) if target_llm.callbacks else []
        target_llm.callbacks = original_callbacks + [cb]
        try:
            yield cb
        finally:
            target_llm.callbacks = original_callbacks
    else:
        yield cb


# Gemini 모델 초기화
llm = ChatGoogleGenerativeAI(model=model_name, temperature=0)

# get_gemini_callback() 컨텍스트 매니저로 실행
with get_gemini_callback(llm) as cb:
    response = llm.invoke("프랑스, 영국, 스페인의 수도는?")
    print("--- 모델 응답 ---")
    print(response.content)
    print("\n--- 토큰 사용량 및 비용 (Callback) ---")
    print(f"Total Tokens     : {cb.total_tokens}")
    print(f"Prompt Tokens    : {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost       : ${cb.total_cost:.6f}")

# LangChain 표준 usage_metadata 확인 (추가 확인용)
if hasattr(response, "usage_metadata") and response.usage_metadata:
    print("\n--- LangChain 표준 usage_metadata ---")
    print(response.usage_metadata)


# In[3]:





# In[3]:
