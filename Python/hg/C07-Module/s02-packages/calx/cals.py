# -*- coding: utf-8 -*-

# 모듈명 : cals.py

# 모듈(module)
# 일반적으로 컴퓨터 소프웨어에서는 기능의 단위
# 파이썬에서 함수나 변수, 클래스들을 모아 놓은 파이썬 코드 파일

#%%

# 변수
PI = 3.141592

#%%
# 함수
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

#%%

# 모듈 테스트
# __name__ : 파이썬 시스템 변수
# __name__("__main__") : 해당 모듈이 직접 독립적으로 실행
# __name__("cals") : 종족적인 모듈로서 실행

print(f"[cals.py] __name__ : {__name__}")


if __name__ == "__main__":
    print(f"[cals.py] __name__ : {__name__}")
    
    a = 10
    b = 20
    print(f"더하기({a} + {b}): ", add(a,b))
    print(f"  빼기({b} - {a}): ", sub(b,a))

