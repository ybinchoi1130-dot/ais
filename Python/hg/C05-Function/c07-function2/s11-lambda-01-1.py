# -*- coding: utf-8 -*-

# 함수 : 람다(lambda)
# inline 함수, 익명함수
# 함수형 프로그래밍(functional programming)에 활용
#   - 부작용의 최소화
#   - 부작용: 함수 안에서 외부의 상태에 영향을 미치는 행위
#   - 함수형: 처리가 항상 동일해야 한다.
#
# 정의와 선언이 동시에 이루짐
# 정의선언: 함수변수 = lambda 파라미터 : 표현식
# 함수호출: 함수변수(파라미터)
# 결과리턴: 표현식의 처리 결과를 리턴

#%%

printx = print

#%%

print = lambda a, b: a if a > b else b

#%%
# 람다함수: 호출
x = 99
y = 98
z = print(x, y) 

printx(f"값 {x}와 {y} 중에 큰 값은? {z}")

#%%

