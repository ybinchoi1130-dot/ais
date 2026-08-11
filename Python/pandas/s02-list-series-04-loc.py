# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:39:06 2026

@author: Solx
"""

# 판다스 시리즈
# loc: 인덱스로 값을 참조

import pandas as pd

# 리스트
lst = [ '2026-08-10', '홍길동', 3.14, 178, True, "HGD"]

# ★ 인덱스는 순번이 아니다.
# 명시적으로 인덱스(index)를 지정
sr = pd.Series(lst, index=[6,5,4,3,2,1]) # 역순으로 번호를 지정
print(sr)

#%%

# loc: 인덱스로 값을 참조
# print(sr.loc[0]) # KeyError: 0

#%%

print(sr.loc[1]) # HGD
print(sr.loc[2]) # True
print(sr.loc[3]) # 178
print(sr.loc[4]) # 3.14
print(sr.loc[5]) # 홍길동
print(sr.loc[6]) # 2026-08-10

#%%

# loc를 생략하고 인덱스로 값을 참조
# ※ 권고하지 않음
#     - 순번과 혼선
#     - 컬럼 참조와 혼선
print(sr[1]) # HGD
print(sr[2]) # True
print(sr[3]) # 178
print(sr[4]) # 3.14
print(sr[5]) # 홍길동
print(sr[6]) # 2026-08-10




