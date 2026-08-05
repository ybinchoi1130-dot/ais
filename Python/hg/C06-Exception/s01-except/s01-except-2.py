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

# 파일을 읽기용으로 오픈

# FileNotFoundError: [Errno 2] No such file or directory: '없는파일.txt'
file = open("없는파일.txt", 'r') 

#%%

try:
    file = open("./없는파일.txt", 'r') 
except FileNotFoundError as ex:
    print("[예외발생] ", ex)
    print("존재하지 않는 파일입니다.")

    
