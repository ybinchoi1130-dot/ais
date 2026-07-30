# -*- coding: utf-8 -*-

# 함수(Function)

# [문제]
# 함수를 이용하여 사칙연산 계산기를 만들라.
# 계산기능: 
#   - 더하기, 빼기, 나누기, 곱하기, 나머지, 제곱
#   - 총합누적, 평균
#   - 히스토리(이력)

#%%

# 글로벌(global) 변수
histories = [] # 히스토리: 표현식을 전체를 이력처리
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

# 연산자별 연산 수행
def comp(a, op, b):
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
    else: # 준비되지 않은 연산자
        return None
    
    return c

# 계산기
def calc(a, op, b):
    # 전연변수: 함수 밖에 선언되어 있는 변수의 값을 변경하려면 global 선언
    global histories # 객체형은 global을 명시하지 않아도 수정 가능
    global total
    global count
    
    c = comp(a, op, b)
    if c == None:
        return 0
    
    # 누적
    count += 1 # 연산횟수 누적
    total += c # 연산결과 누적
    # histories.append(c) # 계산결과를 보관(히스토리)
    histories.append((a, op, b)) # calc() 함수에 전달된 인자를 보관(튜플)
    
    return c   # 단위연산 결과 리턴

#%%

# 총합
def tot():
    return total

# 평균
def avg():
    return total / count

# 재계산(히스토리)
def recalc(): 
    print("[recalc]")
    t = 0
    for a, op, b in histories:
        c = comp(a, op, b)
        t += c
        print(f"{c} = {a} {op} {b}: total({t})")
    return t, t / len(histories) # 튜플(총합, 평균)

#%%

calc(10, '+', 20)      # 30    
calc(2,  '*', 4)       # 8
calc(10, '/', 2)       # 5
calc(2,  '**', 3)      # 8

# calc() 함수에서 지원하지 않는 연산자
calc(2,  '&', 3)       # 0

print("총합:", total)  # 51 
print("총합:", tot())  # 51 
print("평균:", avg())  # 12.75 
print("검산:", recalc())  # (51, 12.75)

