#!/usr/bin/env python
# coding: utf-8

# # 05 업무에 자주 쓰는 실무 함수 구현하기

# ## 5.1 동적 배열 함수

# ### 실습 데이터 불러오기

# In[1]:


import pandas as pd     # pandas를 pd라는 이름으로 불러오기

# 동적 배열 함수 실습을 위해 액셀 파일을 불러와 work에 저장하기
work = pd.read_excel(r"./근무 유형.xlsx", sheet_name = "Sheet1")
work


# ### 원하는 데이터 필터링하기

# In[2]:


work = pd.read_excel(r"./근무 유형.xlsx", sheet_name = "Sheet1")
w1 = work.loc[work["부서"] == "제조팀"]			# 부서명이 "제조팀"인 행 추출
w2 = work.loc[work["근무형태"].isin(["상근"])]	# 근무형태가 "상근"인 행 추출

#display(w1, w2)									# w1, w2 출력


# In[3]:


work.loc[(work["부서"] == "제조팀") | (work["근무형태"] == "교대") ]


# In[4]:


work.loc[~work["근무형태"].isin(["상근"])]


# ### 기준 열로 정렬하기

# In[5]:


work = pd.read_excel(r"./근무 유형.xlsx", sheet_name = "Sheet1")
work.sort_values(by = "사원번호").head()	# 사원번호 기준으로 오름차순 정렬


# In[6]:


work.sort_index().head()				# 인덱스 기준으로 오름차순 정렬


# ### 중복 행 제거하기

# In[7]:


work = pd.read_excel(r"./근무 유형.xlsx", sheet_name = "Sheet1")
work.duplicated()				# 중복 행을 True로 출력


# In[8]:


work.drop_duplicates()			# 중복 행 제거


