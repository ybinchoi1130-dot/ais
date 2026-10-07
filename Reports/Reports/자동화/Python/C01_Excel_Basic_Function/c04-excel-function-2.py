#!/usr/bin/env python
# coding: utf-8

# # 04 엑셀 기본 함수 구현하기

# ## 4.2 텍스트 함수

# ### 파이썬 패키지 설치

# In[1]:

# jupyter notebook
# get_ipython().system('pip list')

# 판다스 설치
# pip install pandas


# In[17]:


# pandas를 pd라는 이름으로 불러오기
import pandas as pd     

# 텍스트 함수 실습을 위한 직원 정보 엑셀을 불러와 데이터 프레임 info에 저장하기
info = pd.read_excel(r"./직원 정보.xlsx", sheet_name = "Sheet1")
info


# ### 여러 셀의 문자 합치기

# In[18]:


info = pd.read_excel(r"./직원 정보.xlsx", sheet_name = "Sheet1")
info["성명"] = info["성"] + info["이름"]		# 데이터 프레임 열 연산
info["성명1"] = info[["성", "이름"]].sum(1)		# 열 방향으로 각 행의 문자를 결합
info										    # 데이터 프레임 info 출력


# ### 몇 개의 문자만 추출하기

# In[19]:


info = pd.read_excel(r"./직원 정보.xlsx", sheet_name = "Sheet1")
info["사원번호 앞 4자리"] = info["사원번호"].str[0:4]  # 사원번호 앞에서 4자리 추출
info["전화번호 뒤 4자리"] = info["전화번호"].str[9:13] # 전화번호 뒤에서 4자리 추출
info


# In[20]:


info = pd.read_excel(r"./직원 정보.xlsx", sheet_name = "Sheet1")
info["구"] = info["주소"].str.split(" ").str[1]
info[["성", "이름", "전화번호", "구"]]


# ### 영문 대소문자 바꾸기

# In[21]:


info = pd.read_excel(r"./직원 정보.xlsx", sheet_name = "Sheet1")
info["대문자"] = info["영문명"].str.upper()		# [영문명] 열을 대문자로 변환
info["첫 글자"] = info["영문명"].str.capitalize()	# [영문명] 열의 첫 글자만 대문자로 변환
info[["순번", "성", "이름", "영문명", "전화번호", "대문자", "첫 글자"]]


# In[22]:


# 대문자를 소문자로 변경하고 소문자를 대문자로 변경
str.swapcase("ABcde")


#%%
# ### 특정 문자 바꾸기

# In[23]:


info = pd.read_excel(r"./직원 정보.xlsx", sheet_name = "Sheet1")
info["phone"] = info["전화번호"].str.replace("-", "", 1) 	# 첫 번째 하이픈(-) 제거 
info["phone1"] = info["전화번호"].str.replace("-"," ")		# 모든 하이픈 (-)을 공백으로 대체
info[["순번", "성", "이름", "전화번호", "phone", "phone1"]]


# ### 문자열 길이 구하기

# In[24]:


info = pd.read_excel(r"./직원 정보.xlsx", sheet_name = "Sheet1")
info["주소 길이"] = info["주소"].str.len()			    # [주소] 열의 문자열 길이 반환  
info[["순번", "성", "이름", "주소", "주소 길이" ]].head()


# ### 문자열 공백 삭제하기

# In[25]:


info = pd.read_excel(r"./직원 정보.xlsx", sheet_name = "Sheet1")
info["주소 길이"] = info["주소"].str.len()		        # [주소] 열의 길이 구하기
info["공백 제거"] = info["주소"].str.strip()		    # [주소] 열의 문자열 앞뒤 공백 제거
info["공백 제거 후 길이"] = info["공백 제거"].str.len()	# 공백 제거 문자열의 길이 구하기
info[["순번", "주소", "주소 길이", "공백 제거", "공백 제거 후 길이"]].tail(6)

#%%

# THE END