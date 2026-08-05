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

x = 10
y = 0
z = 0

try:
    z = x / y
except:
    print("예외발생")
else: # 예외가 발생되지 않으면 처리
    print("정상처리")
finally: # 예외에 관계없이 맨 마지막에 무조건 처리
    print("작업종료")

    
