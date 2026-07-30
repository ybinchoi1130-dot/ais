# -*- coding: utf-8 -*-

# 함수(Function)

#%%

# [문제]
# 국어, 영어, 수학의 점수를 받아서 총점과 평균을 구하는 함수를 각각 정의하라.
# 그리고 함수를 호출해서 결과를 출력하라.

#%%

#다중리턴=튜플
def subject_total(sub1,sub2,sub3):
    return sub1 + sub2 + sub3
def subject_average(sub1,sub2,sub3):
    total = subject_total(sub1,sub2,sub3)
    return total / 3


kor_score = int(input("국어점수 입력하세요 : "))
eng_score = int(input("영어점수 입력하세요 : "))
math_score = int(input("수학점수 입력하세요 : ")) 

total_score  = subject_total(kor_score, eng_score, math_score) 
average_result = subject_average(kor_score, eng_score, math_score) 

print(f"""국어점수: {kor_score}점
영어점수: {eng_score}점
수학점수: {math_score}점""") 
print(f"총점: {total_score}점")
print(f"평균: {average_result:.2f}점")

print(subject_total)
