#!/usr/bin/env python
# coding: utf-8

# # Langchain Basic

# ### module install

# In[1]:


# get_ipython().system(' pip install langchain_openai==0.2.6 langchain_community==0.3.5')
# pip install langchain_openai==0.2.6 langchain_community==0.3.5


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


# ## 1.5.3 메모리(Memory)

# In[3]:


# LangChain 및 필요한 라이브러리 임포트
try:
    from langchain.agents import initialize_agent, Tool, AgentType
except ImportError:
    from langchain_classic.agents import initialize_agent, Tool, AgentType
from langchain_openai import ChatOpenAI
try:
    from langchain.callbacks import get_openai_callback
except (ImportError, ModuleNotFoundError):
    from langchain_community.callbacks import get_openai_callback
try:
    from langchain.chains import LLMChain
except ImportError:
    from langchain_classic.chains import LLMChain
try:
    from langchain.prompts import PromptTemplate
except ImportError:
    from langchain_core.prompts import PromptTemplate

# LLM 모델 설정 (예: OpenAI GPT 모델)
llm = ChatOpenAI(model="gpt-4o-mini")

# 에이전트가 사용할 툴 설정
tools = [
    Tool(
        name="Echo",
        func=lambda x: f"Echoing: {x}",  # 간단한 툴로 입력한 값을 그대로 반환
        description="Echo the input text"
    )
]

# 에이전트 설정: Tool을 사용하여 질의를 처리할 수 있도록 설정
agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # 적절한 에이전트 타입 설정
    verbose=True  # 출력되는 내용이 많아짐
)

# 에이전트 실행 예시
query = "Hello, I am Bob."
print("Question:", query)

# 에이전트 실행
result = agent_executor.invoke({"input": query})

# 결과 출력
print("Answer:", result['output'])


# ### 메모리 없는 예제

# In[4]:


# 사용자 프로필 관리
query = "안녕 나는 김철수야."
print("질문:", query)
result = agent_executor.invoke({"input": query})
print("답변:", result['output'])

query = "내가 누구인지 기억나니?"
print("질문:", query)
result = agent_executor.invoke({"input": query})
print("답변:", result['output'])


# In[5]:


# 사용자 설정 정보와 관련 질문
query = "기본 설정 언어를 한국어로 업데이트합니다."
print("질문:", query)
result = agent_executor.invoke({"input": query})
print("답변:", result['output'])
print('---')
query = "내가 선호하는 언어는?"
print("질문:", query)
result = agent_executor.invoke({"input": query})
print("답변:", result['output'])


# ### 메모리클래스 정의

# In[7]:


# 메모리 클래스 정의
from pydantic import BaseModel, Field, validator
from langchain_core.tools import StructuredTool
from langchain_core.tools import ToolException

class UserProfileInput(BaseModel):
    name: str = Field(description="사용자 이름")
    language: str = Field(description="사용자 언어")

    @validator('name')
    def validate_name(cls, v):
        if not v or len(v) < 1:
            raise ToolException('Name cannot be empty')
        return v

    @validator('language')
    def validate_language(cls, v):
        if not v or len(v) < 1:
            raise ToolException('Language cannot be empty')
        return v


# In[8]:


# 도구 정의
def update_user_profile(name: str, language: str) -> str:
    """이름과 선호하는 언어로 사용자 프로필을 업데이트"""
    return f"프로필 업데이트 완료: name: {name}, language: {language}"

def get_user_profile() -> str:
    """사용자의 프로필 정보를 검색"""
    # In a real scenario, this would fetch data from a database or a file
    return "사용자 프로필 가져오기: name: Alex, language: 프랑스어"

update_profile_tool = StructuredTool.from_function(
    func=update_user_profile,
    args_schema=UserProfileInput,
    handle_tool_error=True,
)

get_profile_tool = StructuredTool.from_function(
    func=get_user_profile,
    # args_schema=UserProfileInput,
    handle_tool_error=True,
)


# In[9]:


# 메모리 기반 에이전트 설정
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
try:
    from langchain.agents import create_tool_calling_agent, AgentExecutor
except ImportError:
    from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a helpful assistant"),
    ("placeholder", "{history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

tools = [update_profile_tool, get_profile_tool]

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

store = {}  # 메시지 기록을 저장하는 더미 데이터베이스

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

agent_executor_w_memory = RunnableWithMessageHistory(
    agent_executor,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)


# ### 메모리 사용 사례

# In[10]:


# 사용자 프로필 관리
print("\n--- [메모리 있음] 세션 user123: 첫 번째 질문 ---")
res1 = agent_executor_w_memory.invoke(
    {"input": "안녕하세요, 저는 김철수입니다."},
    config={"configurable": {"session_id": "user123"}},
)
print("답변:", res1['output'])

print("\n--- [메모리 있음] 세션 user123: 두 번째 질문 ---")
res2 = agent_executor_w_memory.invoke(
    {"input": "내가 누구인지 기억나?"},
    config={"configurable": {"session_id": "user123"}},
)
print("답변:", res2['output'])


# In[11]:


# 사용자 설정 정보와 관련 질문
print("\n--- [메모리 있음] 세션 user123: 프로필 언어 업데이트 ---")
res3 = agent_executor_w_memory.invoke(
    {"input": "기본 설정 언어를 프랑스어로 업데이트합니다."},
    config={"configurable": {"session_id": "user123"}},
)
print("답변:", res3['output'])

print("\n--- [메모리 있음] 세션 user123: 선호 언어 확인 ---")
res4 = agent_executor_w_memory.invoke(
    {"input": "제가 선호하는 언어는 무엇인가요?"},
    config={"configurable": {"session_id": "user123"}},
)
print("답변:", res4['output'])


# In[ ]:




