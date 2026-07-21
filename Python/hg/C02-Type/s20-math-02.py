# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 11:33:56 2025

@author: solgits
"""

#%%

# 수학함수 : math
# 모듈을 임포트
import math
print(math.pi) # 3.141592653589793

#%%

# 모듈에 속한 모든 함수, 변수, 객체들을 임포트
# 모듈 이름을 생략하여 사용
from math import *

# 원주율
print(pi) # 3.141592653589793

#%%

# 내림: floor(x)
# x 값보다 작은 정수
fl1 = floor(4.99)
fl2 = floor(0.12)
fl3 = floor(5)
print(fl1) # 4
print(fl2) # 0
print(fl3) # 5

#%%

# 올림: ceil(x)
# x 값보다 큰 정수
print(ceil(3.14)) # 4
print(ceil(3.35)) # 4
print(ceil(0.99)) # 1

#%%

# 제곱근: sqrt(x)
# 제곱해서 x가 되는 값
print(sqrt(16)) # 4.0
print(sqrt(4))  # 2.0

#%%

# math.log(x[, base])
# With one argument, return the natural logarithm of x (to base e).
# With two arguments, return the logarithm of x to the given base, 
# calculated as log(x)/log(base).
# 로그: log(x[, base])

print(math.e)  # 2.718281828459045

#%%

# 자연상수(e)를 밑으로 한 값
print(log(math.e)) # 1.0

#%%

# 2의 몇승을 해야 8이 되냐?
print(log(8, 2)) # 3.0







