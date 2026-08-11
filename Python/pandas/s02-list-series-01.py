# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:39:06 2026

@author: Solx
"""
# 리스트로 판다스의 시리즈 객체를 생성

import pandas as pd

# 리스트
lst = [ '2026-08-10', '홍길동', 3.14, 178, True, "HGD"]

# 리스트로 시리즈 객체 생성
# 인덱스: 0부터 순차적으로 지정
# 값: 리스트의 요소가 지정
sr = pd.Series(lst)
print(sr)

#%%

"""
0    2026-08-10
1           홍길동
2          3.14
3           178
4          True
5           HGD
dtype: object
"""

#%%

# 시리즈 인덱스
print(sr.index) # RangeIndex(start=0, stop=6, step=1)

# 시리즈 값
sr_values = sr.values
print(sr_values) # ['2026-08-10' '홍길동' 3.14 178 True 'HGD']

#%%

# 시리즈의 데이터 타입
print(sr.dtypes) # object

