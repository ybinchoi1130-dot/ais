# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:27:20 2024

@author: Solero
"""

# filter()
# 반복 가능한 데이터를 지정된 함수를 통해서 필터링

#%%

# 리스트에서 양수만 필터링해서 리턴하는 함수
def positive(lst):
    result = [] # 로컬변수
    for i in lst:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,7,9,-99])) # [1, 2, 7, 9]

#%%

x = 10
b = x > 0
print(b) # True

#%%

# x가 0보다 크면 True, 작거나 같으면 False
def posfunc(x):
    return x > 0 

lst1 = [1,-3,2,0,-5,7,9,-99]
lst2 = [-1,-2,-99]
fr1 = filter(posfunc, lst1) # filter object
fr2 = filter(posfunc, lst2) # filter object
print(fr1)
print(fr2)

#필터(filter) 객체를 리스트(list) 객체로 변환
# 필터객체의 결과(참) -> 리스트
lst1 = list(fr1)
lst2 = list(fr2)
print(lst1) # [1, 2, 7, 9]
print(lst2) # []
#%%
#리스트 =filter(롤백함수, 리스트)
def filterx(func,lst):
    result = []
    for x in lst:
        if func(x):
            result.append(x)
        return result


#%%

lst = [1,-3,2,0,-5,7,9,-99]

# 람다함수 이용
lstx = list(filter(lambda x: x > 0, lst))
print(lstx) # [1, 2, 7, 9]

