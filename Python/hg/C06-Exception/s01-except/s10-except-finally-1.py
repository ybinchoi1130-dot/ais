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

# finally가 필요한 경우?
# 함수에서 리턴과 같이 중간에 처리가 분기되는 경우
# 필수적으로 처리를 해야할 루틴이 있는 경우

def compute(x, y):
    
    z = 0
    
    try:
        if x < 0 or x > 100:
            return -1
        z = x / y
    except:
        print("예외발생")
    else: # 예외가 발생되지 않으면 처리
        print("정상처리")
    finally: # 예외에 관계없이 맨 마지막에 무조건 처리
        print("finally:작업종료")
        
    return z        

    
#%%

print(compute(10, 3))

#%%

print(compute(-1, 3))

#%%

print(compute(10, 0))


