# -*- coding: utf-8 -*-

# 문자열 삽입
# 결과 = 삽입할문자열.join(원본문자열)
# 원본문자열의 각 문자들 사이에 문자열을 삽입

s = "ABCDEFG"   # 원본
t = ','.join(s) # 결과 : 원본에 콤마(,)를 삽입

# 문자열
print(s)  # ABCDEFG
print(t)  # A,B,C,D,E,F,G

#%%

print(", ".join(s)) # A, B, C, D, E, F, G

#%%

# 리스트를 결합(join)해서 문자열로 생성
tel = ['010', '1234', '5678']
cst = '-'.join(tel)
print(tel, type(tel))
print(cst)

#%%

# [문제]
# 아래 전화번호를 공백(' ') 대신에 하이픈('-')으로 대체하라.
# 단. 최종적으로 join() 함수를 이용해서 완성하라.

hp = "010 1234 1234"
tl = hp.split()   # 공백으로 문자열 분할: ['010', '1234', '1234']
tx = '-'.join(tl) # 하이픈으로 문자열 삽입: 010-1234-1234
print(tl, tx)



