# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 15:01:10 2025

@author: solgits
"""
# 수학함수
from  math import floor

# 랜덤(random): 난수
from random import random, randint, randrange

#%%%

# 0이상 1미만의 실수인 난수 생성
# 0 <= random() < 1
r = random()
print(r)

#%%

# [문제1]
# 1부터 6까지의 경우의 수를 난수 함수로 생성하라.
# 단: random() 함수를 사용하라.

# 난수 발생
rn = random()
print('난수발생:', rn)

# 경우의 수 만듦
rx = rn * 6
print('6 가지경우의 수:', rx)

#%%
# 경우의 수 정리
rt = floor(rn * 6)
print(rt)

# 시작값 지정
sx = rt + 1
print('주사위 값:', sx)

#%%

# [문제2]
# 10부터 20까지의 경우의 수를 난수 함수로 생성하라.
# 단: random() 함수를 사용하라.

rmin = 10 # 최솟값
rmax = 20 # 최댓값
rx = rmax - rmin + 1
rn = random()
rt = rn * rx + rmin
rr = floor(rt)

print("최솟값:", rmin)
print("최댓값:", rmax)
print("난수값:", rn)
print("최종값:", rt)
print("보정값:", rr)

#%%

# randint(시작값, 종료값)
# 정수 난수를 발생
rmin = 10 # 최솟값
rmax = 20 # 최댓값
rn = randint(rmin, rmax)

print("최솟값:", rmin)
print("최댓값:", rmax)
print("보정값:", rn)

#%%

# randrange(시작값, 종료값)
# 정수 난수를 발생
# 종료값 미포함
rmin = 10 # 최솟값
rmax = 20 # 최댓값
rn = randrange(rmin, rmax + 1)

print("최솟값:", rmin)
print("최댓값:", rmax)
print("보정값:", rn)















