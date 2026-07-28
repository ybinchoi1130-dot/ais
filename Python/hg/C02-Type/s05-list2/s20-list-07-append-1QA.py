# 문자열 위치 검색
# 처음 만나는 문자열의 위치(인덱스)를 리턴
# 찾는 문자열이 없으면 -1을 리턴

# [문제] 
# 위 문자열 s에서 공백을 제외한 각 단어를 추출하라
# 단 문자열 함수 find()를 사용하라.
# 힌트: 슬라이싱(slicing) 사용
# 조건: 처리 결과를 리스트 담아라.

# 참고 
ss = "Python is the best choice"
fs = ' ' # 분할할 문자 코드(공백)
sx = 0   # 찾을 문자의 시작 위치

lst = [] # 빈 리스트 생성
cnt = 0

while True:
    cnt += 1
    se = ss.find(fs, sx)
    if se == -1: # 찾지 못하면 -1을 리턴
        sw = ss[sx:]
        lst.append(sw)
        break
        
    print(f"[{cnt}]: se={se}")
    sw = ss[sx:se]
    sx = se + 1  # 이전 찾은 위치에 다음 위치 지정
    lst.append(sw)
    
print("결과: ", type(lst))
print(lst)    