# -*- coding: utf-8 -*-

# 람다함수 응용
# 함수: 
# 일급함수(First-class)    
# 파이썬에서 일급 함수란 함수를 일반 변수처럼 다루는 성질을 뜻하며, 
# 함수를 변수에 할당하고, 다른 함수의 인자로 전달하며, 
# 함수의 결과로 반환할 수 있는 특징을 가집니다. 

#%%

from random import randint
def control_center(name, callback):
    name2 = name + "님"
    event = randint(1,2)  # 1:화재, 2:홍수

    # callback(name=name2, evt=event) # 호출: 홍길동, 정미라, 최정명, 아파트
    callback(name2, event) # 호출: 홍길동, 정미라, 최정명, 아파트
    # 홍길동(name2, evnet)
    # 정미라(name2, evnet)
    # 최정명(name2, evnet)
    # 아파트(name2, evnet)
#%%
def 홍길동(name, evt):
    print(f"[{name}] {evt} ", "화재!" if evt == 1 else "홍수!")
    
def 정미라(name, evt):
    print(f"[{name}] {evt} ", "불이야!" if evt == 1 else "물이야!")
    
def 최정명(name, evt):
    print(f"[{name}] {evt} ", "대피해!" if evt == 1 else "도망가!")
    
def 아파트(name, evt):
    print(f"[{name}] {evt} ", "화재경보!" if evt == 1 else "대피경보!")
    
def 빌라(name, evt):
    print(f"[{name}] {evt} ", "화재경보!" if evt == 1 else "대피경보!")

#%%

control_center("낙원빌라", 빌라)
control_center("공원빌라", 빌라)

"""
control_center("길동", 홍길동)
control_center("미라", 정미라)
control_center("정명", 최정명)
control_center("관리", 아파트)
"""

