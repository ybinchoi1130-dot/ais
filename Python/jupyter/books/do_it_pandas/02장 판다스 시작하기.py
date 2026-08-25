#!/usr/bin/env python
# coding: utf-8

# ## 02-1 판다스가 왜 필요할까?

# ## 02-2 데이터셋 불러오기

# ### 데이터 분석은 데이터셋 불러오기부터

# #### [Do It! 실습] 첫 데이터셋 불러오기

#%%

"""
# 데이터프레임 CSV(Comma Separated Values) 다루기
# CSV(Comma Separated Values)
#   - 콤마 즉 쉼표(,)로 구분한 텍스트 데이터 및 텍스트 파일
# 텍스트 파일 포맷: 
#   - CSV(Comma Separated Values)  구분자가 콤마(,)
#   - TSV(Tab Separated Values)    구분자가 탭(\t)
#   - SSV(Space Separated Values)  구분자가 스페이스(공백)

# 파일 처리
#   - DataFrame.to_csv(filename) 
#     데이터프레임 객체를 텍스트(csv) 파일로 저장
#   - DataFrame = pandas.read_csv(filename, sep='...') 
#     판다스가 텍스트(csv) 파일을 읽어서 데이터프레임 객체를 생성
"""


# In[73]:


import pandas


# In[74]:


# TSV
# df = pandas.read_csv('../data/gapminder.tsv', sep='\t')
df = pandas.read_csv('./data/gapminder.tsv', sep='\t')


# In[75]:


print(df)


# In[11]:


import pandas as pd
df = pd.read_csv('./data/gapminder.tsv', sep='\t')


# #### [Do It! 실습] 데이터프레임 이해하기

# In[12]:


print(type(df)) # <class 'pandas.DataFrame'>


# In[13]:


print(df.shape) # (1704, 6)


# In[14]:


print(df.columns)
# Index(['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap'], dtype='str')

# In[15]:

# 컬럼의 자료형
print(df.dtypes)

#%%

"""
country          str  # 나라
continent        str  # 대륙
year           int64  # 연도
lifeExp      float64  # 기대 수명
pop            int64  # 인구
gdpPercap    float64  # 1인당 국내 총 생산
dtype: object
"""

# In[16]:


print(df.info())

#%%

# 레코드 건수(1704)와 Non-Null Count(1704)가 같으므로 
# 결측 데이터 없다.
"""
<class 'pandas.DataFrame'>
RangeIndex: 1704 entries, 0 to 1703
Data columns (total 6 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   country    1704 non-null   str    
 1   continent  1704 non-null   str    
 2   year       1704 non-null   int64  
 3   lifeExp    1704 non-null   float64
 4   pop        1704 non-null   int64  
 5   gdpPercap  1704 non-null   float64
dtypes: float64(2), int64(2), str(2)
memory usage: 80.0 KB
None
"""

#%%
# ### 02-3 데이터 추출하기

# In[17]:


# 데이터프레임의 처음부터 5건의 행을 보여 줌
print(df.head())


# ### 열 데이터 추출하기

# #### [Do It! 실습] 문자열로 열 데이터 추출하기

# In[18]:

# 컬럼(country)만 추출해서 시리즈를 리턴
country_df = df['country']


# In[19]:

# 앞 부분 5건 
print(country_df.head())


# In[20]:

# 뒷 부분 5건
print(country_df.tail())

#%%

# #### [Do It! 실습] 리스트로 열 데이터 추출하기

# In[21]:

# 리스트로 컬럼 목록을 지정하여 추출
subset = df[['country', 'continent', 'year']]


# In[22]:


print(subset)


# #### [Do It! 실습] 두 추출 방법의 차이점 이해하기 

# In[23]:


country_df = df['country']
print(type(country_df)) # <class 'pandas.Series'>


# In[24]:


print(country_df)


# In[25]:

# 컬럼을 하나만 지정해도 리스트로 지정하면
# 리턴은 데이터프레임이다.
country_df_list = df[['country']]
print(type(country_df_list)) # <class 'pandas.DataFrame'>
 

# In[26]:


print(country_df_list)

#%%

# ### 행 데이터 추출하기

# #### [Do It! 실습] 행 이름으로 행 데이터 추출하기

# In[27]:


print(df)


# In[28]:

# 인덱스로 추출
print(df.loc[0])


# In[29]:


print(df.loc[99])


# In[30]:

# 오류: KeyError: -1
# loc는 인덱스로 접근하기 때문에 순번이 아니다.
# 그러므로 마지막 요소(-1)를 접근하는 형태를 사용할 수 없다.
print(df.loc[-1])  # 오류


# In[31]:

df_shape = df.shape
print(type(df_shape), df_shape) # <class 'tuple'> (1704, 6)

#%%
# shape 속성을 사용하여 행의 개수 구하기
number_of_rows = df.shape[0]

# 행의 개수에서 1을 뺀 값으로 마지막 행의 인덱스 구하기
last_row_index = number_of_rows - 1

# 마지막 행의 인덱스로 데이터 추출하기
print(df.loc[last_row_index])  # 인덱스 참조
print(df.iloc[last_row_index]) # 순번 참조



# In[32]:

# 기본: 맨 뒤에서부터 5개를 보여 줌
print(df.tail())

#%%

# 맨 뒤에서부터 n개를 보여 줌
print(df.tail(n=1))

#%%

print(df.tail(n=10))


# In[33]:

# 인덱스를 다중으로 지정하여 추출
# 리스트에 목록을 지정
print(df.loc[[0, 99, 999]])


#%%

# #### [Do It! 실습] 행 번호로 행 데이터 추출하기
# iloc: integer location, 정수로 지정된 위치
# DataFrame.iloc[행순번]

# In[34]:

# 1번째 위치의 행을 추출
# 결과: 시리즈(Series)
print(df.iloc[1])


# In[35]:


print(df.iloc[99])


# In[36]:

# iloc는 순번으로 참조하기 때문에 -1이 지정 가능    
# 맨 마지막 요소
print(df.iloc[-1])

#%%

ilast = len(df) - 1
print(df.iloc[ilast])


#%%

# 맨 뒤(-1)에서부터 역으로 참조 가능
print(df.iloc[-2]) # 1702


# In[37]:

# 다중 선택
print(df.iloc[[0, 99, 999]])

#%%

# 모두 0번째 행
ibegin = -len(df)     # 0번째 행
istart = len(df) * -1 # 0번째 행
print(df.iloc[[0, istart, ibegin]])


#%%

# ### loc와 iloc로 데이터 추출하기
# #### [Do It! 실습] 슬라이싱(slicing) 구문으로 데이터 추출하기

# In[38]:

#     
# 인덱스 0부터 5까지
# 주의: 5가 포함
#   - 인덱스는 순번이 아니다
#   - 인덱스는 지정된 값이다.  
# 컬럼 목록이 생략 되어 전체 컬럼을 의미
print(df.loc[0:5])    

#%%

print(df.loc[0:5,:])    

#%%
    
# 인덱스로 슬라이싱을 이용해서 추출
# 행: 전체, 슬라이싱(:)
# 열: 컬럼 이름('year', 'pop')
# 데이터프레임 = loc[행, 열]
subset = df.loc[:, ['year', 'pop']]
print(subset)


# In[39]:

# IndexError: .iloc requires numeric indexers, got ['year' 'pop' 'gdpPercap']
subset = df.iloc[:, ['year', 'pop', 'gdpPercap']]

#%%

# 행: 전체
# 열: year(2), pop(4), gdpPercap(-1)
subset = df.iloc[:, [2, 4, -1]]
print(subset)


# In[40]:

# KeyError: "None of [Index([2, 4, -1], dtype='int64')] are in the [columns]"
# subset = df.loc[:, [2, 4, -1]]  # 오류
# print(subset)


# In[41]:

# IndexError: .iloc requires numeric indexers, got ['year' 'pop']
# subset = df.iloc[:, ['year', 'pop']]  # 오류
# print(subset)

#%%

# #### [Do It! 실습] range()로 데이터 추출하기

# In[42]:

#%%    

# range()
# 정해진 범위의 수를 반환하는 제너레이터(generator) 즉 생성기이다.
# 그때마다 값을 생성하며 한 번 사용한 값은 메모리에서 사라진다.
# 반복문이 5번 실행된다.
lst = []
for n in range(5):
    lst.append(n)
    end = '\n' if n == 4 else ', '
    print(n, end=end)
    
# print(lst) # [0, 1, 2, 3, 4]

#%%

lst2 = [ n for n in range(5) ]
print(lst2) # [0, 1, 2, 3, 4]

#%%

# range() 함수를 5번 실행해서 최종적으로 리스트에 담음
# 리스트로 변환해야 한다.
small_range = list(range(5))
print(small_range) # [0, 1, 2, 3, 4]


# In[43]:

# 행: 전체
# 열: 'country'부터 'pop'까지
subset = df.iloc[:, small_range]
print(subset)


# In[44]:

# 3부터 6-1까지 즉 5까지: [3, 4, 5]
small_range = list(range(3, 6))
print(small_range)


# In[45]:

# 변수(small_range)가 가지고 있는 컬럼의 위치 목록
# 3:lifeExp, 4:pop, 5:gdpPercap
subset = df.iloc[:, small_range]
print(subset)


# In[46]:

# 0부터 5까지 스텝(2): [0, 2, 4]
# 0:country, 2:year, 4:pop
small_range = list(range(0, 6, 2))
subset = df.iloc[:, small_range]
print(subset)

#%%

# 행: [0, 4, 8, 12, 16]
# 열: [0, 2, 4] -> 0:country, 2:year, 4:pop 
# 행: 20은 포함되지 않음
iloc_list = list(range(0, 20, 4))
ndf = df.iloc[iloc_list, small_range]
print(ndf)

#%%

"""
        country  year       pop
0   Afghanistan  1952   8425333
4   Afghanistan  1972  13079460
8   Afghanistan  1992  16317921
12      Albania  1952   1282697
16      Albania  1972   2263554
"""

#%%
# #### [Do It! 실습] 슬라이싱 구문과 range() 비교하기

# In[47]:

# 컬럼 속성
print(df.columns)
# Index(['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap'], dtype='str')

#%%

# 컬럼 속성 변경
df.columns = [ '나라', '대륙', '년도', '기대수명', '인구', 'GDP']
print(df.head())


# In[48]:

# range()를 이용해서 컬럼 목록 지정
small_range = list(range(3)) # [0,1,2]
subset = df.iloc[:, small_range]
print(subset)


# In[49]:

# 슬라이싱을 이용하여 범위를 지정
# 행: 전체
# 열: 0부터 2까지
subset = df.iloc[:, :3]
print(subset)


# In[50]:

# 슬라이싱을 이용하여 범위를 지정
# 행: 전체
# 열: 3부터 5까지(6-1)
small_range = list(range(3, 6)) # [ 3, 4, 5 ]
subset = df.iloc[:, small_range]
print(subset)


# In[51]:

# 위와 동일함
subset = df.iloc[:, 3:6]
print(subset)


# In[52]:

# ragne(시작, 종료, 스텝)
# 행: 전체
# 열: 0, 2, 4
small_range = list(range(0, 6, 2))
subset = df.iloc[:, small_range]
print(subset)


# In[53]:

# 위와 동일
subset = df.iloc[:, 0:6:2]
print(subset)


#%%

# ### 행과 열 함께 지정하여 추출하기

# In[54]:

# 인덱스를 이용해서 행, 열에 해당하는 1개의 셀을 추출
# print(df.loc[42, 'country'])
print(df.loc[42, '나라']) # Angola


# In[55]:

# 결과는 위와 동일    
# 순번을 이용해서 행, 열에 해당하는 1개의 셀을 추출
print(df.iloc[42, 0]) #  # Angola

#%%

# #### [Do It! 실습] 여러 행과 열 지정하여 데이터 추출하기

# In[56]:

# 목록을 지정
# 행: [0,99,999]
# 열: [0, 3, 5]
print(df.iloc[[0, 99, 999], [0, 3, 5]])


# In[57]:


# print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])

# KeyError: "['gdp'] not in index"
# 컬럼명은 대소문자 구분한다.
# print(df.loc[[0, 99, 999], ['나라', '기대수명', 'gdp']])
print(df.loc[[0, 99, 999], ['나라', '기대수명', 'GDP']])

#%%

GDP = 'gdp'.upper() # 대문자로 변환하라.
gdp = GDP.lower()   # 소문자로 변환하라.
print(f"대문자:{GDP}, 소문자:{gdp}")

print(df.loc[[0, 99, 999], ['나라', '기대수명', GDP]])

#%%

# THE END