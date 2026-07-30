# -*- coding: utf-8 -*-

# 함수 : 람다(lambda)
# inline 함수, 익명함수
# 함수형 프로그래밍(functional programming)에 활용
#
# 정의와 선언이 동시에 이루짐
# 정의선언: 함수변수 = lambda 파라미터 : 표현식
# 함수호출: 함수변수(파라미터)
# 결과리턴: 표현식의 처리 결과를 리턴

#%%

# 일반함수: 정의
# 두 인자(a, b)를 비교해서 큰 값을 리턴
def max(a, b):
    return a if a > b else b

#%%

# 함수 이름에 None을 할당하면 더 이상 함수를 호출할 수 없다.
max = None

#%%

# 일반함수: 호출
# TypeError: 'NoneType' object is not callable
max(10,20) 

#%%



