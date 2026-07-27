# 제어문(if)
# 조건부 표현식(conditional expression)

# score = 70
score = 59

succ = None
if score >= 60:
    succ = "합격"
else:
    succ = "불합격"    

print('succ=', succ)

#%%
score = 70
succ = None
# if score >= 60: succ = "합격" else: succ = "불합격";
if score >= 60: succ = "합격"
print('succ=', succ)

#%%

# 위의 문장을 아래의 문장으로 변환
# 조건부 표현식(conditional expression)
msg = "합격" if score >= 60 else "불합격"

print('msg=', msg)    

#%%

# JavaScript: 삼항 연산자
# msg = (score >= 60) ? "합격" : "불합격";