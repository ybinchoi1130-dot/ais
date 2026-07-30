# -*- coding: utf-8 -*-

# 함수(Function)
# 가변인자
# 인자의 갯수가 가변일 때

#%%

# 가변인자로 전달하면 튜플로 받음
# 가변인자형은 파라미터 변수앞에 아스터리스크(*)를 붙임
def tots(*vals):
    print(f"[tots] type({type(vals)}), {vals}, {len(vals)}개") # tuple
    print(f"{type(vals[0])}")
    
#%%

# 가변인자로 호출
tots(10)        # 인자 1개
tots(10,20)     # 인자 2개
tots(10,20,30)  # 인자 3개

#%% 

# 전달된 인자의 타입은 int
tots(99)   # (99,), 1개
tots(99,)  # (99,), 1개

#%%
t1 = 99  # int
t2 = 99, # tuple

#%%

# 전달된 인자의 타입은 tuple
tots((99,)) # [tots] type(<class 'tuple'>), ((99,),), 1개

#%%

# [주의]
# 튜플을 인자로 보내면
# 튜플이 하나의 인자로 전달(3개의 인자가 아님)
tots((10,20,30)) # ((10, 20, 30),), 1개

