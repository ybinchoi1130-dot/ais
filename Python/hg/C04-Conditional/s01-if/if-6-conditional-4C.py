# 제어문(if)
# 조건부 표현식(conditional expression)

"""
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
"""

#%%
from random import random, randint, randrange

score = randint(0 , 100)
print(score)
if score < 60:
    grade="E등급"
elif score < 70:
    grade ="D등급"
elif score < 80:
    grade = "C등급"
elif score < 90:
    grade = "B등급"
elif score >= 90:
    grade = "A등급"
else:
    grade = "잘못된 점수"
    
print('grade=',grade)

    
    
   
