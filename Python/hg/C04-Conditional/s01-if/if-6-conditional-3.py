# 제어문(if)
# 조건부 표현식(conditional expression)

# score = 59
score = 61

msg = "합격" if score >= 60 else "보류" if score >= 55 else "불합격"

print('1] msg=', msg) # 보류

#%%

# JavaScript
# msg = (score >= 60) ? "합격" : (score >= 55) ? "보류" : "불합격"

#%%

# 일반 조건문(if)
# 단일 조건문
if score >= 60:
    msg = "합격"
elif score >= 55:
    msg = "보류"    
else:
    msg = "불합격"    

print('2] msg=', msg)    

#%%

# 일반 조건문(if)
# 이중 조건문
if score >= 55:
    if score >= 60:
        msg = "합격"
    else:
        msg = "보류"    
else:        
    msg = "불합격"    

print('3] msg=', msg)    
