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

# 람다함수 정의와 함께 호출하는 방법
#   - 람다식을 괄호로 묶은 후에
#   - 함수를 호출하는 방식으로 괄호 안에 인자를 전달
# (lambda parameter: expression)(argument)

#%%

# [문제]
# 아래 변수 a, b, c를 람다 함수로 전달하여 가장 큰 값을 구하라.
a = 30
b = 40
c = 50
max = lambda a, b, c: a if a > b and a > c else b if b > c else c
print(f"{a}, {b}, {c} 중에 가장 큰 값은?", max(a,b,c))

#%%


