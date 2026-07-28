# 반복문(for)

"""
# [문제]
# 국어, 국사, 과학, 수학의 점수를 딕셔너리(dict)로 저장하여
# 각 과목과 점수를 출력하고 총점, 평균을 구하라.
# 각 과목에서 최저 점수와 최고 점수를 표시하라.
# 조건: 
#   - 각 과목의 점수는 0부터 100까지 난수로 처리하라.
#   - 총점은 for문으로 계산하라.
#   - 평균은 소숫점 2자리까지 출력하라.
"""
#%%
from random import randint 

subjects = ["국어","국사","과학","수학"]
scores = {sub:randint(0, 100) for sub in subjects}
# .items() = key , value 꺼내오기
# .key() = 과목이름만 꺼내오기
# .values() = 점수만 꺼내오기 
for sub, score in scores.items():
 print(f"과목별 {sub} :{score}점 입니다.")  
#총점, 평균 구하기
total = 0
for score in scores.values():
    total += score

average = total / len(scores)
#최고, 최저 구하기
maxsub = max(scores,key=scores.get)
minsub = min(scores,key=scores.get)

print(f"최고 과목점수는 {maxsub}: {scores[maxsub]}")
print(f"최저 과목점수는 {minsub}: {scores[minsub]}")
print(f"총점{total}점이고 평균은{average:.2f}점입니다.")
      


#%% 제미나이 코드 
'''
import random

# 1. 과목 리스트 정의 및 난수(0~100)로 딕셔너리 생성
subjects = ["국어", "국사", "과학", "수학"]
scores = {sub: random.randint(0, 100) for sub in subjects}

# 2. 각 과목과 점수 출력
print("--- [ 과목별 점수 ] ---")
for sub, score in scores.items():
    print(f"{sub}: {score}점")

# 3. for문을 이용한 총점 계산
total_score = 0
for score in scores.values():
    total_score += score

# 4. 평균 계산 (소수점 2자리)
average_score = total_score / len(scores)

# 5. 최고 점수와 최저 점수 과목 찾기
max_sub = max(scores, key=scores.get)
min_sub = min(scores, key=scores.get)

# 6. 결과 출력
print("\n--- [ 통계 결과 ] ---")
print(f"총점: {total_score}점")
print(f"평균: {average_score:.2f}점")
print(f"최고 점수: {max_sub} ({scores[max_sub]}점)")
print(f"최저 점수: {min_sub} ({scores[min_sub]}점)")
'''