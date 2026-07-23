# 리스트 특징을 이해하자

# [문제1]
# 국어, 영어, 수학, 과학 점수를 가진 변수를 만들고
# 점수는 0부터 100까지 지정한 후
# 총점과 평균을 구하라.
# 선택: 각 과목의 점수를 난수를 발생해서 지정하라.

from random import random, randint, randrange
kor = randint(0, 100)
math = randint(0, 100)
eng = randint(0, 100)
sci = randint(0, 100)
total = kor+math+eng+sci
totalev = total/4
avg ="{:g}".format(totalev)
print(type(avg))
print(f"국어점수는{kor}점")
print(f"영어점수는{eng}점")
print(f"수학점수는{math}점")
print(f"과학점수는{sci}점")
print("-"*40)
print(f"총점은{total}이고 평균은{avg}입니다.")








#%%

# [문제2]
# 위 문제1을 리스트 자료형으로 바꿔서 처리하라.
l=[[kor,math,eng,sci],0,0]
l[1]=sum(l[0])
l[2]=total/len(l[0])

print(f"과목점수{l[0]}이고 총점은 {l[1]},평균은{l[2]}입니다.")