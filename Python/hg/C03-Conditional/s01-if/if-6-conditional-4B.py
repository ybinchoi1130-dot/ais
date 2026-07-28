# 제어문(if)
# 조건부 표현식(conditional expression)

# [문제]
# 점수에 따른 등급을 부여한다.
# 조건: 
#   - 점수의 범위는 0점에서 100점 사이여야 한다.
#   - 범위를 넘어서면 "잘못된 점수"라고 출력한다.
# A등급 : 90점 이상
# B등급 : 80점 이상
# C등급 : 70점 이상
# D등급 : 60점 이상
# E등급 : 60점 미만

# 단: 일반 조건문과 조건부 표현식으로 코딩하라

#%%

# score = -110
# score = 110
score = 99
grade = None  # 옵션: 선언하지 않아도 된다.

# 일반 조건문
if score >= 0 and score <= 100:
    if score < 60:
        grade = 'E'
    elif score < 70:
        grade = 'D'    
    elif score < 80:
        grade = 'C'    
    elif score < 90:
        grade = 'B'    
    else:
        grade = 'A'    
else:    
    grade = "'잘못된 점수'"

print(f"<1> 점수는 {score}점이며 등급은 {grade}이다")    

#%%

# [문제]
# 조건부 표현식(conditional expression)
score = 99
grade = 'A' if score >= 90 and score <= 100 \
    else 'B' if score >= 80 and score < 90 \
    else 'C' if score >= 70 and score < 80 \
    else 'D' if score >= 60 and score < 70 \
    else 'E' if score >= 0 and score < 60 \
    else "'잘못된 점수'"        

print(f"<2> 점수는 {score}점이며 등급은 {grade}이다")    

#%%

score = 88
grade = 'A' if 90 <= score <= 100 \
    else 'B' if 80 <= score < 90 \
    else 'C' if 70 <= score < 80 \
    else 'D' if 60 <= score < 70 \
    else 'E' if 0 <= score < 60 \
    else "'잘못된 점수'"        

print(f"<2> 점수는 {score}점이며 등급은 {grade}이다")

