# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:01:28 2024

@author: Solero
"""

# 사용자 예외처리
# Exception : 예외처리의 기반 클래스
class BirdException(Exception):
    def __init__(self, errno, msg='', why=''):
        super().__init__(msg, why)
        self.errno = errno
        
    def error(self):
        return self.errno        

#%%

# 예외발생: raise 예외클래스
def HiBird(hi):
    if hi == 'dead':
        raise BirdException(-1, "새가 죽었습니다.", "사고") # 예외발생
    print("[버드] 안녕?")
    
#%%

try:
    HiBird('dead')
except BirdException as e:
    print("[예외발생]", e)    
    print("args: type=", type(e.args))
    for arg in e.args:
        print(f"\t -> {arg}")
    print("errno:", e.error())

#%%




