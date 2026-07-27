# 제어문(if)
# 조건부 표현식(conditional expression)

# score = 70
score = 60
# message = None

# 변수 message를 if 블럭 안에서 선언한 후에 블럭 밖에서 사용
if score >= 60: # 60이상미면
    message = "합격"
else:
    message = "불합격"    

# 블럭 밖에서 사용할 수 있다.
print(message)    
