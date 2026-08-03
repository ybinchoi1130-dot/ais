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

gv = 10

print("gv:", 100)
#%%

#%%

# 일반함수: 전역변수(gv)를 변경
def max(a, b):
    global gv   # 전역변수(gv)를 변경하겠다는 선언
    gv = a + b  # 전역변수(gv)를 변경
    if a > b:
        return a
    else:
        return b

#%%
# max2 = lambda a, b: a if (a + gv) > b else b
max_lambda = lambda a, b: (globals().update({'gv': a + b}), a if a > b else b)[1]
print(max_lambda(10, 20)) # 20 

#%%
# 람다함수: 호출
x = 1
y = 100
z = max(x, y) 

print(f"global gv:", gv)
print(f"값 {x}와 {y} 중에 큰 값은? {z}")

#%%

