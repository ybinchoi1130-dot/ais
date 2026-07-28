# 문자열 위치 검색
# 처음 만나는 문자열의 위치(인덱스)를 리턴
# 찾는 문자열이 없으면 -1을 리턴

#    012345678901234567890123456789
s = "Python is the best choice"

# [문제] 
# 위 문자열 s에서 공백을 제외한 각 단어를 추출하라
# 단 문자열 함수 find()를 사용하라.
# 힌트: 슬라이싱(slicing) 사용
# 조건: 처리 결과를 리스트 담아라.

ss = s   # 대상
fs = ' ' # 분할할 문자 코드(공백)
sx = -1

lst = []

while True:
    ss = ss[sx+1:]
    sx = ss.find(fs) # 공백의 위치에 해당하는 인덱스
    if sx == -1:
        sw = ss[:]
        lst.append(sw)
        break

    lst.append(ss[:sx])

print("결과: ", type(lst))
print(lst)