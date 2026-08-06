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

import os
import sys

filename = "없는파일.txt"

# 존재유무?
if os.path.exists(filename) != True:
    print(f"해당 파일({filename})이 존재하지 않습니다.")
    sys.exit(-1)
    
# 폴더 or 파일 ?    
if os.path.isfile(filename) != True:
    print(f"({filename})은 파일이 아니고 폴더인 것 같습니다.")
    sys.exit(-1)
    
file = open("없는파일.txt", 'r') # 파일열기
file.close()  # 파일닫기

#%%

