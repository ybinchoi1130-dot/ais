# -*- coding: utf-8 -*-

# 함수(Function)
# 일급시민(First Class Citizen) : 모든 권리를 다 가진 시민처럼 취급
#   - 함수형 프로그래밍 언어에서는 함수도 변수와 같은 방식으로 취급
#   - 함수를 변수에 대입할 수 있다.
#   - 함수를 리턴할 수 있다.
#   - 컬렉션에 저장할 수 있다.

# [문제] 함수형 프로그래밍 기법으로 작성하라.
# 함수를 이용하여 사칙연산 계산기를 만들라.
# 계산기능: 
#   - 더하기, 빼기, 나누기, 곱하기, 나머지, 제곱
#   - 총합누적, 평균
#   - 히스토리(이력)

#%%

# 전역변수(global variable)
# histories = [] # 히스토리: 표현식 전체를 이력처리
# total = 0   # 총합누적
# count = 0   # 연산횟수

#%%

# 계산기
def Calc(name):
    histories = [] # 이력처리
    total = 0      # 총합누적
    count = 0      # 연산횟수
    
    # 총합
    def tot():
        nonlocal total
        return total
    
    # 평균
    def avg():
        nonlocal total, count
        return total / count
    
    # 재계산(히스토리)
    def recalc(): 
        nonlocal histories
        
        t = 0
        for a, op, b in histories:
            c = comp(a, op, b)
            t += c
            print(f"{c} = {a} {op} {b}: total({t})")
        return t, t / len(histories) # 튜플(총합, 평균)    
    
    def compute(a, op, b):
       nonlocal histories, total, count
       
       c = comp(a, op, b)
       if c == None:
           return 0
       
       # 누적
       count += 1 # 연산횟수 누적
       total += c # 연산결과 누적
       histories.append((a, op, b)) # calc() 함수에 전달된 인자를 보관(튜플)
       return c   # 단위연산 결과 리턴    
    
    def calc(oper, *args):
        if oper == 'tot':
            return tot()
        elif oper == 'avg':
            return avg()
        elif oper == 'recalc':
            return recalc()
        elif oper == 'calc':
            a, op, b = args
            return compute(a, op, b)
        elif oper == 'name':
            return name
        else:
            return None
     
    return calc

#%%

# 더하기
def plus(a, b):
    return a + b

# 빼기
def sub(a, b):
    return a - b

# 곱하기
def mul(a, b):
    return a * b

# 나누기(정수 나누기)
def div(a, b):
    return a // b

# 나머지
def sur(a, b):
    return a % b

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



#%%

c0 = Calc("더미계산기")
c0('calc', 10, '*', 20)
c0('calc', 10, '^', 20)    # 없는 연산자
print("이름:", c0('name'))
print("총합:", c0('tot'))  
print("평균:", c0('avg'))  
print("검산:", c0('recalc'))

#%%

calc = Calc("전자계산기")
calc('calc', 10, '+', 20)      # 30    
calc('calc', 2,  '*', 4)       # 8
calc('calc', 10, '/', 2)       # 5
calc('calc', 2,  '**', 3)      # 8

print("이름:", calc('name'))
print("총합:", calc('tot'))    # 51 
print("평균:", calc('avg'))    # 12.75 
print("검산:", calc('recalc')) # (51, 12.75)

#%%
print('-' * 30)

calc2 = Calc("전자계산기2")
calc2('calc', 99, '+', 1)      # 100    

print("이름:", calc2('name'))
print("총합:", calc2('tot'))    # 51 
print("평균:", calc2('avg'))    # 12.75 
print("검산:", calc2('recalc')) # (51, 12.75)


#%%

print("총합:", calc('tot'))     # 51 
print("총합:", calc2('tot'))    # 100 

