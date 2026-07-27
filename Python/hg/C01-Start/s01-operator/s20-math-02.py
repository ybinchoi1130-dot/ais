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

#%%
# 원주율
print(pi) # 3.141592653589793

#%%

# 내림: floor(x)
# x 값보다 작은 정수를 리턴
fl1 = floor(4.99)
fl2 = floor(0.12)
fl3 = floor(5)
print(fl1) # 4
print(fl2) # 0
print(fl3) # 5

#%%

# 소숫점 이하 절사
print(int(4.99)) # 4
print(int(0.12)) # 0
print(int(2.01)) # 2

#%%

# 올림: ceil(x)
# x 값보다 큰 정수
print(ceil(3.14)) # 4
print(ceil(3.35)) # 4
print(ceil(0.99)) # 1

#%%

def my_ceil(x: float) -> int:
    int_x = int(x)
    # 소수점이 남아있고 양수인 경우에만 1을 더해줍니다.
    if x > int_x: 
        return int_x + 1
    return int_x

# 테스트
print(my_ceil(3.2))   #  4
print(my_ceil(3.0))   #  3
print(my_ceil(-3.2))  # -3
print(my_ceil(-3.0))  # -3

#%%

x = 3.2
int_x = int(x) # 3
y = int_x + 1 if x > int_x else int_x
print(y) # 4

#%%

x = 3.0
int_x = int(x) # 3
y = int_x + 1 if x > int_x else int_x
print(y) # 3



#%%

# 제곱근: sqrt(x)
# 제곱해서 x가 되는 값
print(sqrt(16)) # 4.0
print(sqrt(4))  # 2.0

#%%

import math

# math.log(x[, base])
# With one argument, return the natural logarithm of x (to base e).
# With two arguments, return the logarithm of x to the given base, 
# calculated as log(x)/log(base).
# 로그: log(x[, base])

# 자연상수
print(math.e)  # 2.718281828459045

#%%

# 자연상수(e)를 밑으로 한 값
print(log(math.e)) # 1.0

#%%

print(log(math.e, math.e)) # 1.0

#%%

# 2의 몇승을 해야 8이 되냐?
print(log(8, 2)) # 3.0







