#!/usr/bin/env python
# coding: utf-8

"""
데이터프레임 연산 메서드 및 비교 메서드
연산자   메서드              설명
-----------------------------------------------------
+        add()               덧셈
-        sub(), subtract()   뺄셈
*        mul(), multiply()   곱셈
/        div(), divide()     나눗셈
%        mod()               나머지
**       pow()               거듭제곱
-----------------------------------------------------
>        gt()                크다(Greater Than)
<        lt()                작다(Less Than)
==       eq()                같다(Equal)
!=       ne()                같지않다(Not Equal)
>=       ge()                크거나 같다(Greater Than or Equal)
<=       le()                작거나 같다(Less Than or Equal)
-----------------------------------------------------
"""



#%%
# ## 03-1 나만의 데이터 만들기

# ### 시리즈와 데이터프레임 만들기

# #### [Do It! 실습] 시리즈 만들기

#%%

import pandas as pd

#%%

# ### 시리즈와 불리언

scientists = pd.read_csv('./data/scientists.csv', sep=',')

#%%

# ## 03-3 데이터프레임 다루기

# ### 데이터프레임의 구성

# In[97]:

print(scientists.index)
# RangeIndex(start=0, stop=8, step=1)

# In[98]:

print(scientists.columns)
# Index(['Name', 'Born', 'Died', 'Age', 'Occupation'], dtype='str')

# In[99]:

# print(scientists.values)
scientists.values

#%%

# scientists.values 출력 결과로 데이터프레임을 생성
df = pd.DataFrame(
[['Rosaline Franklin', '1920-07-25', '1958-04-16', 37, 'Chemist'],
 ['William Gosset', '1876-06-13', '1937-10-16', 61, 'Statistician'],
 ['Florence Nightingale', '1820-05-12', '1910-08-13', 90, 'Nurse'],
 ['Marie Curie', '1867-11-07', '1934-07-04', 66, 'Chemist'],
 ['Rachel Carson', '1907-05-27', '1964-04-14', 56, 'Biologist'],
 ['John Snow', '1813-03-15', '1858-06-16', 45, 'Physician'],
 ['Alan Turing', '1912-06-23', '1954-06-07', 41, 'Computer Scientist'],
 ['Johann Gauss', '1777-04-30', '1855-02-23', 77, 'Mathematician']])

df.columns = scientists.columns


#%%
# ### 데이터프레임과 불리언 추출

# In[100]:

scientists['Age']
scientists['Age'].mean()  # np.float64(59.125)

#%%

"""
0    False
1     True
2     True
3     True
4    False
5    False
6    False
7     True
Name: Age, dtype: bool
"""

#%%

# True에 해당하는 인덱스만 선택 됨
# 인덱스: 1,2,3,7
age_gt_mean1 = scientists.loc[scientists['Age'] > scientists['Age'].mean()]
age_gt_mean2 = scientists.iloc[scientists['Age'] > scientists['Age'].mean()]

age_gt_mean3 = scientists[scientists['Age'] > scientists['Age'].mean()]

age_bools = scientists['Age'] > scientists['Age'].mean()
age_gt_mean4 = scientists[age_bools]

#%%

# ### 데이터프레임과 브로드캐스팅

# #### [Do It! 실습] 데이터프레임을 대상으로 연산하기

# In[101]:

# 슬라이싱으로 데이터 행을 추출
first_half = scientists[:4]  # 0~3
second_half = scientists[4:] # 4~7

print(first_half)
print(second_half)


# In[103]:

# 타입 확인
scientists.dtypes

#%%

"""
Name            str
Born            str
Died            str
Age           int64
Occupation      str
dtype: object
"""

#%%

# 연산: 데이터프레임 * 2
# 데이터프레임의 자료형에 맞춰서 연산이 수행
# 문자열: 붙이기(반복)
# 숫자형: 산술 연산
scientists_multi2 = scientists * 2


# In[104]:

"""
데이터프레임 연산 메서드 및 비교 메서드
연산자   메서드              설명
-----------------------------------------------------
+        add()               덧셈
-        sub(), subtract()   뺄셈
*        mul(), multiply()   곱셈
/        div(), divide()     나눗셈
%        mod()               나머지
**       pow()               거듭제곱
-----------------------------------------------------
>        gt()                크다(Greater Than)
<        lt()                작다(Less Than)
==       eq()                같다(Equal)
!=       ne()                같지않다(Not Equal)
>=       ge()                크거나 같다(Greater Than or Equal)
<=       le()                작거나 같다(Less Than or Equal)
"""

#%%
df1 = df2 = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 프레임끼리 더하기
df_added1 = df1.add(df2)
df_added2 = df1 + df2

#%%

# 프레임끼리 곱하기
df_multi1 = df1 * df2
df_multi2 = df1.mul(df2)
df_multi3 = df1.multiply(df2)

#%%

df_eq1 = df1 == df2
df_eq2 = df1.eq(df2)

#%%

df_gt1 = df_added1 > df1
df_gt2 = df_added1.gt(df1)

#%%

# ## 03-4 시리즈와 데이터프레임 데이터 변경하기

# #### [Do It! 실습] 열 추가하기

# In[105]:


print(scientists.dtypes)


# In[106]:

# 날짜: 
# 날짜형, 문자열, 정수형(1900부터 경과 시간), 표현형식 다양
# 국가별 시차, 국가별 표현 방식 다양
# format: 문자열 형식을 지정
#  - %Y: 연도 4자리
#  - %m: 월 2자리
#  - %d: 일 2자리
# 컬럼('born')을 문자열에서 날짜형을 변환
born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
print(born_datetime)


# In[107]:

died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')


# In[108]:

# 컬럼 추가: born_dt, died_dt
scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)


# In[109]:


print(scientists.head())


# In[110]:


print(scientists.shape) # (8, 7)


# In[111]:

print(scientists.dtypes) 

#%%

"""
Name                     str
Born                     str
Died                     str
Age                    int64
Occupation               str
born_dt       datetime64[us]
died_dt       datetime64[us]
dtype: object
"""

#%%

# #### [Do It! 실습] 열 내용 변경하기

# In[112]:


print(scientists['Age'])


# In[113]:

# 지정된 열을 기준으로 데이터프레임의 행의 위치를 변경
# frac: 0~1
# random_state: 씨드값 고정, 동일한 난수 발생
print(scientists["Age"].sample(frac=1, random_state=42)) # 

#%%

print(scientists["Age"].sample(frac=1)) # 무작위


# In[114]:

# index 기준으로 자동 병합하기 때문에 제자리로 돌아 간다.
scientists["Age"] = scientists["Age"].sample(frac=1, random_state=42)
print(scientists['Age'])


# In[115]:

# values를 사용
scientists["Age"] = scientists["Age"].sample(frac=1, random_state=42).values
print(scientists['Age'])


# In[116]:

# 날짜 연산: 
# 나이: 죽은날짜 - 태어난 날짜
scientists['age_days'] = (scientists['died_dt'] - scientists['born_dt'])
print(scientists)


# In[117]:

import numpy as np
# scientists['age_years'] = (scientists['age_days'].astype('timedelta64[Y]'))  # pandas 2.0.3 오류
# scientists['age_years'] = (scientists['age_days'].astype('timedelta64[us]'))  # pandas 2.0.3 오류
scientists['age_years'] = (scientists['age_days'].dt.days / 365).apply(np.floor)  # 날짜 수를 햇수로 변환

print(scientists)


# #### [Do It! 실습] assign()으로 열 수정하기 

# In[118]:

# 열 추가 및 수정: assign
scientists = scientists.assign(
    age_days_assign=scientists['died_dt'] - scientists['born_dt'],
    # age_year_assign=scientists['age_days'].astype('timedelta64[Y]'))  # pandas 2.0.3 오류
    age_year_assign=(scientists['age_days'].dt.days / 365).apply(np.floor)
)
print(scientists)


#%%
# ##### <한 걸음 더!> 다른 방법으로 나이 계산하기

# In[119]:


scientists = scientists.assign(
    age_days_assign=scientists["died_dt"] - scientists["born_dt"],
    # age_year_assign=lambda df_: df_["age_days_assign"].astype("timedelta64[Y]"),  # pandas 2.0.3 오류
    age_year_assign=lambda df_: (df_["age_days_assign"].dt.days / 365).apply(np.floor), 
)
print(scientists)


# #### [Do It! 실습] 열 삭제하기

# In[120]:


print(scientists.columns)


# In[121]:

# 컬럼 삭제: drop()
# axis="columns"
# axis=1
scientists_dropped = scientists.drop(['Age'], axis="columns")
scientists_dropped2 = scientists.drop(['Age'], axis=1)


# In[122]:

print(scientists_dropped.columns)

#%%

# ## 03-5 데이터 저장하고 불러오기

# ### 피클로 저장하고 불러오기

# #### [Do It! 실습] 시리즈와 데이터프레임 저장하기

# In[123]:


names = scientists['Name']
print(names)


# In[124]:

# 시리즈를 저장
names.to_pickle('./output/scientists_names_series.pickle')


# In[125]:

# 데이터프레임을 저장
scientists.to_pickle('./output/scientists_df.pickle')


# #### [Do It! 실습] 피클 데이터 읽어 오기

# In[126]:

# 피클(pickle) 파일 포맷: 바이너리(이진형식)
# 파일 확장자: *.pickle, *.p, *.pkl
series_pickle = pd.read_pickle('./output/scientists_names_series.pickle')
print(series_pickle)


# In[127]:


dataframe_pickle = pd.read_pickle('./output/scientists_df.pickle')
print(dataframe_pickle)


#%%
# ### CSV와 TSV 파일로 저장하고 불러오기

# In[128]:

# CSV 파일로 저장
# index=False: 인덱스 제외
scientists.to_csv('./output/scientists_df_in_index.csv') # 인덱스 포함
scientists.to_csv('./output/scientists_df_no_index.csv', index=False) # 인덱스 제외

#%%

# ### 엑셀로 저장하기

# #### [Do It! 실습] 시리즈와 데이터프레임 저장하기

# In[129]:

# 엑셀 파일 읽기 및 저장을 위한 패키지
#!pip install openpyxl  # openpyxl이 없다면 주석을 제거하고 설치하세요.


# In[130]:


# 시리즈
names = scientists['Name']
print(names)


# In[131]:

# 시리즈 -> 데이터프레임
names_df = names.to_frame()


# In[132]:

# 엑셀 파일로 저장
# engine='openpyxl' : 엑셀 파일을 실제적으로 처리하는 모듈(엔진)
names_df.to_excel('./output/scientists_names_series_df.xls', engine='openpyxl')


# In[133]:

# 엑셀 파일로 저장
# 인덱스 제외: index=False
# 시트이름: scientists
scientists.to_excel("./output/scientists_df.xlsx",
                    sheet_name="scientists",
                    index=False)


#%%
# ### 다양한 형식으로 저장하기

# #### [Do It! 실습] feather 파일로 저장하기

# In[134]:


#!pip install pyarrow  # pyarrow가 없다면 주석을 제거하고 설치하세요.
# R과 같은 다른 언어에서 읽을 수 있는 이진 객체로 저장하고 읽음

# In[135]:


scientists.to_feather('./output/scientists.feather')


# In[136]:


sci_feather = pd.read_feather('./output/scientists.feather')
print(sci_feather)


#%%

# #### [Do It! 실습] 딕셔너리로 변환하기

# In[137]:

# 상위 2행을 읽음
sci_sub_dict = scientists.head(2)


# In[138]:

# 데이터프레임을 파이썬 자료형 딕셔너리(dict)로 변환
sci_dict = sci_sub_dict.to_dict()

#%%

print(sci_dict)

# In[139]:

# 딕셔너리를 보기 좋게 출력
import pprint
pprint.pprint(sci_dict)


# In[140]:

# 딕셔너리 -> 데이터프레임
sci_dict_df = pd.DataFrame.from_dict(sci_dict)
print(sci_dict_df)


#%%

# #### [Do It! 실습] JSON으로 저장하기

# In[141]:

# 데이터프레임 -> JSON
sci_json = sci_sub_dict.to_json(orient='records', indent=2, date_format="iso")
pprint.pprint(sci_json)
print(sci_json)

#%%

# JSON 파일을 읽기서 데이터프레임으로 변환
# 파일이름: sci_json.json
sci_json_in = pd.read_json("./data/sci_json.json")
print(sci_json_in)

# In[142]:

import io

sci_json_df = pd.read_json(io.StringIO(
 '[\n'
 '  {\n'
 '    "Name":"Rosaline Franklin",\n'
 '    "Born":"1920-07-25",\n'
 '    "Died":"1958-04-16",\n'
 '    "Age":61,\n'
 '    "Occupation":"Chemist",\n'
 '    "born_dt":"1920-07-25T00:00:00.000",\n'
 '    "died_dt":"1958-04-16T00:00:00.000",\n'
 '    "age_days":"P13779DT0H0M0S",\n'
 '    "age_years":37.0,\n'
 '    "age_days_assign":"P13779DT0H0M0S",\n'
 '    "age_year_assign":37.0\n'
 '  },\n'
 '  {\n'
 '    "Name":"William Gosset",\n'
 '    "Born":"1876-06-13",\n'
 '    "Died":"1937-10-16",\n'
 '    "Age":45,\n'
 '    "Occupation":"Statistician",\n'
 '    "born_dt":"1876-06-13T00:00:00.000",\n'
 '    "died_dt":"1937-10-16T00:00:00.000",\n'
 '    "age_days":"P22404DT0H0M0S",\n'
 '    "age_years":61.0,\n'
 '    "age_days_assign":"P22404DT0H0M0S",\n'
 '    "age_year_assign":61.0\n'
 '  }\n'
 ']'), orient="records")

print(sci_json_df)


# In[143]:


print(sci_json_df.dtypes)


# In[144]:


sci_json_df["died_dt_json"] = pd.to_datetime(sci_json_df["died_dt"])
print(sci_json_df)


# In[145]:


print(sci_json_df.dtypes)


#%%

##################################################################
# JSON 포맷 #
##################################################################

import pandas as pd

scientists = pd.read_csv('./data/scientists.csv', sep=',')

#%%

# 상위 2행을 읽음
ndf = scientists.head(2)

#%%

# DataFrame -> JSON
ndf_json = ndf.to_json(orient='records', indent=2, date_format="iso")
print(type(ndf_json)) # <class 'str'>
print(ndf_json)

#%%

"""
[
  {
    "Name":"Rosaline Franklin",
    "Born":"1920-07-25",
    "Died":"1958-04-16",
    "Age":37,
    "Occupation":"Chemist"
  },
  {
    "Name":"William Gosset",
    "Born":"1876-06-13",
    "Died":"1937-10-16",
    "Age":61,
    "Occupation":"Statistician"
  }
]
"""
#%%

import json

# json 형식으로 된 문자열을 읽어서 파이썬 객체 변환
# 리턴: 리스트 형식
json_data = json.loads(ndf_json)

# 리스트 -> 데이터프레임
json_df = pd.DataFrame(json_data)
print(json_df)





