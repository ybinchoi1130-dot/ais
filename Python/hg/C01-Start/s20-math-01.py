# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 11:33:56 2025

@author: solgits
"""

#%%

# Built-In : 내장 함수

# 절대값
print(abs(-5)) # 5
print(abs(10)) # 10

x = -5
print(abs(x))  # 5

#%%

# 거듭제곱 함수
# pow(x, y) : x의 y승
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

#%%

# TypeError: 'int' object is not iterable
# print(max(7))
print(max((7,)))

#%%

xs = 7,
print(max(xs))

#%%

ys = (7,)
print(max(ys))

#%%

al = 'a', 'b', 'x', 't'
print(max(al)) # 'x'

#%%

# 가장 작은 값을 리턴
ax = 'a', 'b', 'x', 't'
print(min(ax)) # 'a'

#%%

# 가장 작은 값을 리턴
# 문자열과 숫자를 결합
an = 'a', 'b', 'x', 't', 10, 99, 'end'
print(an)  # ('a', 'b', 'x', 't', 10, 99)
print(type(an))  # <class 'tuple'>, 튜플

# TypeError: '>' not supported between instances of 'int' and 'str'
# print(max(an))
# print(min(an))

#%%

# ASCII 코드표 참조
# 문자열은 각 자릿수끼리 코드값으로 비교한다.
st = 'Capical', 'abc', 'abx', '1234'
print(min(st)) # '1234'
print(max(st)) # 'abx'

#%%

# 반올림 : 소숫점 이하 1자리에서 반올림
print(round(3.14))  # 3
print(round(3.5))   # 4
print(round(3.44))  # 3
print(round(3.45))  # 3

#%%

# 반올림 : 소숫점 이하 2자리에서 반올림
print(round(3.45, 1))  # 3.5

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






