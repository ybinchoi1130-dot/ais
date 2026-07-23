# 문자열 위치 검색
# 처음 만나는 문자열의 위치(인덱스)를 리턴
# 찾는 문자열이 없으면 -1을 리턴

#    012345678901234567890123456789
s = "Python is the best choice"

# [문제] 
# 위 문자열 s에서 공백을 제외한 각 단어를 추출하라
# 단 문자열 함수 find()를 사용하라.
# 힌트: 슬라이싱(slicing) 사용
ss = s
fs = ' ' # 찾을 문자

sx = ss.find(fs)
s1 = ss[:sx]
print(s1) # 'Python'

ss = ss[sx+1:]
sx = ss.find(fs)
s2 = ss[:sx]
print(s2) # 'is'

ss = ss[sx+1:]
sx = ss.find(fs)
s3 = ss[:sx]
print(s3) # 'the'

ss = ss[sx+1:]
sx = ss.find(fs)
s4 = ss[:sx]
print(s4) # 'best'

ss = ss[sx+1:]
sx = ss.find(fs)
s5 = ss[:]
print(s5) # 'choice'
