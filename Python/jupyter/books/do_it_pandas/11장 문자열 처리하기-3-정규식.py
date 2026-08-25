# 정규 표현식(Regular Expression)

# 정규 표현식을 사용하지 않고 처리
# 주민번호 뒷자리를 '*'로 마킹하여 정보를 보호
data = """kim 940431-1234567
lee 250710-4123456
"""

result = []

# for line in data.split("\n"): # 개행(\n 단위로 토큰 분할)
for line in data.splitlines(): # 개행(\n 단위로 토큰 분할)
    word_result = []
    for word in line.split(' '): # 공백으로 성과 주민번호 토큰 분할
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit(): # 주민번호
            word = word[:6] + '-' + ('*' * 7) # '*'로 7자리를 마킹
        word_result.append(word) # 성, 마킹된 주민번호 추가

    # 성과 주민번호 사이에 공백 추가해서 문자열로 변환        
    words = ' '.join(word_result) 
    print("word_result:", word_result, words) 
    result.append(words)
    
print('result:', result)    
print()
print('\n'.join(result))

#%%

"""
kim 940431-*******
lee 250710-*******
"""
