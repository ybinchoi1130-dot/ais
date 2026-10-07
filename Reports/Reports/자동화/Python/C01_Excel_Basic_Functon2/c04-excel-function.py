#!/usr/bin/env python
# coding: utf-8

# # 04 엑셀 기본 함수 구현하기

# ## 4.1 파이썬으로 엑셀 파일 다루기

# ### 파이썬 패키지 설치

# In[1]:


# get_ipython().system('pip list')


# In[1]:


# pandas 패키지를 pd라는 별명으로 불러오기
import pandas as pd


# ### 데이터 프레임 생성하기

# In[3]:


# 딕셔너리 유형으로 data를 만든 후 데이터 프레임 생성하기
import pandas as pd
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


# 현재 디렉토리의 “명단.xlsx” 파일을 불러와 df12에 저장하기
df12 = pd.read_excel("명단.xlsx")
# 첫 번째 열을 인덱스로 지정하는 코드; df12 = pd.read_excel(“명단.xlsx", index_col = 0)


# ## 4.2 텍스트 함수

# In[17]:


# pandas를 pd라는 이름으로 불러오기
import pandas as pd     

# 텍스트 함수 실습을 위한 직원 정보 엑셀을 불러와 데이터 프레임 info에 저장하기
info = pd.read_excel(r"직원 정보.xlsx", sheet_name = "Sheet1")
info


# ### 여러 셀의 문자 합치기

# In[18]:


info = pd.read_excel(r"직원 정보.xlsx", sheet_name = "Sheet1")
info["성명"] = info["성"] + info["이름"]			# 데이터 프레임 열 연산
info["성명1"] = info[["성", "이름"]].sum(1)		# 열 방향으로 각 행의 문자를 결합
info										# 데이터 프레임 info 출력


# ### 몇 개의 문자만 추출하기

# In[19]:


info = pd.read_excel(r"직원 정보.xlsx", sheet_name = "Sheet1")
info["사원번호 앞 4자리"] = info["사원번호"].str[0:4]  # 사원번호 앞에서 4자리 추출
info["전화번호 뒤 4자리"] = info["전화번호"].str[9:13] # 전화번호 뒤에서 4자리 추출
info


# In[20]:


info = pd.read_excel(r"직원 정보.xlsx", sheet_name = "Sheet1")
info["구"] = info["주소"].str.split(" ").str[1]
info[["성", "이름", "전화번호", "구"]]


# ### 영문 대소문자 바꾸기

# In[21]:


info = pd.read_excel(r"직원 정보.xlsx", sheet_name = "Sheet1")
info["대문자"] = info["영문명"].str.upper()		# [영문명] 열을 대문자로 변환
info["첫 글자"] = info["영문명"].str.capitalize()	# [영문명] 열의 첫 글자만 대문자로 변환
info[["순번", "성", "이름", "영문명", "전화번호", "대문자", "첫 글자"]]


# In[22]:


str.swapcase("ABcde")


# ### 특정 문자 바꾸기

# In[23]:


info = pd.read_excel(r"직원 정보.xlsx", sheet_name = "Sheet1")
info["phone"] = info["전화번호"].str.replace("-", "", 1) 	# 첫 번째 하이픈(-) 제거 
info["phone1"] = info["전화번호"].str.replace("-"," ")		# 모든 하이픈 (-)을 공백으로 대체
info[["순번", "성", "이름", "전화번호", "phone", "phone1"]]


# ### 문자열 길이 구하기

# In[24]:


info = pd.read_excel(r"직원 정보.xlsx", sheet_name = "Sheet1")
info["주소 길이"] = info["주소"].str.len()			    # [주소] 열의 문자열 길이 반환  
info[["순번", "성", "이름", "주소", "주소 길이" ]].head()


# ### 문자열 공백 삭제하기

# In[25]:


info = pd.read_excel(r"직원 정보.xlsx", sheet_name = "Sheet1")
info["주소 길이"] = info["주소"].str.len()		# [주소] 열의 길이 구하기
info["공백 제거"] = info["주소"].str.strip()		# [주소] 열의 문자열 앞뒤 공백 제거
info["공백 제거 후 길이"] = info["공백 제거"].str.len()	# 공백 제거 문자열의 길이 구하기
info[["순번", "주소", "주소 길이", "공백 제거", "공백 제거 후 길이"]].tail(6)


# ## 4.3 수학 및 통계 함수

# ### 실습 데이터 불러오기

# In[26]:


# pandas를 pd라는 이름으로 불러오기
import pandas as pd     

# 수학 및 통계 함수 실습을 위해 "성적 처리.xlsx" 파일을 불러와 score에 저장하기
score = pd.read_excel(r"성적 처리.xlsx", sheet_name = "Sheet1")
score


# ### 데이터 합계 구하기

# ** 합계 출력 코드 수정
# 
#     기존 : total_korean
#     변경 : print(total_korean)

# In[5]:


score = pd.read_excel("성적 처리.xlsx", sheet_name = "Sheet1")
score = score[:12]
total_korean = score["국어"].sum(axis=0)		# 행 방향 [국어] 열의 데이터 합계 구하기
print(total_korean)


# In[28]:


score["sum"] = score.iloc[:, 2:7].sum(1)		# 2~6열 각 행의 데이터 합계 구하기
score["sum1"] = score["국어"] + score["영어"] + score["수학"] + score["사회"] + score["과학"]
score.head()


# ### 데이터 평균 구하기

# ** 평균 출력 코드 수정
# 
#     기존 : korean_avg
#     변경 : print(korean_avg)

# In[8]:


# score = pd.read_excel(r"성적 처리.xlsx", sheet_name = "Sheet1")
korean_avg = score["국어"].mean()		# [국어] 열의 행 방향 평균 구하기
print(korean_avg)


# In[30]:


score["평균"] = score.iloc[:, 2:7].mean(1)			# 2~6열의 열 방향 각 행의 평균 구하기
score["평균1"] = (score["국어"] + score["영어"] + score["수학"] + score["사회"] + score["과학"])/5
score


# ### 조건에 따른 합계, 평균 구하기

# **  score1 코드 수정
# 
#     기존 : score1 = score.groupby(["반"]).sum()
#     기존 : score1 = score[["반","국어","영어","수학","사회","과학"]].groupby(["반"]).sum()
# 
# **  score2 코드 수정
#     
#     기존 : score1 = score.groupby(["반"]).mean()
#     기존 : score1 = score[["반","국어","영어","수학","사회","과학"]].groupby(["반"]).mean()

# In[19]:


# score = pd.read_excel(r"성적 처리.xlsx", sheet_name = "Sheet1")
score1 = score[["반","국어","영어","수학","사회","과학"]].groupby(["반"]).sum()	       # 반, 다섯 과목의 점수 데이터를 추출하여 [반] 열을 기준으로 그룹화한 후 합계 계산
score1[["국어","영어","수학","사회","과학"]]      # 반 별 다섯 과목의 점수 합계 출력


# In[22]:


score2 = score[["반","국어","영어","수학","사회","과학"]].groupby(["반"]).mean()		# 반, 다섯 과목의 점수 데이터를 추출하여 [반] 열을 기준으로 그룹화한 후 평균 계산
score2						# score2 출력


# ### 순위 구하기

# In[33]:


score = pd.read_excel(r"성적 처리.xlsx", sheet_name = "Sheet1")
score["평균"] = score.iloc[:, 2:7].mean(1)			# 2~6열의 열 방향 각 행의 평균 구하기
score["순위_오름"] = score["평균"].rank(ascending = True)		# 동점 시 평균 순위 부여, 오름차순
score["순위_내림"] = score["평균"].rank(ascending = False)	# 동점 시 평균 순위 부여, 내림차순
score["순위_내림_min"] = score["평균"].rank(method = "min", ascending = False)  # 동점 시 최소 순위
score


# ### 최대값/최소값 구하기 

# In[34]:


score = pd.read_excel(r"성적 처리.xlsx", sheet_name = "Sheet1")
score_row = score.iloc[:, [2, 3, 4, 5, 6]]		# score에서 숫자열만 추출하여 score_row에 저장
score["MIN"] = score_row.min(1)		# score_row의 행 방향 최소값을 score[“MIN”]에 저장
score["MAX"] = score_row.max(1)		# score_row의 행 방향 최대값을 score[“MAX”]에 저장
score


# In[35]:


score = pd.read_excel(r"성적 처리.xlsx", sheet_name = "Sheet1")
score.describe()		# score 데이터 프레임의 기초 통계량 확인

