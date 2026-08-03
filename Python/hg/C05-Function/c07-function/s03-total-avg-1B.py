# -*- coding: utf-8 -*-

# 함수(Function)

#%%
# [문제]
# 국어, 영어, 수학의 점수를 받아서 총점과 평균을 구하는 함수를 각각 정의하라.
# 그리고 함수를 호출해서 결과를 출력하라.

#%%

# 다중 리턴: 튜플
# 총점, 평균을 리턴하는 함수
def totavg(k, e, m):
    tot = k + e + m
    avg = tot / 3
    return tot, round(avg, 2)


#%%

t, a = totavg(70,80,90)
# 지역변수: 함수 내부에서 선언된 변수는 함수 바깥에서 사용할 수 없다.
# print("총점:", tot)
# print("평균:", avg)
print("총점:", t)
print("평균:", a)


#%%

# 리턴값은 튜플: unpacking
tot, avg = totavg(70,80,90)
print("총점:", tot)
print("평균:", avg)

#%%

print("영수:", totavg(100, 90, 100))
print("철수:", totavg(99, 99,99))


#%%    

# 다중 리턴을 튜플로 받음
score = totavg(70,80,90)
print("점수:", type(score), score)    # <class 'tuple'> (240, 80.0)
print("총점:", score[0])
print("평균:", score[1])

#%%

# 총점을 받지 않고 평균만 받음
_, sa = totavg(70,80,90)
print("평균:", sa)  # 평균: 80.0

#%%
# 평균은 받지 않고 총점만 받음
st, _ = totavg(70,80,90)
print("총점:", st) # 총점: 240

