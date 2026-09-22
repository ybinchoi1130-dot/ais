#!/usr/bin/env python
# coding: utf-8

# # Langchain Basic (Google Gemini)

# ### module install

# In[2]:


# get_ipython().system(' pip install -q -U langchain-google-genai')
# pip install -q -U langchain-google-genai


# In[3]:


import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    if "GEMINI_API_KEY" in os.environ:
        os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]
    else:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")

# model_name = "gemini-1.5-flash"
model_name = "gemini-3.1-flash-lite"

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model=model_name)


# ## 1.5.2 프롬프트(Prompt)

# ### PromptTemplate 기본 사용법

# In[4]:


from langchain_core.prompts import PromptTemplate

# 유머 템플릿 만들기
prompt_template = PromptTemplate.from_template(
    "{content}에 대한 {adjective} 농담을 들려주세요."
)

# 템플릿에 값 채우기
formatted_prompt = prompt_template.format(adjective="재미있는", content="닭")
print("--- 포맷된 프롬프트 ---")
print(formatted_prompt)  # '닭에 대한 재미있는 농담을 들려주세요.'

# Gemini 모델 실행
chain = prompt_template | llm
response = chain.invoke({"adjective": "재미있는", "content": "닭"})
print("\n--- Gemini 응답 ---")
print(response.content)


# ### 채팅프롬프트

# In[5]:


from langchain_core.prompts import ChatPromptTemplate

# 대화형 템플릿 만들기
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "너는 유능한 어시스턴트야. 너의 이름은 {name}이야."),
        ("human", "안녕하세요?"),
        ("ai", "안녕하세요 무엇을 도와드릴까요?"),
        ("human", "{user_input}"),
    ]
)

# 템플릿에 값 채우기
messages = chat_template.format_messages(name="김철수", user_input="너의 이름은 뭐야?")
print("--- 포맷된 메시지 목록 ---")
print(messages)

# Gemini 모델 실행
chain = chat_template | llm
response = chain.invoke({"name": "김철수", "user_input": "너의 이름은 뭐야?"})
print("\n--- Gemini 응답 ---")
print(response.content)


# ### 프롬프트 조합 및 변수 사용

# In[7]:


from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import HumanMessage, AIMessage

# 대화 요약 템플릿 만들기
human_prompt = "지금까지의 대화를 {word_count} 단어로 요약합니다."
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)

# 대화 내용과 함께 요약 요청
chat_prompt = ChatPromptTemplate.from_messages(
    [MessagesPlaceholder(variable_name="conversation"), human_message_template]
)

# 대화 내용과 단어 수를 넣어서 요약 프롬프트 생성
conversation = [
    HumanMessage(content="프로그래밍을 배우는 가장 좋은 방법은 무엇인가요?"),
    AIMessage(content="변수 및 루프와 같은 기본 사항부터 시작하세요."),
]
formatted_prompt = chat_prompt.format_prompt(conversation=conversation, word_count="10")
print("--- 포맷된 메시지 ---")
print(formatted_prompt.to_messages())

# Gemini 모델 실행
chain = chat_prompt | llm
response = chain.invoke({"conversation": conversation, "word_count": "10"})
print("\n--- Gemini 응답 ---")
print(response.content)




