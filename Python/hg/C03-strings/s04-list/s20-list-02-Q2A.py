# 리스트 특징을 이해하자

# [문제1]
# 국어, 영어, 수학, 과학 점수를 가진 변수를 만들고
# 점수는 0부터 100까지 지정한 후
# 총점과 평균을 구하라.
# 선택: 각 과목의 점수를 난수를 발생해서 지정하라.

# 난수
from random import randint

k = randint(0, 100)
e = randint(0, 100)
m = randint(0, 100)
s = randint(0, 100)
t = k + e + m + s
a = round(t / 4, 2)
print("국어:", k)
print("영어:", e)
print("수학:", m)
print("과학:", s)
print("---------------")
print("총점:", t)
print("평균:", a)
print()

#%%

# [문제2]
# 위 문제1을 리스트 자료형으로 바꿔서 처리하라.
k = randint(0, 100)
e = randint(0, 100)
m = randint(0, 100)
s = randint(0, 100)
h = randint(0, 100)
titles = [['국어', '영어', '수학', '과학', '역사'], '총점', '평균']
scores = [[k, e, m, s, h], 0, 0]

score = scores[0]
scores[1] = sum(score)              # 총점
scores[2] = scores[1] / len(score)  # 평균

print("# 학생 성적 #")
title = titles[0]
for index, subject in enumerate(title):
    print(f"{subject}: {score[index]}")   # 과목

print("---------------")
print(f"{titles[1]}: {scores[1]}")          # 총점
print(f"{titles[2]}: {round(scores[2],2)}") # 평균

