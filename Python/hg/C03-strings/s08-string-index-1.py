# -*- coding: utf-8 -*-

# 문자열 함수

# 문자열의 위치 : index()
# 처음 만나는 문자열의 위치
# 결과
#   성공 : 0부터
#   실패 : ValueError 예외발생
# str.index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.

s = "Python is the best choice"
print("0123456789" * 4)
print(s)

#%%

# 문자 한개 탐색
ipos = s.index('i')
print(f"'{s}'.index('i') : ", ipos) # 7

#%%

# 문자 한개 탐색

# 예외발생: 프로그램이 강제종료
# ValueError: substring not found
kpos = s.index('k')
print(f"'{s}'.index('k') : ", kpos) 

#%%

# 문자열 탐색
print(f"'{s}'.index('is') : ", s.index('is'))   # 7
print(f"'{s}'.index('the') : ", s.index('the')) # 10

#%%

# [문제]
# 문자열을 연속해서 찾기.
# 문자열 변수(s)에서 지정된 문자열('t')의 위치를 모두 찾아라.
# 단. find() 함수를 이용하라.
# 정답: 2 10 17

s = "Python is the best choice"
print("0123456789" * 4)
print(s)

# 찾을 문자열
findstr = 't'
print(f"문자열 ('{s}')에서 문자열('{findstr}')의 갯수는?", s.count(findstr))

#%%

# [해결1] 슬라이싱
t1 = s.index(findstr)
t2 = s[t1+1:].index(findstr) + t1 + 1
t3 = s[t2+1:].index(findstr) + t2 + 1
print(t1,t2,t3) # 2 10 17

#%%

# 분할
t1 = s.index(findstr)
s1 = s[t1+1:]  # 슬라이싱
t2 = s1.index(findstr) + t1 + 1 # 이전위치
s2 = s[t2+1:]  # 슬라이싱 
t3 = s2.index(findstr) + t2 + 1 # 이전위치
print(t1,t2,t3) # 2 10 17

#%%

# [해결2] index() 함수의 시작위치
# str.index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.
# 결과 = 문자열.index(탐색문자열, 시작위치[, 종료위치])

t1 = s.index(findstr)
t2 = s.index(findstr, t1 + 1) # 다음위치
t3 = s.index(findstr, t2 + 1) # 다음위치
print(t1,t2,t3) # 2 10 17

#%%

sp = s.split() # 공백

for idx, item in enumerate(sp):
    print(f"sp[{idx}]:{item}")