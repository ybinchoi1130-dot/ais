# -*- coding: utf-8 -*-

# 함수형 프로그래밍(Functional Programming)
#
# (사전적 의미)
# 함수형 프로그래밍(函數型 프로그래밍, 영어: functional programming)은 
# 자료 처리를 수학적 함수의 계산으로 취급하고 
# 상태와 가변 데이터를 멀리하는 프로그래밍 패러다임의 하나이다.

#%%

# [문제]
# 내부함수를 이용해서 총점, 평균을 구하는 함수를 정의하고
# 중간고사, 기말고사 전용함수를 만들어라.

#%%
def score(name): # 외부함수(정의)
    print(f"[score] name({name})")
    
    def totavg(*args): # 내부함수(정의)
        tot = 0    # 총점
        avg = 0.0  # 평균
        
        for val in args:
            tot += val
            
        avg = round(tot / len(args), 2)
        return name, tot, avg
    
    return totavg

#%%
# 전용함수
mfunc = score("[중간고사]")
lfunc = score("[기말고사]")

print(mfunc(70,80,90))   # ('[중간고사]', 240, 80.0)
print(mfunc(88,99,100))  # ('[중간고사]', 287, 95.67)

print(lfunc(80,90,100))  # ('[기말고사]', 270, 90.0)
print(lfunc(90,77,65))   # ('[기말고사]', 232, 77.33)

