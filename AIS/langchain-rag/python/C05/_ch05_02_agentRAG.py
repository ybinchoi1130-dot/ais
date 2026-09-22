#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('pip', 'install --upgrade langchain==0.3.12 langchain_openai==0.2.12  #0.3.11')


# ## 기본 에이전트에서의 Tool Calling

# ### Set up the Tools

# In[ ]:


from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import StructuredTool


# In[ ]:


class MultiplierInput(BaseModel):
    a: int = Field(description="첫 번째 숫자")
    b: int = Field(description="두 번째 숫자")


def multiply(a: int, b: int) -> int:
    return a * b


multiplier = StructuredTool.from_function(
    func=multiply,
    name="Multiplier",
    description="두 숫자 곱셈",
    args_schema=MultiplierInput,
    return_direct=False,
)


# In[ ]:


class AdderInput(BaseModel):
    a: int = Field(description="첫 번째 숫자")
    b: int = Field(description="두 번째 숫자")


def add(a: int, b: int) -> int:
    return a + b


adder = StructuredTool.from_function(
    func=add,
    name="Adder",
    description="두 숫자 덧셈",
    args_schema=AdderInput,
    return_direct=False,
)


# In[ ]:


tools=[multiplier, adder]


# ### Set up the Agents

# In[ ]:


import getpass
import os

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
if "SERPER_API_KEY" not in os.environ:
    os.environ["SERPER_API_KEY"] = getpass.getpass("Enter your SERPER API key: ")
if "rapid_api_key" not in os.environ:
    os.environ["rapid_api_key"] = getpass.getpass("Enter your RAPID API key: ")


# In[ ]:


from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_tools_agent
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

model = ChatOpenAI(model="gpt-4o-mini", temperature=0, streaming=True)

system_template = """
당신은 수학 계산을 도와주는 AI 어시스턴트입니다.
사용 가능한 도구들:
- Adder: 두 숫자를 더합니다
- Multiplier: 두 숫자를 곱합니다

각 단계별로 계산 과정을 설명하고, 최종 결과를 명확하게 알려주세요.
"""

human_template = "{input}"

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_template),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        HumanMessagePromptTemplate.from_template(input_variables=["input"], template=human_template),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent = create_openai_tools_agent(model, tools, prompt)


# #### RUN Agents

# In[ ]:


from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

query = "13과 28을 더하고 40을 곱하면 어떤 결과가 나올까요?"
response = agent_executor.invoke({"input": query, "chat_history": [] })
result = response['output']


# In[ ]:


from langchain.agents import AgentExecutor

# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)


# In[ ]:


queries = [
    "13과 28을 더하고 40을 곱하면 어떤 결과가 나올까요?",
    "5와 7을 곱하고 3을 더하면?",
    "10에 20을 더하고 그 결과를 2로 나누면?"
]

for query in queries:
    print(f"\n질문: {query}")
    response = agent_executor.invoke(
            {
                "input": query,
                "chat_history": []
            }
        )
    result = response['output']
    print(f"답변: {result}")


# In[ ]:


query = "13과 28을 더하고 40을 곱하면 어떤 결과가 나올까요?"
response = agent_executor.invoke(
        {
            "input": query,
            "chat_history": []
        }
    )
result = response['output']
print(result)


# ## ReACT 활용한 고급 Tool Calling

# 도구 간 동적 조정

# In[ ]:


import requests
import json
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.tools import StructuredTool

# 1. 도구 클래스/함수 정의
class StockTool:
    def run(self, input_data):
        # 입력 데이터를 기반으로 주식 관련 작업 수행 함수 작성
        api_key = os.getenv("rapid_api_key")
        url = "https://seeking-alpha.p.rapidapi.com/symbols/get-ratings"

        querystring = {"symbols":input_data.lower()}

        headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        print(response)

        if response.status_code == 200:
            data = response.json()
            result = json.dumps(data)
        else:
            raise ValueError(f"{input_data}에 대한 데이터가 없습니다.")
        return f"주식데이터 입력: {input_data}\n{result}"

class SearchTool:
    def run(self, input_data):
        # 입력 데이터를 기반으로 검색 작업 수행 함수 작성
        url = "https://google.serper.dev/search"

        payload = json.dumps({
            "q": input_data
        })
        headers = {
            'X-API-KEY': os.getenv("SERPER_API_KEY"),
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text

# 2. 도구 객체 생성
stock_tool = StockTool()
search_tool = SearchTool()


# In[ ]:


def choose_tool_based_on_input(input_data):
    # 입력 데이터에 따라 사용할 도구를 동적으로 선택
    if "주식" in input_data:
        return stock_tool
    elif "검색" in input_data:
        return search_tool
    else:
        raise ValueError("입력에 적합한 도구를 찾을 수 없습니다.")

# 입력에 따라 적합한 도구 선택
def dynamic_tool_call(input_data):
    tool = choose_tool_based_on_input(input_data)
    return tool.run(input_data)

result = dynamic_tool_call("AI 연구 검색")
print(result)


# 캐싱을 통한 최적화

# In[ ]:


from functools import lru_cache

# 검색 결과를 캐싱하는 예시
@lru_cache(maxsize=10)
def cached_search(query):
    return search_tool.run(query)

# 캐싱된 검색 호출
result = cached_search("AI 연구 동향")
print(result)


# 오류 처리 및 재시도
# 

# In[ ]:


def robust_tool_call(tool, input_data, retries=3):
    for attempt in range(retries):
        try:
            result = tool.run(input_data)
            return result
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                raise
            print("재시도...")

# 도구 호출 예시
result = robust_tool_call(search_tool, "AI 도구의 발전")
print(result)


# 멀티 스텝 워크플로우와 분기 로직

# In[ ]:


def multi_step_workflow(input_data):
    # 첫 번째 단계: 웹 검색
    search_result = search_tool.run(input_data)

    # 두 번째 단계: 특정 조건을 만족하면 주식 가격 확인
    if "stock" in input_data:
        stock_price = stock_tool.run(input_data.split()[-1])
        return f"Search Result: {search_result}, Stock Price: {stock_price}"
    else:
        return f"Search Result: {search_result}"

# 워크플로우 실행 예시
result = multi_step_workflow("AAPL 주식 가격은 얼마입니까?")
print(result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




