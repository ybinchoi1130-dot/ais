# -*- coding: utf-8 -*-

# 함수(Function)

# [문제]
# 함수를 이용하여 사칙연산 계산기를 만들라.
# 계산기능: 
#   - 더하기, 빼기, 나누기, 곱하기, 나머지, 제곱
#   - 총합누적, 평균
#   - 히스토리(연산결과 저장)

#%%

total = 0   
count = 0

def add(a,b):
    return a + b
def subt(a,b):
    return a - b
def mup(a,b):
    return a * b
def div(a,b):
    return a / b
def get_div(a,b):
    return a % b
def po(a,b):
    return a ** b

def cal(a,op,b):
    if op == '+':
        c = add(a,b)
    elif op == '-':
        c = subt(a, b)
    elif op == '*':
        c = mup(a, b)
    elif op == '/':
        c = div(a, b)
    elif op == '%':
        c = get_div(a, b)
    elif op == '**':
        c = po(a, b)
    else:
        return 0
    
    cnt = count +1 
    tot = total+c
    
    return tot,cnt

def tot():
    return total
def avg():
    return tot() / count

print(cal(3, '%', 1))
cal(10,'+',7)
cal(11, '-', 9)
cal(300,'**',3)
cal(1000,"/",100)   
print("총합:", tot())  # 51 
print("평균:", round(avg(),2))