# 문자열 위치 검색
# 처음 만나는 문자열의 위치(인덱스)를 리턴
# 찾는 문자열이 없으면 -1을 리턴

#    012345678901234567890123456789
s = "Python is the best choice"

# [문제] 
# 위 문자열 s에서 공백을 제외한 각 단어를 추출하라
# 단 문자열 함수 find()를 사용하라.
# 조건: 처리 결과를 리스트 담아라.
#   - 슬라이싱(slicing) 사용하라.
#   - 리스트.append()를 이용하라.

#%%

# 참고 
s = "Python is the best choice"
fs = ' ' # 분할할 문자 코드(공백)
sx = 0   # 찾을 문자의 시작 위치

while True:
    se = s.find(fs, sx) # 찾은위치 = find(찾을문자열, 시작위치)
    if se == -1: # 찾지 못하면 -1을 리턴
        # print("찾지 못함: se=", se)
        print(s[sx:])
        break
        
    ss = s[sx:se]
    sx = se + 1  # 이전 찾은 위치에 다음 위치 지정
    print(ss)
    
#%%

# 문자열.split() 함수를 사용한 예
ss = "Python is the best choice"
sp = ss.split() # 공백

print(type(sp), sp) # <class 'list'>
# ['Python', 'is', 'the', 'best', 'choice']
    