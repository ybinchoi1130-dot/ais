#!/usr/bin/env python
# coding: utf-8

# # 04 엑셀 기본 함수 구현하기

# ## 4.1 파이썬으로 엑셀 파일 다루기

# ### 파이썬 패키지 설치

# In[1]:

# jupyter notebook
# get_ipython().system('pip list')

# 판다스 설치
# pip install pandas

# 엑셀 모듈 설치
# pip install oopenpyxl

# In[2]:


# pandas 패키지를 pd라는 별명으로 불러오기
import pandas as pd


# ### 데이터 프레임 생성하기

# In[3]:


# 딕셔너리 유형으로 data를 만든 후 데이터 프레임 생성하기
data = {"이름" : ["홍길동", "이순신", "강감찬", "임꺽정", "이성계"],
        "출생년도" : [1980, 1986, 1990, 1985, 1988],
        "점수" : [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)
df


# In[4]:


# df의 열 이름 변경하기
df = df.rename({"출생년도":"출생"}, axis = "columns")
df


# ### 행과 열 추가 및 삭제하기

# In[5]:


# df의 열 데이터 가져오기
df[["이름", "출생"]]	#[이름]과 [출생] 열 데이터 가져오기


# In[6]:


# df의 행 데이터 가져오기
df[1:3]		# 1행부터 2행 데이터 가져오기


# In[7]:


# df에서 [이름]과 [출생] 열의 0행과 1행을 가져오기
df.loc[0:1, ["이름", "출생"]]		# [0:1] 행 선택, [이름], [출생] 열 선택


# In[8]:


df # df 출력


# In[9]:


df["보너스"] = df["점수"] * 5 			# [보너스] 열 추가
df


# In[10]:


df["지역"] = ["서울", "서울", "부산", "대구", "인천"]	# [지역] 열 데이터 추가
df


# In[11]:


del df["보너스"]	# 보너스 열 삭제
df


# In[12]:


df.loc[5] = ["김순신", 1980, 3.3, "광주"]		# 인덱스가 5인 행을 추가
df


# In[13]:


df.iloc[4, 1] = 1999				# 4행 1열의 데이터를 1999로 변경
df.drop(5, inplace = True)			# 5행을 삭제
df


# In[14]:


df1 = df.copy()						# 원 데이터 보존을 위해 df를 df1로 복사
id = df1[df1["점수"] <= 2.0].index  	# df1[“점수”] <= 2.0인 행의 인덱스를 id에 저장 
df1.drop(id, inplace = True)		# id에 저장된 인덱스로 행 삭제
df1


# ### 엑셀 파일 읽고 쓰기

# In[15]:


# 데이터 프레임 변수인 df를 현재 디렉토리에 “명단.xlsx”로 저장하기
df.to_excel("명단.xlsx")


# In[16]:

# 현재 디렉토리의 “명단.xlsx” 파일을 불러와 df_name_list에 저장하기
df_name_list = pd.read_excel("명단.xlsx")

#%%

# 첫 번째 열을 인덱스로 지정하는 코드; 
df_name_list2 = pd.read_excel("명단.xlsx", index_col = 0)

