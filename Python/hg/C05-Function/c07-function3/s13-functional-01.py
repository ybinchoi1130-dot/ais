# -*- coding: utf-8 -*-

# 함수형 프로그래밍(Functional Programming)
#
# (사전적 의미)
# 함수형 프로그래밍(函數型 프로그래밍, 영어: functional programming)은 
# 자료 처리를 수학적 함수의 계산으로 취급하고 
# 상태와 가변 데이터를 멀리하는 프로그래밍 패러다임의 하나이다.

#%%
def score(name): # 외부함수(정의)
    print(f"[score] name({name})")
    
    def minmax(*args): # 내부함수(정의)
        min = args[0]  # 최솟값
        max = args[0]  # 최대값
        
        for val in args:
            if val < min:
                min = val
            if val > max:
                max = val
                
        return name, min, max # 이름, 최솟값, 최대값
    
    return minmax

#%%
# 전용함수
mfunc = score("[중간고사]")
lfunc = score("[기말고사]")

print(mfunc(70,80,90))   # ('[중간고사]', 70, 90)
print(mfunc(88,99,100))  # ('[중간고사]', 88, 100)

print(lfunc(80,90,100))  # ('[기말고사]', 80, 100)
print(lfunc(90,77,65))   # ('[기말고사]', 65, 90)

