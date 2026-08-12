#!/usr/bin/env python
# coding: utf-8

# ## 09-1 결측값이란?

# In[41]:


from numpy import NaN, NAN, nan


# In[42]:


print(NaN == True)
print(NaN == 0)
print(NaN == '')
print(NaN == NaN)
print(NaN == NAN)
print(NaN == nan)
print(nan == NAN)


# In[43]:


import pandas as pd

print(pd.isnull(NaN))
print(pd.isnull(nan))
print(pd.isnull(NAN))


# In[44]:


print(pd.notnull(NaN))
print(pd.notnull(42))
print(pd.notnull('missing'))


# ## 09-2 결측값은 왜 생길까?

# ### 데이터를 불러올 때 생기는 결측값

# In[45]:


visited_file = '../data/survey_visited.csv'
print(pd.read_csv(visited_file))


# In[46]:


print(pd.read_csv(visited_file, keep_default_na=False))


# In[47]:


print(
    pd.read_csv(visited_file, na_values=[""], keep_default_na=False)
)


# ### 데이터를 연결할 때 생기는 결측값

# In[48]:


visited = pd.read_csv('../data/survey_visited.csv')
survey = pd.read_csv('../data/survey_survey.csv')
print(visited)


# In[49]:


print(survey)


# In[50]:


vs = visited.merge(survey, left_on='ident', right_on='taken')
print(vs)


# ### 직접 입력한 결측값

# In[51]:


num_legs = pd.Series({'goat': 4, 'amoeba': nan})
print(num_legs)


# In[52]:


scientists = pd.DataFrame(
    {
        "Name": ["Rosaline Franklin", "William Gosset"],
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "missing": [NaN, nan],
    }
)

print(scientists)


# In[53]:


print(scientists.dtypes)


# In[54]:


scientists = pd.DataFrame(
    {
        "Name": ["Rosaline Franklin", "William Gosset"],
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
    }
)

scientists["missing"] = nan
print(scientists)


# ### 인덱스를 다시 설정할 때 생기는 결측값

# In[55]:


gapminder = pd.read_csv('../data/gapminder.tsv', sep='\t')

life_exp = gapminder.groupby(['year'])['lifeExp'].mean()
print(life_exp)


# In[56]:


y2000 = life_exp[life_exp.index > 2000]
print(y2000)


# In[57]:


print(y2000.reindex(range(2000, 2010)))


# ## 09-3 결측값 다루기

# ### 결측값 처리하기

# #### [Do It! 실습] 결측값 개수 구하기

# In[58]:


ebola = pd.read_csv('../data/country_timeseries.csv')

print(ebola.count())


# In[59]:


num_rows = ebola.shape[0]
num_missing = num_rows - ebola.count()
print(num_missing)


# In[60]:


import numpy as np

print(np.count_nonzero(ebola.isnull()))


# In[61]:


print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))


# In[62]:


cnts = ebola.Cases_Guinea.value_counts(dropna=False)
print(cnts)


# In[63]:


print(cnts.loc[pd.isnull(cnts.index)])


# In[64]:


print(ebola.Cases_Guinea.isnull().sum())


# #### [Do It! 실습] 결측값 대체하기

# In[65]:


print(ebola.fillna(0).iloc[:, 0:5])


# #### [Do It! 실습] 정방향 채우기

# In[66]:


print(ebola.fillna(method='ffill').iloc[:, 0:5])


# #### [Do It! 실습] 역방향 채우기

# In[67]:


print(ebola.fillna(method='bfill').iloc[:, 0:5])


# #### [Do It! 실습] 보간법으로 채우기

# In[68]:


print(ebola.interpolate().iloc[:, 0:5])


# #### [Do It! 실습] 결측값 삭제하기

# In[69]:


print(ebola.shape)


# In[70]:


ebola_dropna = ebola.dropna()
print(ebola_dropna.shape)


# In[71]:


print(ebola_dropna)


# ### 결측값이 있는 데이터 계산하기

# In[72]:


ebola["Cases_multiple"] = (
    ebola["Cases_Guinea"]
    + ebola["Cases_Liberia"]
    + ebola["Cases_SierraLeone"]
)


# In[73]:


ebola_subset = ebola.loc[
    :,
    [
        "Cases_Guinea",
        "Cases_Liberia",
        "Cases_SierraLeone",
        "Cases_multiple",
    ],
]

print(ebola_subset.head(n=10))


# In[74]:


print(ebola.Cases_Guinea.sum(skipna=True))


# In[75]:


print(ebola.Cases_Guinea.sum(skipna=False))


# ## 09-4 판다스 내장 NA 결측값

# In[76]:


scientists = pd.DataFrame(
    {
        "Name": ["Rosaline Franklin", "William Gosset"],
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "Age": [37, 61]
    }
)

print(scientists)


# In[77]:


print(scientists.dtypes)


# In[78]:


scientists.loc[1, "Name"] = pd.NA
scientists.loc[1, "Age"] = pd.NA
print(scientists)


# In[79]:


print(scientists.dtypes)  # 판다스 2.0.3 float64로 바뀜


# In[82]:


scientists = pd.DataFrame(
    {
        "Name": ["Rosaline Franklin", "William Gosset"],
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "Age": [37, 61]
    }
)

scientists.loc[1, "Name"] = np.NaN
scientists.loc[1, "Age"] = np.NaN

print(scientists.dtypes)


# In[ ]:




