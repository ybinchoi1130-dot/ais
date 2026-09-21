#!/usr/bin/env python
# coding: utf-8

# 발화주체: 역할("ai", "human", "system")
# "system": 역할, 규칙, 제약 사항을 지시하는 시스템 프롬프트
# "human: 사용자(사람)가 모델에 입력하는 질문이나 프롬프트
# "ai": AI 모델이 이전에 생성했던 응답, 대화이력

# # Langchain Basic

# ### module install

# In[ ]:


# get_ipython().system(' pip install langchain_openai==0.2.6')
# get_ipython().system(' pip install langchain_community==0.3.5')


# In[ ]:


import getpass
import os

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")


# ## 1.5.1 체인(Chain)

# ### 기본 체인 연결

# In[ ]:


from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")
llm.invoke("피타고라스 정리의 공식은 무엇인가요?")


# In[ ]:


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 프롬프트 + 모델 + output parser
prompt = ChatPromptTemplate.from_template("초등학생이 이해할 수 있는 방식으로 답을 설명하세요.: <질문>: {query}")

print(prompt)


# In[ ]:


llm = ChatOpenAI(model="gpt-4o-mini")

chain = prompt | llm

chain.invoke({"query": "피타고라스 정리의 공식은 무엇인가요?"})


# In[ ]:


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# prompt + model + output parser
prompt = ChatPromptTemplate.from_template("초등학생이 이해할 수 있는 방식으로 답을 설명하세요.: <질문>: {query}")
llm = ChatOpenAI(model="gpt-4o-mini")

# chain에 이어서 output_parser 추가
output_parser = StrOutputParser()

# LCEL chaining
chain = prompt | llm | output_parser

# chain 호출
chain.invoke({"query": "피타고라스 정리의 공식은 무엇인가요?"})


# ### 멀티 체인 연결

# In[ ]:


from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableMap
from operator import itemgetter

# 논쟁거리 생성
basictopic = (
    ChatPromptTemplate.from_template("{topic} 에 대한 논쟁을 한국어로 생성합니다.")
    | ChatOpenAI()
    | StrOutputParser()
    | {"base": RunnablePassthrough()}
)

# 긍정 의견
positive = (
    ChatPromptTemplate.from_template(
        "{base} 의 장점 또는 긍정적인 측면을 나열하세요."
    )
    | ChatOpenAI()
    | StrOutputParser()
)

# 부정 의견
negative = (
    ChatPromptTemplate.from_template(
        "{base} 의 단점 또는 부정적인 측면을 나열하세요."
    )
    | ChatOpenAI()
    | StrOutputParser()
)

# 최종 답변
# 발화주체: 역할("ai", "human", "system")
# "system": 역할, 규칙, 제약 사항을 지시하는 시스템 프롬프트
# "human: 사용자(사람)가 모델에 입력하는 질문이나 프롬프트
# "ai": AI 모델이 이전에 생성했던 응답, 대화이력
final = (
    ChatPromptTemplate.from_messages(
        [
            ("ai", "{original_response}"),
            ("human", "긍정:\n{results_1}\n\n부정:\n{results_2}"),
            ("system", "비평에 대한 최종 답변 생성"),
        ]
    )
    | ChatOpenAI()
    | StrOutputParser()
)

# RunnableParallel을 사용하여 긍정,부정 의견을 병렬로 처리
chain = (
    basictopic
    | RunnableParallel(
        results_1 = positive,
        results_2 = negative,
        original_response = itemgetter("base"),
    )
    | RunnableMap(
        {
            "positive_result": itemgetter("results_1"),
            "negative_result": itemgetter("results_2"),
            "final_answer": itemgetter("original_response"),
        }
    )
)

# chain 실행
result = chain.invoke({"topic": "social media"})

positive_result = result['positive_result']
negative_result = result['negative_result']
final_answer = result['final_answer']

print("소셜미디어에 대한 긍정 의견:\n", positive_result)
print("\n소셜미디어에 대한 부정 의견:\n", negative_result)
print("\n최종 의견",final_answer)


# In[ ]:




