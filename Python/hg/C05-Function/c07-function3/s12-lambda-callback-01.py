# -*- coding: utf-8 -*-

# 람다함수 응용

#%%

def add(*vals):
    tot = 0
    for val in vals:
        tot += val
    return tot

# 함수를 변수에 할당
func = add

#%%

# 파라미터
# what: 문자열
# callback: 함수
# vals: 가변인자(계산 할 데이터)
def calc(what, callback, *vals):
    print(f"calc({what}): ", callback(*vals)) # 콜백(callback)

#%%


print("add type:", type(add))  # <class 'function'>
print("fun type:", type(func)) # <class 'function'>

#%%

print("add:", add(1,2,3,4,5)) # 15
print("fun:", func(1,2,3,4,5)) # 15

#%%

calc("홀수", add, 1,3,5,7,9)  # calc(홀수):  25
calc("짝수", func, 2,4,6,8,10) # calc(짝수):  30
    
