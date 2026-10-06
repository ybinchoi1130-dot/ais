#!/usr/bin/env python
# coding: utf-8

# # 04 엑셀 기본 함수 구현하기

# ## 4.3 수학 및 통계 함수

# ### 파이썬 패키지 설치

# In[1]:

# jupyter notebook
# get_ipython().system('pip list')

# 판다스 설치
# pip install pandas

# In[2]:

# ### 실습 데이터 불러오기

# In[26]:


# pandas를 pd라는 이름으로 불러오기
import pandas as pd     

# 수학 및 통계 함수 실습을 위해 "성적 처리.xlsx" 파일을 불러와 score에 저장하기
score = pd.read_excel(r"./성적 처리.xlsx", sheet_name = "Sheet1")
score		# 'c:\works\chapter04' 디렉토리에 파일을 복사한 후 진행


# ### 데이터 합계 구하기

# In[1]:


score = pd.read_excel(r"./성적 처리.xlsx", sheet_name = "Sheet1")
total_korean = score["국어"].sum(axis=0)		# 행 방향 [국어] 열의 데이터 합계 구하기
total_korean


# In[28]:


score["sum"] = score.iloc[:, 2:7].sum(1)		# 2~6열 각 행의 데이터 합계 구하기
score["sum1"] = score["국어"] + score["영어"] + score["수학"] + score["사회"] + score["과학"]
score.head()


# ### 데이터 평균 구하기

# In[29]:


score = pd.read_excel(r"./성적 처리.xlsx", sheet_name = "Sheet1")
korean_avg = score["국어"].mean()		# [국어] 열의 행 방향 평균 구하기
korean_avg


# In[30]:


score["평균"] = score.iloc[:, 2:7].mean(1)			# 2~6열의 열 방향 각 행의 평균 구하기
score["평균1"] = (score["국어"] + score["영어"] + score["수학"] + score["사회"] + score["과학"]) / 5
score


# ### 조건에 따른 합계, 평균 구하기

# In[31]:


score = pd.read_excel(r"./성적 처리.xlsx", sheet_name = "Sheet1")
score1 = score.groupby(["반"]).sum()		# [반] 열을 기준으로 그룹화한 후 합계 계산
score1						# score1 출력


# In[32]:


score2 = score.groupby(["반"]).mean()		# [반] 열을 기준으로 그룹화한 후 평균 계산
score2						# score2 출력


# ### 순위 구하기

# In[33]:


score = pd.read_excel(r"./성적 처리.xlsx", sheet_name = "Sheet1")
score["평균"] = score.iloc[:, 2:7].mean(1)			# 2~6열의 열 방향 각 행의 평균 구하기
score["순위_오름"] = score["평균"].rank(ascending = True)		# 동점 시 평균 순위 부여, 오름차순
score["순위_내림"] = score["평균"].rank(ascending = False)	# 동점 시 평균 순위 부여, 내림차순
score["순위_내림_min"] = score["평균"].rank(method = "min", ascending = False)  # 동점 시 최소 순위
score


# ### 최대값/최소값 구하기 

# In[34]:


score = pd.read_excel(r"./성적 처리.xlsx", sheet_name = "Sheet1")
score_row = score.iloc[:, [2, 3, 4, 5, 6]]		# score에서 숫자열만 추출하여 score_row에 저장
score["MIN"] = score_row.min(1)		# score_row의 행 방향 최소값을 score[“MIN”]에 저장
score["MAX"] = score_row.max(1)		# score_row의 행 방향 최대값을 score[“MAX”]에 저장
score


# In[35]:


score = pd.read_excel(r"./성적 처리.xlsx", sheet_name = "Sheet1")
score.describe()		# score 데이터 프레임의 기초 통계량 확인

