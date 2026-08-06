# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:01:28 2024

@author: Solero
"""

# 사용자 예외처리 정의
# Exception : 예외처리의 기반 클래스
class BirdException(Exception):
    def __init__(self, errno, msg='', why=''):
        super().__init__(msg, why) # Excep[]
        self.errno = errno
        
    def error(self):
        return self.errno        

#%%

# 예외발생: raise 예외클래스
def HiBird(hi):
    if hi == 'dead':
        return BirdException(-1, "새가 죽었습니다.", "사고") # 예외발생
    print("[버드] 안녕?")
    
#%%

# 함수를 통해서 클래스 객체를 리턴 받음
e = HiBird('dead')
print("[함수리턴]", e)    
print("errno:", e.error())

#%%

# 클래스를 직접 생성
be = BirdException(-9, "새가 추락했습니다.", "줄음")
print("[함수리턴]", be)    
print("errno:", be.error())

for arg in be.args:
    print(arg)


#%%


