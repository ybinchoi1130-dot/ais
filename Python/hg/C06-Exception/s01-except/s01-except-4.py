# -*- coding: utf-8 -*-

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

#%%

x = 10
y = 0
z = 0

# 다중의 예외를 하나의 예외 블록에서 처리
try:
    z = x / y
    file = open("./없는파일.txt", 'r') 
    print("정상처리")
except (ZeroDivisionError, FileNotFoundError) as e:    
    print("[예외발생]", e)
    print("프로그램이 정상적으로 처리되지 않았습니다.")
    print("다시 시도해 보세요.")

    
