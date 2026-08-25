#!/usr/bin/env python
# coding: utf-8

# ## 06-1 간단한 함수 만들기

# #### [Do It! 실습] 사용자 함수 만들기

# In[1]:


def my_sq(x):
    return x ** 2


# In[2]:


def avg_2(x, y):
    return (x + y) / 2


# In[3]:


def avg_2(x, y):
    """두 숫자의 평균을 구하는 함수
    """
    return (x + y) / 2


# In[4]:


my_calc_1 = my_sq(4)
print(my_calc_1)


# In[5]:


my_calc_2 = avg_2(10, 20)
print(my_calc_2)


# ## 06-2 apply() 메서드 사용하기

# #### [Do It! 실습] 데이터프레임에 함수 적용하기

# In[6]:


import pandas as pd

df = pd.DataFrame({"a": [10, 20, 30], 
                   "b": [20, 30, 40]})
print(df)


# In[7]:


print(df['a'] ** 2)


# ### 시리즈에 함수 적용하기

# #### [Do It! 실습] 시리즈에 함수 적용하기

# In[8]:


print(type(df['a']))


# In[9]:


print(type(df.iloc[0]))


# In[10]:


sq = df['a'].apply(my_sq)
print(sq)


# #### [Do It! 실습] 사용자 함수 만들어 데이터프레임에 적용하기

# In[11]:


def my_exp(x, e):
    return x ** e


# In[12]:


cubed = my_exp(2, 3)

print(cubed)


# In[13]:


# my_exp(2)  # 오류


# In[14]:


ex = df['a'].apply(my_exp, e=2)
print(ex)


# In[15]:


ex = df['a'].apply(my_exp, e=3)
print(ex)


# ### 데이터프레임에 함수 적용하기

# In[16]:


df = pd.DataFrame({"a": [10, 20, 30], 
                   "b": [20, 30, 40]})
print(df)


# In[17]:


def print_me(x):
    print(x)


# #### [Do It! 실습] 열 단위로 함수 적용하기

# In[18]:


df.apply(print_me, axis=0)


# In[19]:


print(df['a'])


# In[20]:


print(df['b'])


# In[21]:


def avg_3(x, y, z):
    return (x + y + z) / 3


# In[22]:


# print(df.apply(avg_3))  # 오류


# In[23]:


def avg_3_apply(col):
    x = col[0]
    y = col[1]
    z = col[2]
    return (x + y + z) / 3


# In[24]:


print(df.apply(avg_3_apply))


# #### [Do It! 실습] 행 단위로 함수 적용하기

# In[25]:


# print(df.apply(avg_3_apply, axis=1))  # 오류


# In[26]:


def avg_2_apply(row):
    x = row[0]
    y = row[1]
    return (x + y) / 2


# In[27]:


print(df.apply(avg_2_apply, axis=1))


# ## 06-3 람다 함수 사용하기 

# #### [Do It! 실습] 데이터프레임에 람다 함수 사용하기

# In[28]:


df = pd.DataFrame({'a': [10, 20, 30],
                   'b': [20, 30, 40]})
print(df)


# In[29]:


def my_sq(x):
    return x ** 2

df['a_sq'] = df['a'].apply(my_sq)
print(df)


# In[30]:


df['a_sq_lamb'] = df['a'].apply(lambda x: x ** 2)
print(df)


# ## 06-4 벡터화된 함수 사용하기

# #### [Do It! 실습] 벡터화된 함수 사용하기

# In[31]:


df = pd.DataFrame({"a": [10, 20, 30], 
                   "b": [20, 30, 40]})
print(df)


# In[32]:


def avg_2(x, y):
    return (x + y) / 2


# In[33]:


print(avg_2(df['a'], df['b']))


# In[34]:


import numpy as np

def avg_2_mod(x, y):
    if (x == 20):
        return(np.NaN)
    else:
        return (x + y) / 2


# In[35]:


# print(avg_2_mod(df['a'], df['b']))  # 오류


# In[36]:


print(avg_2_mod(10, 20))


# In[37]:


print(avg_2_mod(20, 30))


# ### 넘파이와 넘바로 벡터화하기

# #### [Do It! 실습] 넘파이로 벡터화하기

# In[38]:


import numpy as np

avg_2_mod_vec = np.vectorize(avg_2_mod)


# In[39]:


print(avg_2_mod_vec(df['a'], df['b']))


# In[40]:


@np.vectorize
def v_avg_2_mod(x, y):
    if (x == 20):
        return(np.NaN)
    else:
        return (x + y) / 2

print(v_avg_2_mod(df['a'], df['b']))


# #### [Do It! 실습] 넘바로 벡터화하기

# In[41]:


import numba

@numba.vectorize
def v_avg_2_numba(x, y):
    if (int(x) == 20):
        return(np.NaN)
    else:
        return (x + y) / 2


# In[42]:


# print(v_avg_2_numba(df['a'], df['b']))  # 오류


# In[43]:


print(v_avg_2_numba(df['a'].values, df['b'].values))


# In[ ]:




