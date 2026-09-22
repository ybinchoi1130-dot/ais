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

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model=model_name)

#%%

# Google Gemini의 응답 메시지 구조
# type: 멀티모달(텍스트, 이미지, 함수, ...)
"""
output = [
    { "type" : "text", "text": "안녕하세요!"},
    { "type" : "text", "text": "저는 유능한 어시스턴트입니다."}
]
"""

#%%

# 위의 Google Gemini의 output에서 
# 'text'에 해당하는 응답 메시지를 꺼내서 문자열로 변환하고
# 추출한 각 조각들을 문자열 join() 메서드를 이용해서 하나로 결합

def format_output(output):
    """Gemini 모델의 리스트형 응답을 일반 문자열로 변환"""
    if isinstance(output, list):
        return "".join(part.get("text", "") \
                       if isinstance(part, dict) else str(part) \
                           for part in output)
    return str(output)


#%%
# ## 1.5.3 메모리(Memory)

# In[3]:


# LangChain 및 필요한 라이브러리 임포트
from langchain_core.tools import Tool
from langchain_core.prompts import ChatPromptTemplate
try:
    from langchain.agents import create_tool_calling_agent, AgentExecutor
except ImportError:
    from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

# 에이전트가 사용할 툴 설정
tools = [
    Tool(
        name="Echo",
        func=lambda x: f"Echoing: {x}",  # 간단한 툴로 입력한 값을 그대로 반환
        description="Echo the input text"
    )
]

# 메모리가 없는 기본 에이전트 프롬프트 설정
prompt_without_memory = ChatPromptTemplate.from_messages([
    ("system", "너는 유용한 어시스턴트야."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 에이전트 설정: create_tool_calling_agent 사용 (LangChain 0.2+ / 1.0+ 표준)
agent = create_tool_calling_agent(llm, tools, prompt_without_memory)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 에이전트 실행 예시
query = "Hello, I am Bob."
print("Question:", query)

# 에이전트 실행
result = agent_executor.invoke({"input": query})

# 결과 출력
print("Answer:", format_output(result['output']))


# ### 메모리 없는 예제

# In[4]:


# 사용자 프로필 관리
query = "안녕 나는 김철수야."
print("\n질문:", query)
result = agent_executor.invoke({"input": query})
print("답변:", format_output(result['output']))

query = "내가 누구인지 기억나니?"
print("\n질문:", query)
result = agent_executor.invoke({"input": query})
print("답변:", format_output(result['output']))


# In[5]:


# 사용자 설정 정보와 관련 질문
query = "기본 설정 언어를 한국어로 업데이트합니다."
print("\n질문:", query)
result = agent_executor.invoke({"input": query})
print("답변:", format_output(result['output']))
print('---')
query = "내가 선호하는 언어는?"
print("\n질문:", query)
result = agent_executor.invoke({"input": query})
print("답변:", format_output(result['output']))


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
from langchain_core.messages import AIMessage, BaseMessage
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

class GeminiChatMessageHistory(ChatMessageHistory):
    """Google Gemini의 리스트형 출력을 BaseMessage 형식으로 안전하게 변환하여 저장"""
    def add_message(self, message: BaseMessage) -> None:
        if isinstance(message, dict):
            content = message.get("text") or message.get("content", "")
            message = AIMessage(content=content)
        elif isinstance(message, list):
            content = "".join(p.get("text", "") if isinstance(p, dict) else str(p) for p in message)
            message = AIMessage(content=content)
        super().add_message(message)

store = {}  # 메시지 기록을 저장하는 더미 데이터베이스

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = GeminiChatMessageHistory()
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
print("답변:", format_output(res1['output']))

print("\n--- [메모리 있음] 세션 user123: 두 번째 질문 ---")
res2 = agent_executor_w_memory.invoke(
    {"input": "내가 누구인지 기억나?"},
    config={"configurable": {"session_id": "user123"}},
)
print("답변:", format_output(res2['output']))


# In[11]:


# 사용자 설정 정보와 관련 질문
print("\n--- [메모리 있음] 세션 user123: 프로필 언어 업데이트 ---")
res3 = agent_executor_w_memory.invoke(
    {"input": "기본 설정 언어를 프랑스어로 업데이트합니다."},
    config={"configurable": {"session_id": "user123"}},
)
print("답변:", format_output(res3['output']))

print("\n--- [메모리 있음] 세션 user123: 선호 언어 확인 ---")
res4 = agent_executor_w_memory.invoke(
    {"input": "제가 선호하는 언어는 무엇인가요?"},
    config={"configurable": {"session_id": "user123"}},
)
print("답변:", format_output(res4['output']))

