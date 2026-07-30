# -*- coding: utf-8 -*-

# 함수(Function)
# 가변인자
# 인자의 갯수가 가변일 때

#%%

# 가변인자로 전달하면 튜플로 받음
# 가변인자형은 파라미터 변수앞에 아스터리스크(*)를 붙임
# 가변 파라미터 앞에 일반 파라미터 지정 가능

#%%

# 오류: 가변인자 다음에 고정된 인자가 올 수 없다.
"""
def totx(*vals, title):
    print(f"[{title}] {vals}", end=": ") # tuple

print(totx(1,3,5,7, '홀수'))
print(totx(1,3,5,7))
"""

#%%
    
def tots(title, *vals):
    print(f"[{title}] {vals}", end=": ") # tuple
    tot = 0
    for val in vals:
        tot += val
    return tot

#%%

# 가변인자로 호출
print(tots("홀수", 1,3,5,7))
print(tots("짝수", 2,4,6,7,10))

