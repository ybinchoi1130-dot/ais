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

# Exception: 모든 예외 처리 클래스의 최상위 클래스
# pass: 블록안에 기술하여 아무 처리도 하지않고 지나침(건너뜀)

#%%

x = 10
y = 0
z = 0

# 예외가 발생되고 확인이나 통보를 하지 않고 
# 그냥 무시하고 정상적인 것처럼 처리를 진행
try:
    z = x / y
    file = open("./없는파일.txt", 'r') 
    print("정상처리")
except:
    pass # 오류 회피
    
print("작업종료")

#%%

def space():
    pass


class Space:
    pass

    
#%%

try:
    pass
except:
    pass

#%%

