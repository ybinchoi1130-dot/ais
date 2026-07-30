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
    return a if a > b else b # 조건부 표현식(conditional expression)
    """
    if a > b:
        return a
    else:
        return b
    """
#%%

# 일반함수: 호출
a = 10
b = 20
c = max(a,b) 
print(f"값 {a}와 {b} 중에 큰 값은? {c}")

#%%

# 람다함수: 정의
# 파라미터: a, b
# 리턴: 인라인 처리 결과    
# 람다함수변수: lambda_max
lambda_max = lambda a, b: a if a > b else b

#%%
# 람다함수: 호출
x = 99
y = 98
z = lambda_max(x, y) 
print(f"값 {x}와 {y} 중에 큰 값은? {z}")

#%%

print(f"값 {x}와 {y} 중에 큰 값은? {lambda_max(x,y)}")


#%%

print(f"값 {55}와 {56} 중에 큰 값은? {lambda_max(55,56)}")

