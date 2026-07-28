# -*- coding: utf-8 -*-

# 제어문
# s안에 x값이 존재하는지 유무?
# x in s
# x not in s

s = [1,3,5,7,9]
x = 9

if x in s:
    print(f"리스트 {s} 안에 ({x}) 값이 존재한다.")
else:    
    print(f"리스트 {s} 안에 ({x}) 값이 존재하지 않는다.")

#%%

x = 10

if x not in s: # 존재하지 않으면 참
    print(f"리스트 {s} 안에 ({x}) 값이 존재하지 않는다.")
else: # 존재하면 거짓
    print(f"리스트 {s} 안에 ({x}) 값이 존재한다.")


#%%
#count

n=2
l=[2,4,6,8]
if l.count(n) >0:
    print(f"리스트 {l} 안에 ({n}) 값이 존재한다.")
else:
    print(f"리스트 {l} 안에 ({n}) 값이 존재하지 않는다.")
    
#%%
vl=4 #tuple이라 2,4 는 리스트안에 없다.
l2=[4,2,2,4,6,6,8]
cnt=l2.count(vl)

if cnt >0 :
    print(f"리스트 {l2} 안에 ({vl}) 값이 {cnt}개 존재한다.")
else:
    print(f"리스트 {l2} 안에 ({vl}) 값이 {cnt}개 존재하지 않는다.")