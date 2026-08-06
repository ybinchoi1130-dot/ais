# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:31:38 2024

@author: Solero
"""

# random(), randint()
# 난수: 규칙이 없는 임의의 수

#%%

# random() : 0~1.0 사이의 값, 1.0보다 작은값

import random

# 난수를 10개 발생
for n in range(10):
    x = random.random()
    print(x)
    
#%%

# 1부터 6까지 숫자를 20번 발생시켜라
for n in range(20):
    x = random.random()
    y = x * 6
    z = int(y) + 1
    print(f"{z}: {x:.5f}, {y:.5f}")
    
    
#%%

# 10부터 20까지 숫자를 20번 발생시켜라
# 소숫점 5자리 이하 버리고 발생된 난수를 출력 :
s = 10 # 시작값
e = 20 # 마지막값
m = 20 # 발생 횟수

for n in range(m):
    x = random.random()  # 난수
    y = x * (e-s+1)      # 경우의 갯수로 환산(11개)
    z = int(y) + s       # 정수
    rx = round(x, 5)     # 소숫점 5자리(반올림)
    print(f"{z:2d}: {rx}, {y:.5f}")
    
#%%

# [문제] 
# 1부터 45까지 난수를 발생시켜 6개의 충돌되지 않는 조합을 만들어라.
import random

ls = 1     # 시작값
le = 45    # 종료값
lc = 6     # 갯수
lotto = [0,0,0,0,0,0] # 총 6개의 난수를 저장할 리스트

nx = 0
n = 0
while True:
    if n >= lc: # n이 6보다 크거나 같으면 반복문 탈출
        break
    x = random.random()  # 난수
    y = x * (le-ls+1)    # 경우의 갯수로 환산(45개)
    z = int(y) + ls      # 정수
    rx = round(x, 5)     # 소숫점 5자리(반올림)
    print(f"[{nx}] {z:2d}: {rx}, {y:.5f}")
    if z not in lotto:   # 동일한 번호 확인
        lotto[n] = z
        n += 1
        
    nx += 1
        
print("lotto:", lotto)        
    
    



    
    