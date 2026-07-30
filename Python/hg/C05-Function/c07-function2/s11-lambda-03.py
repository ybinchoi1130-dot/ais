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

x = 10
y = 3
print(f"{x} * {y} ->", (lambda a, b : a * b)(x, y))
print(f"{x} ** {y} ->", (lambda a, b : a ** b)(x, y))

#%%

print(f"{x} * {y} ->", (lambda x, y : x * y)(x, y))

