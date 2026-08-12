#!/usr/bin/env python
# coding: utf-8

# ## 03-1 나만의 데이터 만들기

# ### 시리즈와 데이터프레임 만들기

# #### [Do It! 실습] 시리즈 만들기

# In[63]:


import pandas as pd

s = pd.Series(['banana', 42])
print(s)


# In[64]:


s = pd.Series(data=['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)


# #### [Do It! 실습] 데이터 프레임 만들기

# In[65]:


scientists = pd.DataFrame({
        "Name": ["Rosaline Franklin", "William Gosset"],
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "Age": [37, 61],
})

print(scientists)


# In[66]:


scientists = pd.DataFrame(
    data={
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "Age": [37, 61],
    },
    index=["Rosaline Franklin", "William Gosset"],
    columns=["Occupation", "Born", "Died", "Age"],
)

print(scientists)


# ## 03-2 시리즈 다루기

# #### [Do It! 실습] 시리즈 추출하기

# In[67]:


scientists = pd.DataFrame(
    data={
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "Age": [37, 61],
    },
    index=["Rosaline Franklin", "William Gosset"],
    columns=["Occupation", "Born", "Died", "Age"],
)

print(scientists)


# In[68]:


first_row = scientists.loc['William Gosset']
print(type(first_row))


# In[69]:


print(first_row)


# In[70]:


print(first_row.index)


# In[71]:


print(first_row.values)


# ### 시리즈의 keys() 메서드

# In[72]:


print(first_row.keys())


# In[73]:


print(first_row.index[0])


# In[74]:


print(first_row.keys()[0])


# ### 시리즈와 ndarray

# #### [Do It! 실습] 시리즈의 메서드 사용하기

# In[75]:


ages = scientists['Age']
print(ages)


# In[76]:


# 평균
print(ages.mean())


# In[77]:


# 최솟값
print(ages.min())


# In[78]:


# 최댓값
print(ages.max())


# In[79]:


# 표준 편차
print(ages.std())


# ### 시리즈와 불리언

# In[80]:


scientists = pd.read_csv('../data/scientists.csv')


# #### [Do It! 실습] 기술 통계량 계산하기

# In[81]:


ages = scientists['Age']
print(ages)


# In[82]:


print(ages.describe())


# In[83]:


print(ages.mean())


# In[84]:


print(ages[ages > ages.mean()])


# In[85]:


print(ages > ages.mean())


# In[86]:


print(type(ages > ages.mean()))


# In[87]:


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


# ### 시리즈와 브로드캐스팅

# #### [Do It! 실습] 벡터와 벡터, 벡터와 스칼라 계산하기

# In[88]:


print(ages + ages)


# In[89]:


print(ages * ages)


# In[90]:


print(ages + 100)


# In[91]:


print(ages * 2)


# #### [Do It! 실습] 길이가 서로 다른 벡터 연산하기

# In[92]:


print(ages + pd.Series([1, 100]))


# In[93]:


import numpy as np

# print(ages + np.array([1, 100]))  # 오류


# #### [Do It! 실습] 인덱스가 같은 벡터 자동 정렬하기

# In[94]:


rev_ages = ages.sort_index(ascending=False)
print(rev_ages)


# In[95]:


print(ages * 2)


# In[96]:


print(ages + rev_ages)


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




