# 문자열 위치 검색
# 처음 만나는 문자열의 위치(인덱스)를 리턴
# 찾는 문자열이 없으면 -1을 리턴

# [문제] 
# 문자열 s에서 공백을 제외한 각 단어를 추출하라
# 단 문자열 함수 index()를 사용하라.
# 힌트: 슬라이싱(slicing) 사용
s = "Python is the best choice"
fs = ' ' # 분할할 문자 코드(공백)
sx = 0

while True:
    se = s.index(fs, sx)
    ss = s[sx:se]
    print(ss)
    sx = se + 1
    
#%%

# 맨 마지막 단어를 처리하지 못하고 종료 됨
"""
Python
is
the
best
"""
    
#%%

# 예외처리(Exception)
s = "Python is the best choice"
fs = ' ' # 분할할 문자 코드(공백)
sx = 0   # 찾을 문자의 시작 위치

while True:
    try:
        se = s.index(fs, sx)
        ss = s[sx:se]
        sx = se + 1  # 이전 찾은 위치에 다음 위치 지정
        print(ss)
    except: # 예외발생: index()에서 ValueError 발생
        print(s[sx:])
        break
        

