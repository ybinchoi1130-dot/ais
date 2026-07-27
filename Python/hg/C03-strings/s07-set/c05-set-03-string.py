# 집합 자료형 : set()
# 

# 문자열을 세트로 변환
welcome = "welcome to korea"
print(len(welcome), ':', welcome) # 16 : welcome to korea

# 문자열을 문자로 분해
# 중복은 제거 : 총5개 제거 -> 공백, 2개('e'), 2개('o')
# 순서는 보장하지 않음5
st = set(welcome)
print(len(st), ':', st) 
st = 

#%%

# 결과
# 11 : {'o', 'r', 'c', 't', ' ', 'e', 'w', 'l', 'm', 'a', 'k'}
