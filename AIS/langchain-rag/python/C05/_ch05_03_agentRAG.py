#!/usr/bin/env python
# coding: utf-8

# ### Module Install

# In[19]:


get_ipython().run_line_magic('pip', 'install --upgrade langchain==0.3.12 langchain_openai==0.2.12  # 0.3.10')


# 필요 API 키 입력

# In[20]:


import getpass
import os

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
if "SERPER_API_KEY" not in os.environ:
    os.environ["SERPER_API_KEY"] = getpass.getpass("Enter your SERPER API key: ")
if "rapid_api_key" not in os.environ:
    os.environ["rapid_api_key"] = getpass.getpass("Enter your RAPID API key: ")
if "rapid_api_key_price" not in os.environ:
    os.environ["rapid_api_key_price"] = getpass.getpass("Enter your RAPID STOCK PRICE API key: ")


# # 도구 데코레이터 + Pydantic
# 
# 대부분의 경우 입력값의 유효성을 검사하기 위해 Pydantic이 필요합니다. 예를 들어, 시세의 경우 형식은 일반적으로 AAPL, META, GOGL 등과 같이 최대 4자로 구성됩니다. 따라서 사용자 입력이 올바른 형식인지 논리적으로 검증할 수 있습니다. 그렇지 않은 경우 오류를 발생시켜 더 이상 처리하지 않을 수 있습니다. 이러한 접근 방식은 비용과 실행 시간 측면에서 시스템의 효율성을 향상시킵니다.

# In[21]:


import requests
import json
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic.v1 import BaseModel, Field, validator
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from datetime import datetime

# add pydantic
class SearchInput(BaseModel):
    stock: str = Field(description="Stock ticker to search for")

    @validator('stock')
    def validate_stock(cls, v):
        if not v.isalpha() or len(v) > 4:
            raise ValueError('Stock ticker should only contain up to 4 alphabetic characters')
        return v

# add args_schema=SearchInput inside of the tool decorator
@tool(args_schema=SearchInput)
def get_company_profile(stock:str) -> str:
    # 회사명, 섹터명, 기본 이름, 주식의 직원 수와 같은 세부 프로필 가져오기
    """
    Get the company profile and ratings for a given stock ticker.

    Args:
        stock (str): The stock ticker symbol to search for.

    Returns:
        str: The company profile data in JSON format.
    """
    api_key = os.getenv("rapid_api_key")
    url = "https://seeking-alpha.p.rapidapi.com/symbols/get-ratings"


    querystring = {"symbol":stock.lower()}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        result = json.dumps(data)
    else:
        raise ValueError(f"No data for {stock}")

    return result

@tool(args_schema=SearchInput)
def get_competitors(stock:str) -> str:
    """Get peers or competitors of a stock"""

    api_key = os.getenv("rapid_api_key")
    url = "https://seeking-alpha.p.rapidapi.com/symbols/get-peers"

    querystring = {"symbol":stock.lower()}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        result = json.dumps(data)
    else:
        raise ValueError(f"No data for {stock}")

    return result

prompt = ChatPromptTemplate.from_messages([
    ("system", "you're a helpful assistant"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

tools = [get_company_profile, get_competitors]
llm = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature = 0)
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose = True)


# In[22]:


get_company_profile('aapl')


# 다만 정확히 입력하지 않을 경우 아래와 같이 에러 발생

# In[23]:


query = "I'm an investor, what is AAPLLLLLLL"
print("Question:", query)
result = agent_executor.invoke({"input": query})
print("Answer:",result['output'])


# # Structured Tools
# https://blog.langchain.dev/structured-tools/

# ValueError가 발생하면 시스템이 중단되어 중간에 오류가 발생하면서 프로세스가 중단됩니다. 예를 들어 챗봇의 경우 아무런 설명도 제공하지 않고 갑자기 멈출 수 있습니다. 따라서 우리는 **에러 처리**가 필요합니다. Langchain은 이미 ToolException을 제공하고 있지만, 구조화된 도구나 기본 클래스를 통해서만 접근할 수 있습니다. 도구 데코레이터를 사용하여 ToolException을 구현할 수 없으므로 @tool이 항상 충분하지 않은 이유를 설명합니다. 유연성을 높이려면 StructuredTools를 사용해야 합니다.
# 
# 1. ValueError를 ToolException으로 변경합니다.
# 2. handle_tool_error = True로 변경합니다.

# In[24]:


from pydantic.v1 import BaseModel, Field, validator
from datetime import datetime
from langchain_core.tools import StructuredTool
from langchain_core.tools import ToolException

# change ValueError to ToolException
class SearchInput(BaseModel):
    stock: str = Field(description="Stock ticker to search for")

    @validator('stock')
    def validate_stock(cls, v):
        if not v.isalpha() or len(v) > 4:
            raise ToolException('Stock ticker should only contain up to 4 alphabetic characters')
        return v

def get_company_profile(stock:str) -> str:
    """Get detail profile such as company name, sector name, primary name, number of employees of a stock"""

    api_key = os.getenv("rapid_api_key")
    url = "https://seeking-alpha.p.rapidapi.com/symbols/get-profile"

    querystring = {"symbols":stock.lower()}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        result = json.dumps(data)
    else:
        raise ToolException(f"No data for {stock}")

    return result

def get_competitors(stock:str) -> str:
    """Get peers or competitors of a stock"""

    api_key = os.getenv("rapid_api_key")
    url = "https://seeking-alpha.p.rapidapi.com/symbols/get-peers"

    querystring = {"symbol":stock.lower()}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        result = json.dumps(data)
    else:
        raise ToolException(f"No data for {stock}")

    return result


get_company_profile_tool = StructuredTool.from_function(
    func=get_company_profile,
    args_schema= SearchInput,
    handle_tool_error=True, # add this
)

get_competitors_tool = StructuredTool.from_function(
    func=get_competitors,
    args_schema= SearchInput,
    handle_tool_error=True, # add this
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "you're a helpful assistant"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

tools = [get_company_profile_tool, get_competitors_tool]

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose = True)


# In[25]:


query = "I'm an investor, what is AAPL"
print("Question:", query)
result = agent_executor.invoke({"input": query})
print("Answer:",result['output'])


# * 실시간의 데이터를 가져오기 때문에 장이 운영하지 않는 시간/기간에는 값이 없을 수 있습니다.

# In[26]:


import requests

url = "https://seeking-alpha.p.rapidapi.com/v2/auto-complete"

querystring = {"query":"apple","type":"people,symbols,pages","size":"5"}

headers = {
	"x-rapidapi-key": "58c32f5dd8mshc7da181b67a6bcep110a60jsnbea62f8b288b",
	"x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())


# In[27]:


import requests

def get_stock_symbol(query: str) -> str:
    url = "https://seeking-alpha.p.rapidapi.com/v2/auto-complete"
    querystring = {"query":query,"type":"people,symbols,pages","size":"5"}
    # 기업명 기반으로 주식 정보를 가져오기 위한 함수
    headers = {
        "x-rapidapi-key": os.getenv("rapid_api_key_price"),
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        print(data)
        # 첫 번째 결과의 심볼 반환
        if "symbols" in data and len(data["symbols"]) > 0:
            symbol = data['symbols'][0]['name']
            s_id = data['symbols'][0]['id']
            return symbol, s_id
        else:
            return None
    else:
        print(response)
        raise Exception(f"Failed to fetch stock symbol: {response.status_code}")

symbol = get_stock_symbol("Apple")
print(symbol)


# In[28]:


def get_realtime_stock_price(symbol: str) -> dict:
    url = "https://seeking-alpha.p.rapidapi.com/market/get-realtime-quotes"
    querystring = {"sa_ids": symbol}
    '''회사의 최신 주가 확인하기'''
    headers = {
        "x-rapidapi-key": os.getenv("rapid_api_key_price"),
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        return data.get("real_time_quotes", {})
    else:
        raise Exception(f"실시간 데이터 가져오기에 실패했습니다: {response.status_code}")

price_data = get_realtime_stock_price('146')
print(price_data)


# In[29]:


def fetch_stock_price(query: str) -> str:
    try:
        # 1: 주식 심볼 추출
        symbol,s_id = get_stock_symbol(query)
        print(symbol,s_id)
        if not symbol:
            return f"'{query}'에 대한 심볼을 찾을 수 없습니다."

        # 2: 실시간 주식 가격 추출
        stock_data = get_realtime_stock_price(s_id)
        if not stock_data:
            return f"실시간 데이터를 사용할 수 없습니다: '{symbol}'."

        # 관련 값 추출
        price = stock_data[0].get("last", "N/A")
        return f"{symbol}의 현재 가격은 ${price}입니다."
    except Exception as e:
        return str(e)


# In[30]:


print(fetch_stock_price("Apple"))  # "The current price of AAPL is $123.45."


# In[31]:


def monitor_stock_price(stock: str, threshold: float):
    price_info = fetch_stock_price(stock)
    current_price = float(price_info.split('$')[-1].split('.')[0])

    if current_price >= threshold:
        print(f"{stock} 주가가 ${threshold} 이상입니다. 현재 주가: ${current_price}. 매도 고려하세요.")
    else:
        print(f"{stock} 주가가 ${threshold} 이하입니다. 현재 주가: ${current_price}. 매수 고려하세요.")

# Example Usage
monitor_stock_price("AAPL", 200.00)


# In[32]:


query = "AAPL 관련 뉴스를 분석하고, 주가 변동성을 알려줘."
result = agent_executor.invoke({"input": query})
print("Answer:", result['output'])


# ## 투자전략 수립

# In[33]:


if "NEWS_API_KEY" not in os.environ:
    os.environ["NEWS_API_KEY"] = getpass.getpass("Enter your NEWS_API_KEY: ")


# In[34]:


import json
from typing import Dict, Any
from datetime import timedelta

def get_news_sentiment(topic: str) -> Dict[str, Any]:
    """특정 주제에 대한 뉴스 기사의 감성을 분석합니다."""

    # NewsAPI 설정
    NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    news_api_url = "https://newsapi.org/v2/everything"

    # 날짜 범위 설정
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    querystring = {
        "q": topic,
        "from": start_date.strftime("%Y-%m-%d"),
        "to": end_date.strftime("%Y-%m-%d"),
        "language": "ko",
        "sortBy": "relevancy",
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(news_api_url, params=querystring)
        articles = response.json().get('articles', [])

        if not articles:
            return {
                "topic": topic,
                "average_sentiment": 0,
                "analyzed_articles": 0,
                "sentiment_summary": "데이터 없음"
            }

        # 감성 분석을 위한 OpenAI 설정
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0,
        )

        # 각 기사에 대한 감성 분석
        sentiment_scores = []
        print(articles[:10])
        for article in articles[:10]:  # 최근 10개 기사만 분석
            if article['description'] != '[Removed]':
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "뉴스 기사의 감성을 분석하여 아래와 같은 JSON 형태로 응답하세요. "
                "결과는 'score'는 -1(매우 부정적)에서 1(매우 긍정적) 사이의 값이고, "
                "'explanation'은 해당 감성 점수에 대한 설명을 포함합니다."),
                    ("user", f"제목: {article['title']}\n내용: {article['description']}")
                ])

                chain = prompt | llm
                result = chain.invoke({})
                try:
                    response_json = json.loads(result.content)
                    score = float(response_json['score'])
                    if score != 0:
                        print(response_json)
                    sentiment_scores.append(score)
                except (json.JSONDecodeError, KeyError, ValueError) as e:
                    print(f"파싱 에러 결과: {e}")
                    continue

        # 종합 감성 점수 계산
        if sentiment_scores:
            avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
            return {
                "topic": topic,
                "average_sentiment": round(avg_sentiment, 2),
                "analyzed_articles": len(sentiment_scores),
                "sentiment_summary": "긍정적" if avg_sentiment > 0.3 else "부정적" if avg_sentiment < -0.3 else "중립적"
            }
        else:
            return {
                "topic": topic,
                "average_sentiment": 0,
                "analyzed_articles": 0,
                "sentiment_summary": "분석 불가"
            }

    except Exception as e:
        print('❌',e)
        return {
            "topic": topic,
            "average_sentiment": 0,
            "analyzed_articles": 0,
            "sentiment_summary": f"에러 발생: {str(e)}"
        }

get_news_sentiment('삼성전자')


# In[35]:


from typing import List, Dict, Any
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
import requests
import json
from datetime import datetime, timedelta

# 뉴스 감성분석 도구
@tool
def get_news_sentiment(topic: str) -> Dict[str, Any]:
    """특정 주제에 대한 뉴스 기사의 감성을 분석합니다."""

    # NewsAPI 설정
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    news_api_url = "https://newsapi.org/v2/everything"

    # 날짜 범위 설정
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    querystring = {
        "q": topic,
        "from": start_date.strftime("%Y-%m-%d"),
        "to": end_date.strftime("%Y-%m-%d"),
        "language": "ko",
        "sortBy": "relevancy",
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(news_api_url, params=querystring)
        articles = response.json().get('articles', [])

        if not articles:
            return {
                "topic": topic,
                "average_sentiment": 0,
                "analyzed_articles": 0,
                "sentiment_summary": "데이터 없음"
            }

        # 감성 분석을 위한 OpenAI 설정
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0,
        )

        # 각 기사에 대한 감성 분석
        sentiment_scores = []
        print(articles[:10])
        for article in articles[:10]:  # 최근 10개 기사만 분석
            if article['description'] != '[Removed]':
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "뉴스 기사의 감성을 분석하여 아래와 같은 JSON 형태로 응답하세요. "
                "결과는 'score'는 -1(매우 부정적)에서 1(매우 긍정적) 사이의 값이고, "
                "'explanation'은 해당 감성 점수에 대한 설명을 포함합니다."),
                    ("user", f"제목: {article['title']}\n내용: {article['description']}")
                ])

                chain = prompt | llm
                result = chain.invoke({})
                try:
                    response_json = json.loads(result.content)
                    score = float(response_json['score'])
                    if score != 0:
                        print(response_json)
                    sentiment_scores.append(score)
                except (json.JSONDecodeError, KeyError, ValueError) as e:
                    print(f"Error parsing result: {e}")
                    continue


        # 종합 감성 점수 계산
        if sentiment_scores:
            avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
            return {
                "topic": topic,
                "average_sentiment": round(avg_sentiment, 2),
                "analyzed_articles": len(sentiment_scores),
                "sentiment_summary": "긍정적" if avg_sentiment > 0.3 else "부정적" if avg_sentiment < -0.3 else "중립적"
            }
        else:
            return {
                "topic": topic,
                "average_sentiment": 0,
                "analyzed_articles": 0,
                "sentiment_summary": "분석 불가"
            }

    except Exception as e:
        return {
            "topic": topic,
            "average_sentiment": 0,
            "analyzed_articles": 0,
            "sentiment_summary": f"에러 발생: {str(e)}"
        }

# 산업군 분석 도구
@tool
def analyze_industry_news(industry: str) -> Dict[str, Any]:
    """특정 산업군에 대한 뉴스를 분석합니다."""
    return get_news_sentiment(f"{industry} industry")

# 경제 지표 분석 도구
@tool
def analyze_economic_indicators(indicators: Dict[str, Any] = None) -> Dict[str, Any]:
    """주요 경제 지표 관련 뉴스를 분석합니다."""
    default_indicators = ["금리", "통화정책", "인플레이션", "GDP"]
    if indicators is None:
        indicators ={"list": default_indicators}
    economic_indicators = indicators.get('list', default_indicators)

    results = {}
    for indicator in economic_indicators:
        results[indicator] = get_news_sentiment(indicator)
    return results

# 투자 결정 도구
@tool
def make_investment_decision(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """
    종합적인 분석을 바탕으로 투자 결정을 제안합니다.
    """

    # 입력 값 추출
    company = inputs.get("company", "Unknown")
    company_sentiment = inputs.get("company_sentiment", {"average_sentiment": 0})
    industry_sentiment = inputs.get("industry_sentiment", {"average_sentiment": 0})
    economic_indicators = inputs.get("economic_indicators", {})

    # 가중치 설정
    weights = {
        "company": 0.4,
        "industry": 0.3,
        "economic": 0.3
    }

    # 회사 점수 계산
    company_score = company_sentiment.get("average_sentiment", 0) * weights["company"]

    # 산업 점수 계산
    industry_score = industry_sentiment.get("average_sentiment", 0) * weights["industry"]

    # 경제 지표 점수 계산
    economic_scores = [
        indicator.get("average_sentiment", 0)
        for indicator in economic_indicators.values()
    ]
    economic_score = (sum(economic_scores) / len(economic_scores)) * weights["economic"] if economic_scores else 0

    # 총점 계산
    total_score = company_score + industry_score + economic_score

    # 투자 결정
    decision = {
        "company": company,
        "timestamp": datetime.now().isoformat(),
        "total_score": round(total_score, 2),
        "recommendation": "매수" if total_score > 0.3 else "매도" if total_score < -0.3 else "관망",
        "confidence": abs(total_score),
        "factors": {
            "company_sentiment": company_sentiment,
            "industry_sentiment": industry_sentiment,
            "economic_indicators": economic_indicators
        }
    }

    return decision

class InvestmentAnalyzer:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0
        )

        self.tools = [
            get_news_sentiment,
            analyze_industry_news,
            analyze_economic_indicators,
            make_investment_decision
        ]

        prompt = ChatPromptTemplate.from_messages([
            ("system", """주식 시장 분석 및 투자 결정을 돕는 AI 에이전트입니다.
            뉴스 데이터를 수집하고 감성 분석을 통해 투자 결정을 제안합니다."""),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])

        self.agent = create_openai_functions_agent(self.llm, self.tools, prompt)
        self.executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)

    def analyze(self, company: str, industry: str) -> Dict[str, Any]:
        """투자 분석을 수행하고 결과를 반환합니다."""
        try:
            # 1. 회사 감성 분석
            company_result = get_news_sentiment(company)

            # 2. 산업군 감성 분석
            industry_result = analyze_industry_news(industry)

            # 3. 경제 지표 분석
            economic_result = analyze_economic_indicators({"list": ["금리"]})

            # 4. 투자 결정
            decision = make_investment_decision({"inputs":{
                    "company": company,
                    "company_sentiment": company_result,
                    "industry_sentiment": industry_result,
                    "economic_indicators": economic_result
                }
            })
            # decision = self.executor.invoke({
            #     "tool": "make_investment_decision",
            #     "input": {
            #         "company": company,
            #         "company_sentiment": company_result,
            #         "industry_sentiment": industry_result,
            #         "economic_indicators": economic_result
            #     }
            # })

            return decision

        except Exception as e:
            print(f"분석 중 오류 발생: {str(e)}")
            return {
                "error": str(e),
                "status": "failed"
            }

if __name__ == "__main__":
    analyzer = InvestmentAnalyzer()

    # 삼성전자 분석 예시
    result = analyzer.analyze(
        company="삼성전자",
        industry="반도체"
    )

    print("\n최종 투자 분석 결과:")
    print(json.dumps(result, indent=2, ensure_ascii=False))


# 단순 금리에 대한 뉴스만 불러올 경우 아래 코드 활용 가능

# In[45]:


from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, initialize_agent, Tool
import requests
import json

@tool()
def get_news_sentiment(topic:str) -> str:
    """주제와 관련된 뉴스 기사의 감성어를 가져와 분석"""
    news_api_url = "https://newsapi.org/v2/everything"
    querystring = {"q": topic, "apiKey": os.getenv('NEWS_API_KEY')}

    response = requests.get(news_api_url, params=querystring)
    articles = response.json().get('articles', [])
    print(articles)

    # 간단한 감정 분석 예시
    sentiment_score = sum(1 if "positive" in article['description'].lower() else -1 for article in articles)
    return f"Sentiment score for {topic}: {sentiment_score}"

tools = [get_news_sentiment]

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    ("system", """주식 시장 분석 및 투자 결정을 돕는 AI 에이전트입니다.
    뉴스 데이터를 수집하고 감성 분석을 통해 투자 결정을 제안합니다."""),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

agent = create_openai_functions_agent(llm, tools, prompt)


agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

# 주가 예측 시나리오
response = agent_executor.invoke({"input": "오늘 금리에 대해 감정 분석을 알려줘"})
result = response['output']
print(result)


# In[36]:




