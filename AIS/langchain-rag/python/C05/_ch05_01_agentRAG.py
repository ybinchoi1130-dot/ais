#!/usr/bin/env python
# coding: utf-8

# ### Module Install

# In[ ]:


get_ipython().run_line_magic('pip', 'install --upgrade langchain==0.3.12 langchain_openai==0.2.12 langchain_community==0.3.12')


# In[ ]:


# 랭체인에서 필요한 도구 및 에이전트 초기화
from langchain.agents import initialize_agent, Tool
from langchain_openai import OpenAI

import getpass
import os

# 환경 변수 설정 (API 키 설정 등)
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
if "SERPER_API_KEY" not in os.environ:
    os.environ['SERPER_API_KEY'] = getpass.getpass("Enter your SERPER API key: ")


# ### Code

# In[ ]:


import requests
import os
import json

def search_query(query):
    url = "https://google.serper.dev/search"

    payload = json.dumps({
        "q": query
    })
    headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

result = search_query("LLM RAG Agent") # 원하는 쿼리를 입력
print(result)


# In[ ]:


from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_openai import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

llm = OpenAI(temperature=0)
search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="검색 결과와 함께 유용한 답변을 제공합니다."
    )
]

search = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,max_iterations=4, early_stopping_method="generate", handle_parsing_errors=True)
search.run("발롱도르 2024년도 수상자의 고향은 어디인가요?")


# In[ ]:


# tool description 보강
tools = [
        Tool(
            name="Intermediate Answer",
            func=search.run,
            description="도구를 사용하여 현재 금융 데이터, 주식 정보 및 기업 지표에 대한 사실적인 답변을 찾아 답변하세요."
        )
    ]

# 에이전트 내 파라미터 조정 (handle_parsing_errors, max_iterations)
agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.SELF_ASK_WITH_SEARCH,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=3
    )


# In[ ]:


agent.run("코카콜라의 가장 최근 배당금 지급액은 얼마였나요?")


# In[ ]:


prompt_template = """다음 형식을 사용하세요:

Question: 답변해야 할 입력 질문
Thought: 무엇을 해야 할지 항상 생각하세요
Action: 취해야 할 행동, 항상 "Intermediate Answer"여야 합니다
Action Input: 행동에 대한 입력
Observation: 행동의 결과
... (이 Thought/Action/Action Input/Observation은 N번 반복될 수 있습니다)
Thought: 이제 최종 답변을 알았습니다
Final Answer: 원래 입력된 질문에 대한 최종 답변

Question: {input}
{agent_scratchpad}
"""


# In[ ]:


from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_openai import OpenAI
from langchain_community.utilities import GoogleSerperAPIWrapper

# 에이전트 세팅 함수
def setup_self_ask_agent():
    """
    셀프 질문 에이전트 설정 및 반환
    """
    llm = OpenAI(temperature=0)
    search = GoogleSerperAPIWrapper()
    tools = [
        Tool(
            name="Intermediate Answer",
            func=search.run,
            description="도구를 사용하여 현재 금융 데이터, 주식 정보 및 기업 지표에 대한 사실적인 답변을 찾아 한국어로 답변하세요."
        )
    ]

    # 에이전트 내 파라미터 조정 (handle_parsing_errors, max_iterations)
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.SELF_ASK_WITH_SEARCH,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5
    )

    return agent


# In[ ]:


# 금융 관련 질문에 대해 정보를 가져오는 함수
def get_financial_info(query: str) -> str:
    agent = setup_self_ask_agent()

    # 구조화된 응답을 유도하기 위해 쿼리 형식 지정
    formatted_query = f""" 다음 정보를 찾습니다:
    {query}
    답변의 형식은 다음과 같이 한국어로 답변하세요:
    '[metric] [value]' 다음에 가능한 경우 출처의 날짜를 입력합니다."""

    try:
        response = agent.run(formatted_query)
        return response
    except Exception as e:
        # 가능한 경우 오류에서 유용한 정보를 추출
        if "Intermediate answer:" in str(e):
            try:
                # 오류 메시지에서 실제 답변 추출
                relevant_info = str(e).split("Intermediate answer:")[-1].split("Follow up:")[0].strip()
                return f"Found information: {relevant_info}"

            except:
                pass
        return f"Error occurred: {str(e)}"


# In[ ]:


get_financial_info('코카콜라의 가장 최근 배당금 지급액은 얼마였나요?')


# In[ ]:


from langchain.agents import load_tools
tools = load_tools(["google-serper"])


# In[ ]:




