#!/usr/bin/env python
# coding: utf-8

# # 05 업무에 자주 쓰는 실무 함수

# ## 5.1 동적 배열 함수

# ### 실습 데이터 불러오기

# In[2]:


import pandas as pd     # pandas를 pd라는 이름으로 불러오기

# 동적 배열 함수 실습을 위해 액셀 파일을 불러와 work에 저장하기
work = pd.read_excel(r"근무 유형.xlsx", sheet_name = "Sheet1")
work


# ### 원하는 데이터 필터링하기

# In[2]:


work = pd.read_excel(r"근무 유형.xlsx", sheet_name = "Sheet1")
w1 = work.loc[work["부서"] == "제조팀"]			# 부서명이 "제조팀"인 행 추출
w2 = work.loc[work["근무형태"].isin(["상근"])]	# 근무형태가 "상근"인 행 추출
# display(w1, w2)									# w1, w2 출력
print(w1)
print(w2)


# In[3]:


work.loc[(work["부서"] == "제조팀") | (work["근무형태"] == "교대") ]


# In[4]:


work.loc[~work["근무형태"].isin(["상근"])]


# ### 기준 열로 정렬하기

# In[5]:


work = pd.read_excel(r"근무 유형.xlsx", sheet_name = "Sheet1")
work.sort_values(by = "사원번호").head()	# 사원번호 기준으로 오름차순 정렬


# In[6]:


work.sort_index().head()				# 인덱스 기준으로 오름차순 정렬


# ### 중복 행 제거하기

# In[7]:


work = pd.read_excel(r"근무 유형.xlsx", sheet_name = "Sheet1")
work.duplicated()				# 중복 행을 True로 출력


# In[8]:


work.drop_duplicates()			# 중복 행 제거


# ## 5.2 찾기 및 참조 함수

# ### 실습 데이터 불러오기

# In[9]:


# pandas를 pd라는 이름으로 불러오기
import pandas as pd     

# 찾기 및 참조 함수 실습을 위해 "식자재 주문.xlsl"을 불러와 product, order에 저장하기
product = pd.read_excel(r"식자재 주문.xlsx", sheet_name = "product")
order = pd.read_excel(r"식자재 주문.xlsx", sheet_name = "order")
product


# In[10]:


order


# ### 인덱스로 값 확인하기

# In[11]:


product = pd.read_excel(r"식자재 주문.xlsx", sheet_name = "product")
mapping = {"1":"청주", "2":"대구", "3":"광주"}		# 딕셔너리 자료형으로 Key : Value 정의
product["공장"] = product["제품코드"].str[4].map(mapping)	# 제품코드 마지막 값을 Key로 사용
product.head()


# ### 원하는 값 찾기

# In[12]:


product = pd.read_excel(r"식자재 주문.xlsx", sheet_name = "product")
order = pd.read_excel(r"식자재 주문.xlsx", sheet_name = "order" )
product.set_index("제품코드", inplace = True)	# product["제품코드"]를 인덱스로 설정
order.set_index("제품코드", inplace = True)		# order["제품코드"]를 인덱스로 설정
order["제품명"] = product["제품명"]				# 동일 인덱스의 product["제품명"]을 order에 추가
order["단가"] = product["단가"]					# 동일 인덱스의 product["단가"]를 order에 추가
order["주문금액"] = order["주문수량"] * order["단가"]	# 주문금액 계산하여 order에 추가
order


# In[13]:


order.reset_index(inplace = True)		# order 데이터 프레임 인덱스 리셋


# ## 5.3 논리 및 정보 함수

# ### 실습 데이터 불러오기

# In[14]:


import pandas as pd		# pandas를 pd라는 이름으로 불러오기
# 논리 함수 실습을 위해 "과일 주문.xlsx" 파일을 불러와 fruit에 저장
fruit = pd.read_excel(r"과일 주문.xlsx", sheet_name = "Sheet1")
fruit


# ### 조건 함수 사용하기

# In[15]:


fruit = pd.read_excel(r"과일 주문.xlsx", sheet_name = "Sheet1")
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

# ** 날짜 및 시간 함수 수정 **
# 
#     기존 : fruit["오늘 날짜"] = pd.datetime.now()	
#     수정 : fruit["오늘 날짜"] = datetime.now()
# 

# In[4]:


import pandas as pd
from datetime import datetime 

fruit = pd.read_excel(r"과일 주문.xlsx", sheet_name = "Sheet1")
pd.to_datetime(fruit["판매일자"])			# 날짜형으로 변환
pd.to_datetime(fruit["유통기한"])
fruit["판매일"] = fruit["판매일자"].dt.day		# datetime 자료형에서 일자만 출력
fruit["오늘 날짜"] = datetime.now()		# [오늘 날짜] 열 생성
fruit["유통기한 경과일수"] = (fruit["오늘 날짜"] - fruit["유통기한"]).dt.days
fruit.head()


# In[17]:


from datetime import datetime		# datetime 패키지 import
today = datetime.now()				# 현재 날짜 시간을 today 변수에 저장
print(today.year)					# today 변수에서 년 데이터만 출력
print(today.month) 					# today 변수에서 월 데이터만 출력
print(today.day)					# today 변수에서 일 데이터만 출력


# ** 시간 변경
# 
#     기존 : time1 = datetime(2019, 10, 1, 15, 30, 1)
#     변경 : time1 = datetime(2024, 2, 1, 15, 30, 1)

# In[3]:


from datetime import datetime	
time1 = datetime(2024, 2, 1, 15, 30, 1)		# time1에 임의의 날짜 데이터 저장
time2 = datetime.now()							# time2에 현재 날짜/시간 저장
print((time2 - time1).days, "일")				# 두 변수 간 일 차이 출력
print((time2 - time1).seconds, "초")				# 두 변수 간 초 단위 차이 출력
print((time2 - time1).seconds / 3600, "시간")		# 두 변수 간 시간 단위 차이 출력


# In[ ]:




