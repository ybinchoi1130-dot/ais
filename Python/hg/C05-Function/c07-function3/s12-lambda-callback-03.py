# -*- coding: utf-8 -*-

# 람다함수 응용

#%%

# 파라미터
# what: 문자열
# func: 함수
# a, b: 계산 할 데이터
def calc(what, func, a, b):
    print(f"calc({what}): ", func(a, b))

#%%

# 람다함수 사용
calc("덧셈", lambda a, b: a + b, 10, 20) # 30
calc("뺄셈", lambda a, b: a - b, 10, 6)  # 4
calc("곱셈", lambda a, b: a * b, 10, 3)  # 30

