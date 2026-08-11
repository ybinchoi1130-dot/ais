# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:39:06 2026

@author: Solx
"""

# 판다스 시리즈
# 멀티 인덱스(MultiIndex)

import pandas as pd

# 리스트
lst = [ '홍길동', 34, 178, 80]

sr = pd.Series(lst, index=['이름', '나이', '신장', '체중'])
print(sr)

#%%

# 인덱스로 하나의 요소를 참조
# 요소의 타입: 참조한 요소에 해당하는 자료형
name1 = sr['이름']     # 권고하지 않는 사용 방법
name2 = sr.loc['이름']
age   = sr.loc['나이']
print(type(name1), name1) # <class 'str'> 홍길동
print(type(name2), name2) # <class 'str'> 홍길동
print(type(age), age)     # <class 'int'> 34

#%%

# KeyError: 'key of type tuple not found and not a MultiIndex'
# name_age = sr['이름', '나이']

#%%

# IndexingError: Too many indexers
# name_age = sr.loc['이름', '나이']


#%%

# 다중으로 인덱스를 선택
# 리스트에 선택할 인덱스 목록을 지정
# 결과: 시리즈

# '이름' 1개를 선택
names = sr[ ['이름'] ]
print(type(names)) # <class 'pandas.Series'>
print(names)       # 이름    홍길동

#%%

# '이름', '나이' 2개를 선택
name_age = sr[ ['이름','나이'] ]
print(type(name_age)) # <class 'pandas.Series'>
print(name_age)

#%%

name_age2 = sr.loc[ ['이름','나이'] ]
print(type(name_age2)) # <class 'pandas.Series'>
print(name_age2)

#%%

ng_index = ['이름','나이']  # list
ng_value = sr[ng_index]
print(type(ng_value)) # <class 'pandas.Series'>
print(ng_value)

#%%

# iloc로 다중 선택
# 0:이름, 3:체중, 2:신장
iloc_name_age = sr.iloc[ [0,3,2] ]
print(type(iloc_name_age)) # <class 'pandas.Series'>
print(iloc_name_age)

#%%

"""
<class 'pandas.Series'>
이름    홍길동
체중     80
신장    178
dtype: object
"""

