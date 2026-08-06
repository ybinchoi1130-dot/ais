# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:12:51 2024

@author: Solero
"""

# zip()
# zip(*iterable)
# 여러개로 구성된 데이터를 묶어서 리턴

#%%

a = [1,2,3]
b = [1,3,5]
c = [2,4,6]

abzip = zip(a, b, c)
ablst = list(abzip)

print(abzip) # zip object
print(ablst) # [(1, 1, 2), (2, 3, 4), (3, 5, 6)]

#%%

# 갯수가 다르면?
# 작은 갯수까지만 묶어 준다.
d = [10,11,12,13]
adlst = list(zip(a,d)) # d의 13을 제외
print(adlst) # [(1, 10), (2, 11), (3, 12)]


