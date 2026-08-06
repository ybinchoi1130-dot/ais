# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:06:03 2024

@author: Solero
"""

# 내장함수(Built-In Function)
# 파이썬을 설치할 때 기본적으로 제공되는 모듈

# enumerate()

lst = ['body', 'foo', 'bar']

#%%

# 리스트에서 요소를 하나씩 꺼내줌
for val in lst:
    print(val)
    
#%%

# 리스트의 인덱스 처리
for n in range(len(lst)): # n: 0,1,2
    val = lst[n]  # 리스트에 인덱스를 통해서 값을 참조
    print(f"인덱스({n}), ({val})")
    
#%%

# enumerate를 통해서 인덱스와 요소의 값을 동시에 처리
for n, val in enumerate(lst):
    print(f"인덱스({n}), ({val})")
    
    