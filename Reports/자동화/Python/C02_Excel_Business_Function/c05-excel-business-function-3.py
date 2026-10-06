#!/usr/bin/env python
# coding: utf-8

# # 05 업무에 자주 쓰는 실무 함수 구현하기

# ## 5.3 논리 및 정보 함수

# ### 실습 데이터 불러오기


# In[14]:


import pandas as pd		# pandas를 pd라는 이름으로 불러오기
# 논리 함수 실습을 위해 "과일 주문.xlsx" 파일을 불러와 fruit에 저장
fruit = pd.read_excel(r"./과일 주문.xlsx", sheet_name = "Sheet1")
fruit


# ### 조건 함수 사용하기

# In[15]:


fruit = pd.read_excel(r"./과일 주문.xlsx", sheet_name = "Sheet1")
fruit["비고"] = ""							# [비고] 열 생성
for idx, x in enumerate(fruit["금액"]):		# [금액] 열 값과 인덱스를 하나씩 반환
    if x >= 500000:		# x값(금액)이 500000 이상이면, [비고] 열에 “50만원 이상” 저장 
        fruit["비고"].loc[idx] = "50만원 이상"
    elif x >= 200000:	# x값(금액)이 200000 이상이면, [비고] 열에 “20만원 이상” 저장
        fruit["비고"].loc[idx] = "20만원 이상"
    else:				# x값(금액)이 200000 미만이면, [비고] 열에 “20만원 미만” 저장
        fruit["비고"].loc[idx] = "20만원 미만"
fruit.head(6)						# fruit 출력


# ### 날짜 및 시간 함수

# In[2]:


import pandas as pd
fruit = pd.read_excel(r"./과일 주문.xlsx", sheet_name = "Sheet1")
pd.to_datetime(fruit["판매일자"])			# 날짜형으로 변환
pd.to_datetime(fruit["유통기한"])
fruit["판매일"] = fruit["판매일자"].dt.day		# datetime 자료형에서 일자만 출력
fruit["오늘 날짜"] = pd.datetime.now()		# [오늘 날짜] 열 생성
fruit["유통기한 경과일수"] = (fruit["오늘 날짜"] - fruit["유통기한"]).dt.days
fruit.head()


# In[17]:


from datetime import datetime		# datetime 패키지 import
today = datetime.now()				# 현재 날짜 시간을 today 변수에 저장
print(today.year)					# today 변수에서 년 데이터만 출력
print(today.month) 					# today 변수에서 월 데이터만 출력
print(today.day)					# today 변수에서 일 데이터만 출력


# In[18]:


time1 = datetime(2019, 10, 1, 15, 30, 1)		# time1에 임의의 날짜 데이터 저장
time2 = datetime.now()							# time2에 현재 날짜/시간 저장
print((time2 - time1).days, "일")				# 두 변수 간 일 차이 출력
print((time2 - time1).seconds, "초")				# 두 변수 간 초 단위 차이 출력
print((time2 - time1).seconds / 3600, "시간")		# 두 변수 간 시간 단위 차이 출력

