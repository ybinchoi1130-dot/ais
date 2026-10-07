#!/usr/bin/env python
# coding: utf-8

# # 05 업무에 자주 쓰는 실무 함수 구현하기

# ## 5.2 찾기 및 참조 함수

# ### 실습 데이터 불러오기

# In[9]:


# pandas를 pd라는 이름으로 불러오기
import pandas as pd     

# 찾기 및 참조 함수 실습을 위해 "식자재 주문.xlsl"을 불러와 product, order에 저장하기
product = pd.read_excel(r"./식자재 주문.xlsx", sheet_name = "product")
order = pd.read_excel(r"./식자재 주문.xlsx", sheet_name = "order")
product


# In[10]:


order


# ### 인덱스로 값 확인하기

# In[11]:


product = pd.read_excel(r"./식자재 주문.xlsx", sheet_name = "product")
mapping = {"1":"청주", "2":"대구", "3":"광주"}		# 딕셔너리 자료형으로 Key : Value 정의
product["공장"] = product["제품코드"].str[4].map(mapping)	# 제품코드 마지막 값을 Key로 사용
product.head()


# ### 원하는 값 찾기

# In[12]:


product = pd.read_excel(r"./식자재 주문.xlsx", sheet_name = "product")
order = pd.read_excel(r"./식자재 주문.xlsx", sheet_name = "order" )
product.set_index("제품코드", inplace = True)	# product["제품코드"]를 인덱스로 설정
order.set_index("제품코드", inplace = True)		# order["제품코드"]를 인덱스로 설정
order["제품명"] = product["제품명"]				# 동일 인덱스의 product["제품명"]을 order에 추가
order["단가"] = product["단가"]					# 동일 인덱스의 product["단가"]를 order에 추가
order["주문금액"] = order["주문수량"] * order["단가"]	# 주문금액 계산하여 order에 추가
order


# In[13]:


order.reset_index(inplace = True)		# order 데이터 프레임 인덱스 리셋

order
