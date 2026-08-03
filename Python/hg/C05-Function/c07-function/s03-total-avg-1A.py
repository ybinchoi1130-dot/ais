# -*- coding: utf-8 -*-

# 함수(Function)

#%%
# [문제]
# 국어, 영어, 수학의 점수를 받아서 
# 총점과 평균을 구하는 함수를 각각 정의하라.
# 그리고 함수를 호출해서 결과를 출력하라.

#%%

# 함수정의
# 총점: 국어, 영어, 수학과목의 점수를 인자로 받음
# 인자: k(국어), e(영어), m(수학)
# 리턴: 3과목 총점
def total(k, e, m):
    return k + e + m

# 평균: tot(총점), cnt(과목수)
# 리턴: 평균값 = 총점 / 과목수
def average(tot, cnt):
    return round(tot / cnt, 2)

#%%

# 함수 호출
tot = total(70,80,90) # 총점을 구하는 함수 호출
avg = average(tot, 3) # 평균을 구하는 함수 호출

print("총점:", tot)
print("평균:", avg)

#%%

print("영수:", total(100, 90, 100), average(total(100,90,100), 3))
print("철수:", total(99, 99,99), average(total(99,99,99), 3))
    

