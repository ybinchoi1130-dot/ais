# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:54:19 2024

@author: Solero
"""

# 예외처리(Exception)
# try ~ except
# 
# 예외:
#   - 잘못된 동작을 했을 때 
#   - 실행할 때 발생
#   - 프로그램이 종료
# 
# 예외처리:
#   - 비정상적 상황으로 인해서 프로그램이 중단없이 실행 가능하도록 처리

# Exception: 모든 예외 처리 클래스의 최상위 클래스

#%%

class BirdException(Exception):
    def __init__(self, errno,msg='',why=''):
        super().__init__(msg,why)
        self.errno =errno
        
    def error(self):
        return self.errno

#%%
#예외 발생
def Hibird(hi):
    if hi == 'dead':
        raise BirdException(-1,"새가 죽었습니다.","사고")
    print("[버드] 안녕")

Hibird("잘 잤어?")
#함수를 통해서 클래스 객채를 리턴받음
try:
    Hibird("dead")
except BirdException as e:
    print("[예외발생]",e)
    print("errno:",e.error())
#%%
#클래스를 직접 생성
be = BirdException(-9,"새가 추락했습니다.","졸음")
print("[함수리턴]",be)
print("errno:",be.error())