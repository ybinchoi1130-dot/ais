#!/usr/bin/env python
# coding: utf-8

# ## 02-1 판다스가 왜 필요할까?

# ## 02-2 데이터셋 불러오기

# ### 데이터 분석은 데이터셋 불러오기부터

# #### [Do It! 실습] 첫 데이터셋 불러오기

#%%

import pandas as pd
df = pd.read_csv('./data/gapminder.tsv', sep='\t')

#%%

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


#%%

###############################################################
# ### 02-4 기초 통계 계산하기
###############################################################


#%%

year_gb = df.groupby('year')['lifeExp']
# <pandas.api.typing.SeriesGroupBy object at 0x000002172353B950>

#%%

# 특정한 그룹 단위로 집계
# 그룹연산: groupby('year')
# 컬럼선택: lifeExp 평균
# 처리결과: 연도별 기대 수명의 평균
print(df.groupby('year')['lifeExp'].mean())

#%%

"""
1952    49.057620
1957    51.507401
1962    53.609249
1967    55.678290
1972    57.647386
1977    59.570157
1982    61.533197
1987    63.212613
1992    64.160338
1997    65.014676
2002    65.694923
2007    67.007423
Name: lifeExp, dtype: float64
"""

# In[60]:


grouped_year_df = df.groupby('year')
print(type(grouped_year_df))


# In[61]:

print(grouped_year_df)
# <pandas.api.typing.DataFrameGroupBy object at 0x000002172353B360>

# In[62]:


grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))
# <class 'pandas.api.typing.SeriesGroupBy'>


# In[63]:


print(grouped_year_df_lifeExp)
# <pandas.api.typing.SeriesGroupBy object at 0x000002172477F130>

# In[64]:

# 연도별 기대 수명의 평균(mean)
mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)

#%%

year_continent_count = df.groupby('year')['continent'].count()
print(year_continent_count)

#%%

"""
year
1952    142
1957    142
1962    142
1967    142
1972    142
1977    142
1982    142
1987    142
1992    142
1997    142
2002    142
2007    142
Name: continent, dtype: int64
"""

#%%

# #### [Do It! 실습] 2개 이상 열 그룹화화기

# In[65]:


multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()


# In[66]:


print(multi_group_var)

#%%

"""
                  lifeExp     gdpPercap
year continent                         
1952 Africa     39.135500   1252.572466
     Americas   53.279840   4079.062552
     Asia       46.314394   5195.484004
     Europe     64.408500   5661.057435
     Oceania    69.255000  10298.085650
1957 Africa     41.266346   1385.236062
     Americas   55.960280   4616.043733
     Asia       49.318544   5787.732940
     Europe     66.703067   6963.012816
     Oceania    70.295000  11598.522455
1962 Africa     43.319442   1598.078825
     Americas   58.398760   4901.541870
     Asia       51.563223   5729.369625
     Europe     68.539233   8365.486814
     Oceania    71.085000  12696.452430
1967 Africa     45.334538   2050.363801
     Americas   60.410920   5668.253496
     Asia       54.663640   5971.173374
     Europe     69.737600  10143.823757
     Oceania    71.310000  14495.021790
1972 Africa     47.450942   2339.615674
     Americas   62.394920   6491.334139
     Asia       57.319269   8187.468699
     Europe     70.775033  12479.575246
     Oceania    71.910000  16417.333380
1977 Africa     49.580423   2585.938508
     Americas   64.391560   7352.007126
     Asia       59.610556   7791.314020
     Europe     71.937767  14283.979110
     Oceania    72.855000  17283.957605
1982 Africa     51.592865   2481.592960
     Americas   66.228840   7506.737088
     Asia       62.617939   7434.135157
     Europe     72.806400  15617.896551
     Oceania    74.290000  18554.709840
1987 Africa     53.344788   2282.668991
     Americas   68.090720   7793.400261
     Asia       64.851182   7608.226508
     Europe     73.642167  17214.310727
     Oceania    75.320000  20448.040160
1992 Africa     53.629577   2281.810333
     Americas   69.568360   8044.934406
     Asia       66.537212   8639.690248
     Europe     74.440100  17061.568084
     Oceania    76.945000  20894.045885
1997 Africa     53.598269   2378.759555
     Americas   71.150480   8889.300863
     Asia       68.020515   9834.093295
     Europe     75.505167  19076.781802
     Oceania    78.190000  24024.175170
2002 Africa     53.325231   2599.385159
     Americas   72.422040   9287.677107
     Asia       69.233879  10174.090397
     Europe     76.700600  21711.732422
     Oceania    79.740000  26938.778040
2007 Africa     54.806038   3089.032605
     Americas   73.608120  11003.031625
     Asia       70.728485  12473.026870
     Europe     77.648600  25054.481636
     Oceania    80.719500  29810.188275
"""     

#%%

multi_group_var2 = df.groupby(['continent', 'year'])[['lifeExp', 'gdpPercap']].mean()
print(multi_group_var2)

#%%

# multi_group_var의 인덱스는 2개의 컬럼으로 구성 됨
# 인덱스로 추출할 때는 튜플로 지정해야 한다.
print(multi_group_var.loc[(1952, 'Africa')])
print(multi_group_var.loc[(1952, 'Asia')])

# In[67]:

#
flat = multi_group_var.reset_index()
print(flat)

print(flat.loc[0])
print(flat.loc[2])


#%%

# ### 그룹화한 데이터 개수 세기

# #### [Do It! 실습] 그룹화한 데이터 개수 구하기

# In[68]:

# 중복을 제외한 갯수
# 각 대륙별 나라의 갯수
print(df.groupby('continent')['country'].nunique())

#%%

"""
continent
Africa      52
Americas    25
Asia        33
Europe      30
Oceania      2
Name: country, dtype: int64
"""

# In[69]:

# 빈도수: 행의 갯수
# 대륙별 각 나라의 빈도수
print(df.groupby('continent')['country'].value_counts())

#%%

"""
continent  country          
Africa     Zimbabwe             12
           Equatorial Guinea    12
           Eritrea              12
           Ethiopia             12
           Gabon                12
                                ..
Europe     Germany              12
           Serbia               12
           Slovenia             12
Oceania    Australia            12
           New Zealand          12
Name: count, Length: 142, dtype: int64
"""

#%%

# ### 02-5 데이터를 그래프로 표현하려면?

# #### [Do It! 실습] 데이터프레임으로 그래프 그리기

# In[70]:


global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)


# In[71]:


global_yearly_life_expectancy.plot()


# In[ ]:




