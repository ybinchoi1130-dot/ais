#!/usr/bin/env python
# coding: utf-8

# # Langchain Basic

# ### module install

# In[1]:


# get_ipython().system(' pip install langchain_openai==0.2.6 langchain_community==0.3.5')


# In[2]:


import getpass
import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")


# ## 1.5.5 콜백 및 평가

# ### 콜백

# In[3]:


from langchain_openai import ChatOpenAI
try:
    from langchain_community.callbacks import get_openai_callback
except ImportError:
    from langchain.callbacks import get_openai_callback

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

with get_openai_callback() as cb:
    response = llm.invoke("프랑스, 영국, 스페인의 수도는?")
    print("--- 모델 응답 ---")
    print(response.content)
    print("\n--- 토큰 사용량 및 비용 (Callback) ---")
    print(f"Total Tokens     : {cb.total_tokens}")
    print(f"Prompt Tokens    : {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost       : ${cb.total_cost:.6f}")


# In[3]:





# In[3]:
