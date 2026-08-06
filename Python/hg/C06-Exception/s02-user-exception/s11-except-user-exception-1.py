# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:01:28 2024

@author: Solero
"""

# 사용자 예외처리
# Exception : 예외처리의 기반 클래스
# Exception을 상속하여 사용자 예외 클래스를 정의
class BirdException(Exception):
    pass

#%%

# 예외발생: raise 예외클래스
# raise: 
#   - 예외를 발생 시킨다.    
#   - 함수의 리턴(return) 효과와 같다.
#   - 함수를 호출한 곳으로 돌아 간다.
def HiBird(hi):
    if hi == 'dead':
        raise BirdException("새가 죽었습니다.") # 예외발생
    print("[버드] 안녕?")
    
#%%

HiBird("잘 잤어?")    
# HiBird("dead")     # 예외발생


#%%

try:
    HiBird('dead')
except BirdException as e:
    print("[예외발생]", e)    # [예외발생] 새가 죽었습니다.
    
#%%

try:
    HiBird('Hi!')
except BirdException as e:
    print("[예외발생]", e)    # [버드] 안녕?

