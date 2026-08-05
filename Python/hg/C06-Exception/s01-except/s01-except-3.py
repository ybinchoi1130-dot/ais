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
#   - 예외 종류별로 후속처리를 하기 위해서
#%%

x = 10
y = 3
z = 0

# try의 명령문들 중에서 예외가 발생하면
# 해당하는 위치에서 except로 이동하여 처리후
# 예외 구문을 빠져 나간다.
# 그러므로 예외가 발생한 위치 다음의 명령은 실행되지 않는다.
try:
    z = x / y
    file = open("./없는파일.txt", 'r') 
    print("정상처리")
except ZeroDivisionError as e:    
    print("[예외발생] 나누기 오류:", e)
except FileNotFoundError as e:
    print("[예외발생] 파일처리 오류:", e)


    
