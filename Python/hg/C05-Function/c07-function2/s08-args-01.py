# -*- coding: utf-8 -*-

# 함수(Function)
# 가변인자
# 인자의 갯수가 가변일 때

#%%

# 가변인자로 전달하면 튜플로 받음
# 가변인자형은 파라미터 변수앞에 아스터리스크(*)를 붙임
def tots(*vals):
    print(f"[tots] type({type(vals)}), {vals}") # tuple
    tot = 0
    for val in vals: # 튜플에서 요소를 하나씩 꺼내서 연산을 수행
        tot += val
    return tot

#%%

# 가변인자로 호출
print(tots(10))       # 10
print(tots(10,20))    # 30
print(tots(10,20,30)) # 60

#%% 

# TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
tots((99,))

#%%

# TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
totx = 0
totx += (99,)



