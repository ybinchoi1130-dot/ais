#!/usr/bin/env python
# coding: utf-8

# ## 05-1 깔끔한 데이터란? 

# ## 05-2 열 이름이 값일 때

# ### 하나의 열만 남기기

# #### [Do It! 실습] 넒은 데이터 확인하기

# In[1]:


import pandas as pd

pew = pd.read_csv('../data/pew.csv')


# In[2]:


print(pew.iloc[:, 0:5])


# #### [Do It! 실습] 긴 데이터로 만들기

# In[3]:


pew_long = pew.melt(id_vars='religion')
print(pew_long)


# In[4]:


# melt() 메서드
pew_long = pew.melt(id_vars='religion')

# pd.melt() 함수
pew_long = pd.melt(pew, id_vars='religion')


# In[5]:


pew_long = pew.melt(
    id_vars="religion", var_name="income", value_name="count"
)
print(pew_long)


# ### 여러 개의 열 남기기

# #### [Do It! 실습] 여러 개 열 유지하기

# In[6]:


billboard = pd.read_csv('../data/billboard.csv')
print(billboard.iloc[0:5, 0:16])


# In[7]:


billboard_long = billboard.melt(
    id_vars=["year", "artist", "track", "time", "date.entered"],
    var_name="week",
    value_name="rating",
)
print(billboard_long)


# ## 05-3 열 이름에 변수가 여러 개일 때

# ### 열 이름이 여러 가지 뜻일 때 

# #### [Do It! 실습] 깔끔한 데이터 만들기 첫 번째

# In[8]:


ebola = pd.read_csv('../data/country_timeseries.csv')
print(ebola.columns)


# In[9]:


print(ebola.iloc[:5, [0, 1, 2, 10]])


# In[10]:


ebola_long = ebola.melt(id_vars=['Date', 'Day'])
print(ebola_long)


# ### 열 이름 분할하고 새로운 열로 할당하기

# #### [Do It! 실습] 깔끔한 데이터 만들기 두 번째

# In[11]:


variable_split = ebola_long.variable.str.split('_')
print(variable_split[:5])


# In[12]:


print(type(variable_split))


# In[13]:


print(type(variable_split[0]))


# In[14]:


status_values = variable_split.str.get(0)
country_values = variable_split.str.get(1)


# In[15]:


print(status_values)


# In[16]:


ebola_long['status'] = status_values
ebola_long['country'] = country_values
print(ebola_long)


# ### 한 번에 분할하고 합치기

# #### [Do It! 실습] 깔끔한 데이터 한 번에 만들기

# In[17]:


ebola_long = ebola.melt(id_vars=['Date', 'Day'])


# In[18]:


# split the column by _ into a dataframe using expand
variable_split = ebola_long.variable.str.split('_', expand=True)
print(variable_split)


# In[19]:


ebola_long[['status', 'country']] = variable_split
print(ebola_long)


# ## 05-4 변수가 행과 열 모두에 있을 때

# #### [Do It! 실습] 행과 열 모두에 있는 변수 정리하기

# In[20]:


weather = pd.read_csv('../data/weather.csv')
print(weather.iloc[:5, :11])


# In[21]:


weather_melt = weather.melt(
    id_vars=["id", "year", "month", "element"],
    var_name="day",
    value_name="temp",
)

print(weather_melt)


# In[22]:


weather_tidy = weather_melt.pivot_table(
    index=['id', 'year', 'month', 'day'],
    columns='element',
    values='temp'
)
print(weather_tidy)


# In[23]:


weather_tidy_flat = weather_tidy.reset_index()
print(weather_tidy_flat)


# In[24]:


weather_tidy = (
    weather_melt
    .pivot_table(
        index=['id', 'year', 'month', 'day'],
        columns='element',
        values='temp')
    .reset_index()
)
print(weather_tidy)


# In[ ]:




