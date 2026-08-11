# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:39:06 2026

@author: Solx
"""
# filename : s02-list-series-01.py
# 리스트로 판다스의 시리즈 객체를 생성
# 시리즈의 인덱스를 리스트로 지정

import pandas as pd

# 리스트
inx = [ '날짜', '이름', '원주율', '신장', '생존유무', '이니셜']
lst = [ '2026-08-10', '홍길동', 3.14, 178, True, "HGD"]

# 리스트로 시리즈 객체 생성
# 인덱스: 0부터 순차적으로 지정
# 값: 리스트의 요소가 지정

# 명시적으로 인덱스(index)를 지정
sr = pd.Series(lst, index=inx)
print(sr)

#%%

"""
날짜             2026-08-10
이름             홍길동
원주율           3.14
신장             178
생존유무         True
이니셜           HGD
dtype: object
"""

#%%

# 시리즈 인덱스
print(sr.index) # Index(['날짜', '이름', '원주율', '신장', '생존유무', '이니셜'], dtype='str')

#%%
# 시리즈 값
sr_values = sr.values
print(sr_values) # ['2026-08-10' '홍길동' 3.14 178 True 'HGD']

#%%

# 시리즈의 데이터 타입
print(sr.dtypes) # object

