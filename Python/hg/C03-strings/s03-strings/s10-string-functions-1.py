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
# 리스트를 결합(join)해서 문자열로 생성
tel = ['010', '1234', '5678']
cst = '-'.join(tel)
print(tel, type(tel))
print(cst)

#%%

# 문자열 분할 : split()
# 문자열을 지정된 문자로 분할하여 리스트로 생성
hp = cst.split('-')
print(tel, type(tel))
print(hp, type(hp))
print('type : tel == hp ? ', type(tel) == type(hp))

print(f"{hp[0]}-{hp[1]}-{hp[2]}")
print("{0}-{1}-{2}".format(hp[0], hp[1],hp[2]))

