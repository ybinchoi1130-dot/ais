# -*- coding: utf-8 -*-

# 함수(Function)

# [문제]
# 함수를 이용하여 사칙연산 계산기를 만들라.
# 계산기능: 
#   - 더하기, 빼기, 나누기, 곱하기, 나머지, 제곱
#   - 총합누적, 평균
#   - 히스토리(이력)

#%%

# 전역변수(global variable)
total = 0   # 총합누적
count = 0   # 연산횟수

#%%

# 더하기
def plus(a, b):
    return a + b

#%%

# 빼기
def sub(a, b):
    return a - b

#%%

# 곱하기
def mul(a, b):
    return a * b

#%%

# 나누기(정수 나누기)
def div(a, b):
    return a // b

#%%

# 나머지
def sur(a, b):
    return a % b

#%%

# 제곱
def pow(a, b):
    return a ** b

#%%

# 계산기
# 로컬변수: 함수 안에서 선언된 변수(a, op, b, c)
def calc(a, op, b):
    if op == '+':
        c = plus(a, b)
    elif op == '-':
        c = sub(a, b)
    elif op == '*':
        c = mul(a, b)
    elif op == '/':
        c = div(a, b)
    elif op == '%':
        c = sur(a, b)
    elif op == '**':
        c = pow(a, b)
    else:
        return 0
        
    # 전역변수를 함수내부에서 변경하려면 global 선언
    global total
    global count
    
    # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    # global를 선언하지 않고 전역변수를 수정하려고 하면 로컬변수에서 찾음
    # 누적
    count += 1 # 연산횟수 누적
    total += c # 연산결과 누적
    return c   # 단위연산 결과 리턴

#%%

# 총합
# 전역변수(total)를 수정하지 않고 참조만 하면 global로 선언할 필요가 없다.
def tot():
    return total  

# 평균
def avg():
    return tot() / count

#%%

calc(10, '+', 20)      # 30    
calc(2,  '*', 4)       # 8
calc(10, '/', 2)       # 5
calc(2,  '**', 3)      # 8
#----------------------------
#                     + 51
#                     /  4 = 12.75   
print("총합:", tot())  # 51 
print("평균:", avg())  # 12.75 

