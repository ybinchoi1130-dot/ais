# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:39:06 2026

@author: Solx
"""

# 판다스 시리즈
# iloc: 순번로 값을 참조

import pandas as pd

# 리스트
lst = [ '2026-08-10', '홍길동', 3.14, 178, True, "HGD"]

# ★ 인덱스는 순번이 아니다.
# 명시적으로 인덱스(index)를 지정
sr = pd.Series(lst, index=range(1, len(lst) + 1))
print(sr)

#%%

# iloc: 0부터 순차적으로 접근 가능
# iloc는 index가 아니다.
print(sr.iloc[0]) # 2026-08-10
print(sr.iloc[1]) # 홍길동
print(sr.iloc[2]) # 3.14
print(sr.iloc[3]) # 178
print(sr.iloc[4]) # True
print(sr.iloc[5]) # HGD

#%%

# 시리즈의 갯수
slen = len(sr) # 6개

# 순번에 해당하는 값
for n in range(slen):
    value = sr.iloc[n]
    print(f"순번({n}) : {value}")

#%%

# 순번에 해당하는 인덱스가 가리키는 값
for n in range(slen):
    index = sr.index[n]
    value = sr.loc[index]
    print(f"순번({n}) : {index}, {value}")

#%%

# 순번에 해당하는 번호로 values의 값
for n in range(slen):
    value = sr.values[n]
    print(f"순번({n}) : {value}")

