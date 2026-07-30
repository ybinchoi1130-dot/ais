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

# 일반함수:
# 덧셈용 함수
def add(a, b):
    return a + b

# 뺄셈용 함수
def sub(a, b):
    return a - b

# 곱셈용 함수
def mul(a, b):
    return a * b


#%%

# 일반함수 사용
calc("덧셈", add, 10, 20) # 30
calc("뺄셈", sub, 10, 6)  # 4
calc("곱셈", mul, 10, 3)  # 30
    

#%%


