# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:06:41 2024

@author: Solero
"""

# map()
# map(func, iterable)
# 데이터의 각 요소에 함수(func)를 적용한 결과를 리턴

#%%

# 람다함수

lst = [1,3,5,7,9]

# 각 요소에 2를 곱한 결과를 리턴
lstm = map(lambda x: x * 2, lst)
lstx = list(lstm)

print(lstm) # map object

# 입력한 데이터의 갯수와 처리 결과의 갯수가 동일
print(lstx) # [2, 6, 10, 14, 18]