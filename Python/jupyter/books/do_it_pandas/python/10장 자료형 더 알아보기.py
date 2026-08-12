#!/usr/bin/env python
# coding: utf-8

# ## 10-1 자료형 살펴보기

# In[29]:


import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")


# In[30]:


print(tips.dtypes)


# ## 10-2 자료형 변환하기

# #### [Do It! 실습] 문자열로 변환하기

# In[32]:


tips['sex_str'] = tips['sex'].astype('str')
print(tips.dtypes)


# #### [Do It! 실습] 숫자로 변환하기

# In[18]:


tips['total_bill'] = tips['total_bill'].astype('str') 
print(tips.dtypes)


# In[19]:


tips['total_bill'] = tips['total_bill'].astype('float') 
print(tips.dtypes)


# #### [Do It! 실습] 숫자형으로 변환하는 to_numeric() 메서드 사용하기

# In[20]:


tips_sub_miss = tips.head(10).copy()
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'

print(tips_sub_miss)


# In[21]:


print(tips_sub_miss.dtypes)


# In[22]:


#pd.to_numeric(tips_sub_miss['total_bill'])  # 오류


# In[23]:


tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'],
                                            errors='ignore')

print(tips_sub_miss)


# In[24]:


print(tips_sub_miss.dtypes)


# In[25]:


tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'],
                                            errors='coerce')
print(tips_sub_miss)


# In[26]:


print(tips_sub_miss.dtypes)


# ## 10-3 범주형 데이터

# #### [Do It! 실습] 범주형으로 변환하기

# In[27]:


tips['sex'] = tips['sex'].astype('str') 
print(tips.info())


# In[28]:


tips['sex'] = tips['sex'].astype('category')
print(tips.info())


# In[ ]:




