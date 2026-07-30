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
    for val in vals:
        if isinstance(val, int): # val의 자료형이 정수(int)이면 누적 연산 수행
            tot += val
    return tot

#%%

# 가변인자로 호출
print(tots(10))       # 10
print(tots(10,20))    # 30
print(tots(10,20,30)) # 60

#%% 

print(tots((99,))) # 0

#%%

print(tots("홍길동", 10,20)) # 30
