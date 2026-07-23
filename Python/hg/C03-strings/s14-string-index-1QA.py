# 문자열 위치 검색
# 문자열.index(...)

#    012345678901234567890123456789
s = "Python is the best choice"

# [문제] 
# 위 문자열 s에서 공백을 제외한 각 단어를 추출하라
# 단 문자열 함수 index()를 사용하라.
# 힌트: 문자열 함수 index의 start 파라미터를 활용

fs = ' '

s1 = s.index(fs)
s2 = s.index(fs, s1 + 1)
s3 = s.index(fs, s2 + 1)
s4 = s.index(fs, s3 + 1)
print(s1, s2, s3, s4, sep=', ') # 6, 9, 13, 18 

t1 = s[:s1]
t2 = s[s1+1:s2]
t3 = s[s2+1:s3]
t4 = s[s3+1:s4]
t5 = s[s4+1:]
print(t1) # Python
print(t2) # is
print(t3) # the 
print(t4) # best
print(t5) # choice