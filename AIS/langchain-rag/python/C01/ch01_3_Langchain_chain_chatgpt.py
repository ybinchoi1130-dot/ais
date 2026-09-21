#!/usr/bin/env python
# coding: utf-8

# # Langchain Basic

# ### module install

# In[ ]:

# get_ipython().system(' pip install langchain_openai==0.2.6')
# get_ipython().system(' pip install langchain_community==0.3.5')
"""
langchain                     1.4.0
langchain-openai              1.6.2
langchain-community           0.4.2

langchain-classic             1.0.8
langchain-core                1.6.3
langchain-protocol            0.0.19
langchain-text-splitters      1.1.2
"""

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
pythagoras = llm.invoke("피타고라스 정리의 공식은 무엇인가요?")
print(pythagoras)

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
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

"""
input_variables=['query'] input_types={} partial_variables={} messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['query'], input_types={}, partial_variables={}, template='초등학생이 이해할 수 있는 방식으로 답을 설명하세요.: <질문>: {query}'), additional_kwargs={})]
소셜미디어에 대한 긍정 의견:
1. 소통과 교류 촉진: social media를 통해 사람들은 어디서든 손쉽게 소통하고 정보를 공유할 수 있습니다. 이를 통해 지역, 시간, 직업 등의 제약 없이 사회적 연결성을 증진시킬 수 있습니다.
2. 정보 및 의견 공유: social media를 통해 다양한 정보와 의견을 얻을 수 있으며, 각종 이슈나 문제에 대한 의견을 자유롭게 표현할 수 있습니다. 이를 통해 사회적 대화와 토론이 활성화될 수 있습니다.
3. 비즈니스 및 마케팅: 많은 기업들이 social media를 통해 제품이나 서비스를 홍보하고 고객과 소통하는데 활용하고 있습니다. 이를 통해 비즈니스 성공에 도움을 줄 뿐만 아니라 소비자들과의 관계도 선순환할 수 있습니다.
4. 정보접근성 증진: social media를 통해 뉴스, 이벤트, 엔터테인먼트 등의 정보를 빠르고 편리하게 얻을 수 있습니다. 특히 실시간으로 발생하는 이슈에 대한 빠른 업데이트가 가능하여 다양한 정보에 접근하기 쉽습니다.
5. 창의성과 융합: social media를 통해 다양한 아이디어와 콘텐츠를 얻을 수 있으며, 이를 바탕으로 창의적인 작품을 만들어내거나 협업을 통해 새로운 가치를 창출할 수 있습니다. 

이와 같이 social media는 다양한 측면에서 우리 삶을 풍요롭게 만들어주고, 소통과 교류를 촉진하는 등 많은 긍정적인 영향을 미칠 수 있습니다.

소셜미디어에 대한 부정 의견:
1. 개인정보 유출 문제: 사적인 정보나 개인정보가 유출되어 사생활이 침해될 수 있음
2. 혐오 발언 및 사이버 괴롭힘: social media를 통해 쉽게 익명으로 혐오 발언이나 괴롭힘을 당할 수 있음
3. 정보의 신뢰성과 다양성 저하: social media의 알고리즘은 사용자들의 의견과 관심사를 반영하여 다양성을 감소시킬 수 있음
4. 시간 낭비: 너무 많은 시간을 social media에 투자하면 현실 생활과 사회적 연대감이 손상될 수 있음
5. 비교와 자아 취약성: 다른 사람들의 완벽해 보이는 사진이나 소식을 통해 자아 비교를 하게 되어 자아 취약감이 증가할 수 있음
6. 의사 소통 능력 감퇴: 오프라인에서의 소통 능력이 감퇴되고 사회적 관계 형성 능력이 약화될 수 있음.

최종 의견 요즘 사회에서는 social media가 우리 삶에 지대한 영향을 끼치고 있습니다. 
그에 대한 논쟁도 끊이지 않고 있습니다. 
어떤 사람들은 social media가 소통과 정보 교류에 큰 도움이 되고, 
사회적 연결성을 증진시킨다고 주장합니다. 
반면에, 다른 사람들은 social media가 현실에서의 관계를 손상시키고 
개인정보 유출 문제를 야기한다고 우려하고 있습니다. 

또한, social media의 플랫폼들이 언론과 정보의 다양성을 저하시키고 
사회적으로 유해한 콘텐츠를 확산시킨다는 비판도 있습니다. 
특히 어린이들과 청소년들이 social media를 오용하여 
사회적 문제들과 심리적인 건강에 영향을 받는다는 우려도 큽니다. 

이러한 논쟁들은 계속되고 있지만, 
social media의 존재와 중요성을 부인할 수는 없을 것입니다. 
따라서, social media의 긍정적인 측면을 촉진하고 
부정적인 측면을 극복하기 위한 방안을 모색해야 할 것입니다.
"""


