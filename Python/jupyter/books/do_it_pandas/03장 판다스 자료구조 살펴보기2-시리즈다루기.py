#!/usr/bin/env python
# coding: utf-8

# ## 03-1 나만의 데이터 만들기

# ### 시리즈와 데이터프레임 만들기

# #### [Do It! 실습] 시리즈 만들기

# In[63]:


import pandas as pd

#%%

# ### 시리즈와 불리언

scientists = pd.read_csv('./data/scientists.csv', sep=',')


# #### [Do It! 실습] 기술 통계량 계산하기

# In[81]:


ages = scientists['Age']
print(ages)


# In[82]:

# 다양한 기술 통계량
print(ages.describe())

ages_desc = ages.describe()

#%%

# 데이터의 분포 확인
"""
count     8.000000
mean     59.125000
std      18.325918
min      37.000000
25%      44.000000
50%      58.500000
75%      68.750000
max      90.000000
Name: Age, dtype: float64
"""


# In[83]:

# 평균
print(ages.mean()) # 59.125


# In[84]:


print(ages[ages > ages.mean()])

#%%

"""
1    61
2    90
3    66
7    77
Name: Age, dtype: int64
"""

# In[85]:


print(ages > ages.mean())

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


# In[86]:


print(type(ages > ages.mean()))


# In[87]:

# True인 위치에 있는 시리즈 데이터만 선택
manual_bool_values = [
    True,   # 0
    True,   # 1
    False,  # 2
    False,  # 3
    True,   # 4
    True,   # 5
    False,  # 6
    True,   # 7
]
print(ages[manual_bool_values])

ages_manual_series = ages[manual_bool_values]

#%%

"""
0    37
1    61
4    56
5    45
7    77
Name: Age, dtype: int64
"""

#%%
# ### 시리즈와 브로드캐스팅

# #### [Do It! 실습] 벡터와 벡터, 벡터와 스칼라 계산하기

# In[88]:

# 벡터의 요소의 갯수가 같은 경우
# 결과: 원본 벡터 요소와 동일한 갯수
print(ages + ages)


# In[89]:


print(ages * ages)


# In[90]:

# 벡터의 모든 요소에 한 개의 값을 대입해서 연산을 수행
# 결과: 벡터의 요소와 동일한 갯수
print(ages + 100)


# In[91]:


print(ages * 2)


#%%

# #### [Do It! 실습] 길이가 서로 다른 벡터 연산하기

# In[92]:

# 인덱스가 동일한 요소끼리 연산을 수행
# 나머지 요소는 NaN(Not a Number) 
twos =  pd.Series([1, 100])
# print(ages + pd.Series([1, 100]))
print(ages + twos)

#%%

"""
0     38.0
1    161.0
2      NaN
3      NaN
4      NaN
5      NaN
6      NaN
7      NaN
dtype: float64
"""

#%%

# 동일한 인덱스끼지 연산을 수행
# 없는 인덱스는 결측값(NaN)으로 채운다.
three =  pd.Series([1, 3, 5], index=[2,4,6])
print(ages + three)

#%%
"""
0     NaN
1     NaN
2    91.0
3     NaN
4    59.0
5     NaN
6    46.0
7     NaN
dtype: float64
"""
# In[93]:


import numpy as np

# print(ages + np.array([1, 100]))  # 오류


# #### [Do It! 실습] 인덱스가 같은 벡터 자동 정렬하기

# In[94]:

# 인덱스 정렬    
# ascending=True : 오름차순
# ascending=False: 내림차순
rev_ages = ages.sort_index(ascending=False)
print(rev_ages)

#%%

"""
7    77
6    41
5    45
4    56
3    66
2    90
1    61
0    37
Name: Age, dtype: int64
"""

# In[95]:


print(ages * 2)


# In[96]:

# 인덱스의 정렬 기준
# ages    : 오름차순
# rev_ages: 내림차순
# 처리결과: 정렬된 기준에 관계없이 해당하는 인덱스를 찾아서 연산이 수행 된다. 
print(ages + rev_ages)

#%%

"""
0     74
1    122
2    180
3    132
4    112
5     90
6     82
7    154
Name: Age, dtype: int64
"""

#%%
# ## 03-3 데이터프레임 다루기

# ### 데이터프레임의 구성

# In[97]:


scientists.index


# In[98]:


scientists.columns


# In[99]:


scientists.values


# ### 데이터프레임과 불리언 추출

# In[100]:


print(scientists.loc[scientists['Age'] > scientists['Age'].mean()])


# ### 데이터프레임과 브로드캐스팅

# #### [Do It! 실습] 데이터프레임을 대상으로 연산하기

# In[101]:


first_half = scientists[:4]
second_half = scientists[4:]

print(first_half)


# In[102]:


print(second_half)


# In[103]:


print(scientists * 2)


# In[104]:


df1 = df2 = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

df_added = df1.add(df2)
print(df_added)


# ## 03-4 시리즈와 데이터프레임 데이터 변경하기

# #### [Do It! 실습] 열 추가하기

# In[105]:


print(scientists.dtypes)


# In[106]:


born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
print(born_datetime)


# In[107]:


died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')


# In[108]:


scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)


# In[109]:


print(scientists.head())


# In[110]:


print(scientists.shape)


# In[111]:


print(scientists.dtypes)


# #### [Do It! 실습] 열 내용 변경하기

# In[112]:


print(scientists['Age'])


# In[113]:


print(scientists["Age"].sample(frac=1, random_state=42))


# In[114]:


scientists["Age"] = scientists["Age"].sample(frac=1, random_state=42)
print(scientists['Age'])


# In[115]:


scientists["Age"] = scientists["Age"].sample(frac=1, random_state=42).values
print(scientists['Age'])


# In[116]:


scientists['age_days'] = (scientists['died_dt'] - scientists['born_dt'])
print(scientists)


# In[117]:


# scientists['age_years'] = (scientists['age_days'].astype('timedelta64[Y]'))  # pandas 2.0.3 오류
scientists['age_years'] = (scientists['age_days'].dt.days / 365).apply(np.floor)  # 날짜 수를 햇수로 변환

print(scientists)


# #### [Do It! 실습] assign()으로 열 수정하기 

# In[118]:


scientists = scientists.assign(
    age_days_assign=scientists['died_dt'] - scientists['born_dt'],
    # age_year_assign=scientists['age_days'].astype('timedelta64[Y]'))  # pandas 2.0.3 오류
    age_year_assign=(scientists['age_days'].dt.days / 365).apply(np.floor)
)
print(scientists)


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


scientists_dropped = scientists.drop(['Age'], axis="columns")


# In[122]:


print(scientists_dropped.columns)


# ## 03-5 데이터 저장하고 불러오기

# ### 피클로 저장하고 불러오기

# #### [Do It! 실습] 시리즈와 데이터프레임 저장하기

# In[123]:


names = scientists['Name']
print(names)


# In[124]:


names.to_pickle('../output/scientists_names_series.pickle')


# In[125]:


scientists.to_pickle('../output/scientists_df.pickle')


# #### [Do It! 실습] 피클 데이터 읽어 오기

# In[126]:


series_pickle = pd.read_pickle('../output/scientists_names_series.pickle')
print(series_pickle)


# In[127]:


dataframe_pickle = pd.read_pickle('../output/scientists_df.pickle')
print(dataframe_pickle)


# ### CSV와 TSV 파일로 저장하고 불러오기

# In[128]:


scientists.to_csv('../output/scientists_df_no_index.csv', index=False)


# ### 엑셀로 저장하기

# #### [Do It! 실습] 시리즈와 데이터프레임 저장하기

# In[129]:


#!pip install openpyxl  # openpyxl이 없다면 주석을 제거하고 설치하세요.


# In[130]:


names = scientists['Name']
print(names)


# In[131]:


names_df = names.to_frame()


# In[132]:


names_df.to_excel('../output/scientists_names_series_df.xls',
                  engine='openpyxl')


# In[133]:


scientists.to_excel("../output/scientists_df.xlsx",
                    sheet_name="scientists",
                    index=False)


# ### 다양한 형식으로 저장하기

# #### [Do It! 실습] feather 파일로 저장하기

# In[134]:


#!pip install pyarrow  # pyarrow가 없다면 주석을 제거하고 설치하세요.


# In[135]:


scientists.to_feather('../output/scientists.feather')


# In[136]:


sci_feather = pd.read_feather('../output/scientists.feather')
print(sci_feather)


# #### [Do It! 실습] 딕셔너리로 변환하기

# In[137]:


sci_sub_dict = scientists.head(2)


# In[138]:


sci_dict = sci_sub_dict.to_dict()


# In[139]:


import pprint
pprint.pprint(sci_dict)


# In[140]:


sci_dict_df = pd.DataFrame.from_dict(sci_dict)
print(sci_dict_df)


# #### [Do It! 실습] JSON으로 저장하기

# In[141]:


sci_json = sci_sub_dict.to_json(orient='records', indent=2, date_format="iso")
pprint.pprint(sci_json)


# In[142]:


sci_json_df = pd.read_json(
    ('[\n'
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
 ']'),
     orient="records"
)
print(sci_json_df)


# In[143]:


print(sci_json_df.dtypes)


# In[144]:


sci_json_df["died_dt_json"] = pd.to_datetime(sci_json_df["died_dt"])
print(sci_json_df)


# In[145]:


print(sci_json_df.dtypes)


# In[ ]:




