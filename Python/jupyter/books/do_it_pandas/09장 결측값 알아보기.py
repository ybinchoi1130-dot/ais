#!/usr/bin/env python
# coding: utf-8

# ## 09-1 결측값이란?

# In[41]:

import numpy as np
print(np.__version__) #2.5.2


#%%

# 넘파이 버젼 : 1.x
#from numpy import NaN
#ImportError
from numpy import nan 

# In[42]:

"""
print(NaN == True)
print(NaN == 0)
print(NaN == '')
print(NaN == NaN)
print(NaN == NAN)
print(NaN == nan)
print(nan == NAN)
"""

#%%

print(np.nan)

print(nan == True)
print(nan == 0)
print(nan == '')
print(nan == np.nan)

#%%

# np.nan == np.nan이 False인 이유?
# 국제 표준(IEEE 754)을 엄격하게 따른 의도적인 설계입니다.
# - 알수 없는 것과 알수 없는 것은 비교 할 수가 없다.

# In[43]:

# 결측지 확인: 판다스의 전용함수를 이용하자
import pandas as pd

print(pd.isnull(nan))
print(pd.isnull(np.nan))


# In[44]:


print(pd.notnull(nan))
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
# 결측값
#  - na_values=[""] : 빈 문자열로
#  - keep_default_na=False : 결측값을 처리하지 마라
# 결과 : 결측값은 NaN
print(
    pd.read_csv(visited_file, na_values=[""], keep_default_na=False)
)

#%%

# "1927-01-01" -> NaN
print(
    pd.read_csv(visited_file, na_values=["1927-01-01"])
)

#%%


print(
      pd.read_csv(visited_file).
      fillna({"dated" : "1927-01-01"})
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

# 넘파이 : np.nan
num_legs = pd.Series({'goat': 4, 'amoeba': np.nan})
print(num_legs)

#%%

# 파이썬 : None
num_legx = pd.Series({'goat':4, 'amoeba': None})
print(num_legx)

# In[52]:


scientists = pd.DataFrame(
    {
        "Name": ["Rosaline Franklin", "William Gosset"],
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "missing": [None , None],
    }
)

print(scientists)


# In[53]:

# None -> object 이고 
# np.nan -> float64
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


# 컬럼추가
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


# 인덱스 재설정 : reindex
# range(2000,2010) : 2000 ~ 2009
# 결과 : 존재하지 않는 인덱스에 해당하는
#       컬럼('lifeExp')에는 Nan 값을 넣는다

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

#%%

print(ebola.shape) #122
print(num_rows)    #122



# In[60]:


import numpy as np
# 결측치가 있는 셀을 True
ebola_isnull = ebola.insull()

# True인 모든 셀의 갯수 
count_nonzero_ebola_insull = np.count_nonzero(ebola.insull())

print(np.count_nonzero(ebola.isnull())) #1214


# In[61]:

# 컬럼('cases_Guinea')에서 결측치의 갯수 : 29
print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))


# In[62]:

# dropna=False : 결측치를 포함해서 계산
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


print(ebola.ffill().iloc[:, 0:5])


# #### [Do It! 실습] 역방향 채우기

# In[67]:

# 판다스 2.1.x 이전
#print(ebola.fillna(method='bfill').iloc[:, 0:5])

# 판다스 2.1.x 이후
print(ebola.bfill().iloc[:, 0:5])
# #### [Do It! 실습] 보간법으로 채우기

# In[68]:

# 컬럼(Date)에서 오류 발생 
#print(ebola.interpolate().iloc[:, 0:5])

# 첫번째(iloc) 컬럼(Date)를 제외
print(ebola.iloc[:,1:].interpolate().iloc[:, 0:5])
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




