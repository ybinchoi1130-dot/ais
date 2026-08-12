#!/usr/bin/env python
# coding: utf-8

# ## 02-1 판다스가 왜 필요할까?

# ## 02-2 데이터셋 불러오기

# ### 데이터 분석은 데이터셋 불러오기부터

# #### [Do It! 실습] 첫 데이터셋 불러오기

# In[73]:


import pandas


# In[74]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')


# In[75]:


print(df)


# In[11]:


import pandas as pd
df = pd.read_csv('../data/gapminder.tsv', sep='\t')


# #### [Do It! 실습] 데이터프레임 이해하기

# In[12]:


print(type(df))


# In[13]:


print(df.shape)


# In[14]:


print(df.columns)


# In[15]:


print(df.dtypes)


# In[16]:


print(df.info())


# ### 02-3 데이터 추출하기

# In[17]:


print(df.head())


# ### 열 데이터 추출하기

# #### [Do It! 실습] 문자열로 열 데이터 추출하기

# In[18]:


country_df = df['country']


# In[19]:


print(country_df.head())


# In[20]:


print(country_df.tail())


# #### [Do It! 실습] 리스트로 열 데이터 추출하기

# In[21]:


subset = df[['country', 'continent', 'year']]


# In[22]:


print(subset)


# #### [Do It! 실습] 두 추출 방법의 차이점 이해하기 

# In[23]:


country_df = df['country']
print(type(country_df))


# In[24]:


print(country_df)


# In[25]:


country_df_list = df[['country']]
print(type(country_df_list))


# In[26]:


print(country_df_list)


# ### 행 데이터 추출하기

# #### [Do It! 실습] 행 이름으로 행 데이터 추출하기

# In[27]:


print(df)


# In[28]:


print(df.loc[0])


# In[29]:


print(df.loc[99])


# In[30]:


# print(df.loc[-1])  # 오류


# In[31]:


# shape 속성을 사용하여 행의 개수 구하기
number_of_rows = df.shape[0]

# 행의 개수에서 1을 뺀 값으로 마지막 행의 인덱스 구하기
last_row_index = number_of_rows - 1

# 마지막 행의 인덱스로 데이터 추출하기
print(df.loc[last_row_index])


# In[32]:


print(df.tail(n=1))


# In[33]:


print(df.loc[[0, 99, 999]])


# #### [Do It! 실습] 행 번호로 행 데이터 추출하기

# In[34]:


print(df.iloc[1])


# In[35]:


print(df.iloc[99])


# In[36]:


print(df.iloc[-1])


# In[37]:


print(df.iloc[[0, 99, 999]])


# ### loc와 iloc로 데이터 추출하기

# #### [Do It! 실습] 슬라이싱 구문으로 데이터 추출하기

# In[38]:


subset = df.loc[:, ['year', 'pop']]
print(subset)


# In[39]:


subset = df.iloc[:, [2, 4, -1]]
print(subset)


# In[40]:


# subset = df.loc[:, [2, 4, -1]]  # 오류
# print(subset)


# In[41]:


# subset = df.iloc[:, ['year', 'pop']]  # 오류
# print(subset)


# #### [Do It! 실습] range()로 데이터 추출하기

# In[42]:


small_range = list(range(5))
print(small_range)


# In[43]:


subset = df.iloc[:, small_range]
print(subset)


# In[44]:


small_range = list(range(3, 6))
print(small_range)


# In[45]:


subset = df.iloc[:, small_range]
print(subset)


# In[46]:


small_range = list(range(0, 6, 2))
subset = df.iloc[:, small_range]
print(subset)


# #### [Do It! 실습] 슬라이싱 구문과 range() 비교하기

# In[47]:


print(df.columns)


# In[48]:


small_range = list(range(3))
subset = df.iloc[:, small_range]
print(subset)


# In[49]:


subset = df.iloc[:, :3]
print(subset)


# In[50]:


small_range = list(range(3, 6))
subset = df.iloc[:, small_range]
print(subset)


# In[51]:


subset = df.iloc[:, 3:6]
print(subset)


# In[52]:


small_range = list(range(0, 6, 2))
subset = df.iloc[:, small_range]
print(subset)


# In[53]:


subset = df.iloc[:, 0:6:2]
print(subset)


# ### 행과 열 함께 지정하여 추출하기

# In[54]:


print(df.loc[42, 'country'])


# In[55]:


print(df.iloc[42, 0])


# #### [Do It! 실습] 여러 행과 열 지정하여 데이터 추출하기

# In[56]:


print(df.iloc[[0, 99, 999], [0, 3, 5]])


# In[57]:


print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])


# ### 02-4 기초 통계 계산하기

# In[58]:


print(df)


# In[59]:


print(df.groupby('year')['lifeExp'].mean())


# In[60]:


grouped_year_df = df.groupby('year')
print(type(grouped_year_df))


# In[61]:


print(grouped_year_df)


# In[62]:


grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))


# In[63]:


print(grouped_year_df_lifeExp)


# In[64]:


mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)


# #### [Do It! 실습] 2개 이상 열 그룹화화기

# In[65]:


multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()


# In[66]:


print(multi_group_var)


# In[67]:


flat = multi_group_var.reset_index()
print(flat)


# ### 그룹화한 데이터 개수 세기

# #### [Do It! 실습] 그룹화한 데이터 개수 구하기

# In[68]:


print(df.groupby('continent')['country'].nunique())


# In[69]:


print(df.groupby('continent')['country'].value_counts())


# ### 02-5 데이터를 그래프로 표현하려면?

# #### [Do It! 실습] 데이터프레임으로 그래프 그리기

# In[70]:


global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)


# In[71]:


global_yearly_life_expectancy.plot()


# In[ ]:




