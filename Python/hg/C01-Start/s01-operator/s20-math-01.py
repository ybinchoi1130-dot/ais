# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 11:33:56 2025

@author: solgits
"""

#%%

# Built-In : 내장 수학 함수

# 절대값: abs(value)
print(abs(-5)) # 5
print(abs(10)) # 10

#%%
x = -5
y = abs(x)
print(y)  # 5

#%%

# 거듭제곱: x ** y
# 함수: pow(x, y) : x의 y승
print(pow(4, 2))  # 4의 2승은 16
print(pow(2, 3))  # 2의 3승은 8
print(pow(10, 3)) # 10의 3승은 1000

#%%

# 최대값: max(a, b, c, ...)
# 인자들 중에서 가장 큰값 하나를 찾아서 리턴
# 가변인자
print(max(5, 12))      # 12
print(max(3,10,4,0,7)) # 10
print(max(0.13, 0.10, 0.5, 4.45, 7.0)) # 7.0
print(max(3, 4, 5.1, 5.1, 4.99)) # 5.1


#%%

# TypeError: 'int' object is not iterable
# print(max(7))  # 정수값 1개
print(max((7,))) # tuple

#%%

# 정수
x7 = 7
print(type(x7), x7) # <class 'int'> 7

#%%

# tuple
xs = 7,

print(type(xs)) # <class 'tuple'>
print(max(xs))

#%%

ys = (7,)
print(type(ys)) # <class 'tuple'>
print(max(ys))

#%%

al = 'a', 'b', 'x', 't'
print(max(al)) # 'x'

#%%

# 가장 작은 값을 리턴
ax = '9', 'a', 'b', 'x', 't'
print(min(ax)) # 'a'

#%%

# 가장 작은 값을 리턴
# 문자열과 숫자를 결합
an = 'a', 'b', 'x', 't', 10, 99, 'end'
print(an)  # ('a', 'b', 'x', 't', 10, 99)
print(type(an))  # <class 'tuple'>, 튜플



#%%
# TypeError: '>' not supported between instances of 'int' and 'str'
# print(max(an))
# print(min(an))

#%%

ax = 'a', 'ab', 'b', 'x', 't', 'end'
print(max(ax))


#%%

# ASCII 코드표 참조
# 문자열은 각 자릿수끼리 코드값으로 비교한다.
st = 'Capical', 'abc', 'abx', '1234'
print(min(st)) # '1234'
print(max(st)) # 'abx'

#%%

# 반올림 : 소숫점 이하 1자리에서 반올림
print(round(3.14))  # 3
print(round(3.5))   # 4 = 3.5 + 0.5
print(round(3.44))  # 3
print(round(3.45))  # 3
print(round(3.6))   # 4 = 3.6 + 0.5

#%%

# 반올림 : 소숫점 이하 2자리에서 반올림
print(round(3.45, 1))  # 3.5
print(round(3.35, 1))  # 3.4

#%%

# 사반오입(Round Half to Even) 방식
# 끝자리가 정확히 .5로 끝날 때는 가장 가까운 짝수 방향으로 반올림합니다.
print(round(3.55, 1))  # 3.5
print(round(3.65, 1))  # 3.6
print(round(3.75, 1))  # 3.8

#%%
 
# .5로 끝나는 경우 (가장 가까운 짝수로 이동)
print(round(0.5))  # 0 (0과 1 중 짝수인 0)
print(round(1.5))  # 2 (1과 2 중 짝수인 2)
print(round(2.5))  # 2 (2와 3 중 짝수인 2)
print(round(3.5))  # 4 (3과 4 중 짝수인 4)
print(round(4.5))  # 4 (4와 5 중 짝수인 4)

#%%

# .5가 아닌 일반적인 경우 (가장 가까운 정수로 이동)
print(round(1.4))  # 1
print(round(1.6))  # 2

#%%

# 소수 둘째 자리에서 반올림하여 첫째 자리까지 남기기
print(round(1.25, 1))  # 1.2 (2와 3 중 짝수인 2)
print(round(1.35, 1))  # 1.4 (3과 4 중 짝수인 4)
print(round(1.45, 1))  # 1.4 (4와 5 중 짝수인 4)
print(round(1.55, 1))  # 1.6 (5와 6 중 짝수인 6)


#%%

from decimal import Decimal, ROUND_HALF_UP

val = Decimal('3.55').quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
print(val)  # 출력: 3.6

#%%

val = Decimal('3.65').quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
print(val)  # 출력: 3.7


#%%

x = 3.45 + 0.05
print(x) # 3.5

#%%

x = round(3.14)
y = round(3.45, 1)
print(max(x, y)) # 3.5

#%%

print(max(round(3.14), round(3.35, 1))) # max(3, 3.4) -> 3.4

#%%

# 반올림 : 
# round(값, 소숫점이하 자릿수)    
print(round(-3.14))

#%%

# 소숫점 이하 자릿수 : 음수
print(round(1234, -3)) # 1000
print(round(1534, -3)) # 2000
print(round(1634, -3)) # 2000
print(round(1934, -3)) # 2000
print(round(1994, -3)) # 2000

#%%

# 사반오입(Round Half to Even) 방식을 해결하는 방법
# 사용자 함수를 정의
import math

def custom_round(val, n=0):
    # n 자릿수만큼 10의 거듭제곱을 곱한 뒤 0.5를 더하고 내림 처리
    multiplier = 10 ** n
    return math.floor(val * multiplier + 0.5) / multiplier

print(custom_round(3.55, 1))  # 3.6
print(custom_round(2.5))      # 3.0
print(custom_round(1.25, 1))  # 1.3

#%%

import math

print(math.floor(3.55)) # 3
print(math.floor(2.5))  # 2
print(math.floor(1.25)) # 1





