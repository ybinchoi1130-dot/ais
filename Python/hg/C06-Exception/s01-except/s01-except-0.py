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
#
# (PowerShell)
# python s01-except-0.py <숫자> <숫자>
# 예시: python s01-except-0.py 4 2
# echo $LASTEXITCODE -> exit(code) 확인
# echo $?            -> 성공유무: True/False

# (Windows CMD)
# python s01-except-0.py <숫자> <숫자>
# 예시: python s01-except-0.py 4 2
# echo %ERRORLEVEL%  

# Linux, MacOS
# python s01-except-0.py <숫자> <숫자>
# 예시: python s01-except-0.py 4 2
# echo $?


#%%

import sys

argv = sys.argv


if len(sys.argv) < 3:
    print("사용법: python s01-except-0.py <숫자> <숫자>")
    sys.exit(-1)


filename = sys.argv[0] # 파이썬 코드 파일이름
x = int(sys.argv[1])   # 연속적으로 기술된 인자1
y = int(sys.argv[2])   # 연속적으로 기술된 인자2

print(f"[{filename}] {x}, {y}")

if y == 0:
    print('0으로 나눌 수 없습니다.')
    sys.exit(-2) # 프로그램을 종료

z = int(x / y)
    
print(f"[{filename}] {z} = {x} / {y}")
sys.exit(z) 

