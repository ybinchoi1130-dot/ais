# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:46:47 2026

@author: Solx
"""

#%%
import pandas as pd
print(pd.__version__)

#%%

# dict
dx = { 'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four' }

# 시리즈(Series): 1차원
# 인덱스(index)와 값(value)로 구성
# dict.key   -> pandas.Series.index
# dict.value -> pandas.Series.values
sr = pd.Series(dx)
print(type(sr)) # <class 'pandas.Series'>
print(sr)

#%%

# 판다스 시리즈의 인덱스 속성을 참조
sr_index = sr.index
print(sr_index) # Index(['a', 'b', 'c', 'd'], dtype='str')

#%%

# 판다스 시리즈의 값 속성을 참조
sr_values = sr.values
print(sr_values) # ['one', 'two', 'three', 'four']


