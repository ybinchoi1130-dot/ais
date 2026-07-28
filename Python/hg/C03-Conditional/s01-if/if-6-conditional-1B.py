# 제어문(if)
# 조건부 표현식(conditional expression)

score = 59

# 변수 message를 if 블럭 안에서 선언한 후에 블럭 밖에서 사용
if score >= 60: # 60이상
    message = "합격"

# 블럭 밖에서 사용할 수 있지만 '합격'이 아닌 경우는 오류
print(message)  # NameError: name 'message' is not defined  
