# -*- coding: utf-8 -*-

# 함수(Function)
# 1. 함수는 호출하기 전에 정의가 되어 있어야 한다.
# 2. 함수의 리턴값이 없는 경우 리턴값을 받으면 None이다.
# 3. 함수 정의에서 리턴값이 없으면 return을 생략하면 된다.
# 4. 함수 정의에서 파라미터가 없으면 함수() 형태로 파라미터를 생략한다.
#
# 함수 장점:
#  1. 모듈화: 기능별로 분리
#  2. 블랙박스화: 처리과정보다는 결과   
#  3. 코드의 재사용
#
# 매개변수와 인자
# 매개변수(parameter) : 함수에 입력으로 전달된 값을 받는 변수, 함수 정의
# 인자(arguments) : 함수를 호출할 때 전달하는 입력값, 함수 호출
"""
함수정의

def 함수명(파라미터):
    실행문
    return 리턴값
"""

#%%

# 함수정의: 한 번만 기술한다.
# 함수이름: hello
# 파라미터: 문자열, 출력횟수
# 리턴밸류: None
def hellocnt(msg, cnt): 
    print(f"[hellox] msg({msg}), cnt({cnt})")
    for n in range(cnt):
        print(f"[{n}]: {msg}")
        
#%%

# 함수호출
# 인자는 순서대로 함수의 파라미터로 전달된다.
# hellocnt(10, "Hello, World.") # 인자의 순서를 바꾸면 오류가 나올 수 있다.

#%%

hellocnt("Hello, World.", 10)

#%%

# 함수 정의에 리턴값이 없는데 
# 함수 호출에서 리턴을 받으면?
# 리턴: None
rt = hellocnt("Hello, World.", 10)
print("리턴:", rt) # None

#%%

# 함수가 아닌 곳에서 리턴을 하면?
# SyntaxError: 'return' outside function
for n in range(10):
    print("Hello")
    return 



 


