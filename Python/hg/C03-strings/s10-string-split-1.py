# -*- coding: utf-8 -*-

# 문자열 나누기
# 리스트 = 원본문자열.split(분할문자열)
# 원본문자열을 분할문자열로 나누어 결과를 리스트로 리턴

#%%

tel = "010.1234.5678"
tls = tel.split('.')

print(type(tls), tls) # <class 'list'> ['010', '1234', '5678']

print(tls[0]) # '010'
print(tls[1]) # '1234'
print(tls[2]) # '5678'

print(f"{tls[0]}-{tls[1]}-{tls[2]}")
print("{0}-{1}-{2}".format(tls[0], tls[1], tls[2]))
print("{}-{}-{}".format(tls[0], tls[1], tls[2]))

#%%

hp = f"{tls[0]}-{tls[1]}-{tls[2]}"
print(hp)

#%%

print("원본:", tel) # 불변

#%% 

# 문자열 : immutable(불변)
# 문자열 관련 함수를 실행해도 원본의 변화는 없다.

so = 'abc'
up = so.upper()
print(so)
print(up)  # 불변
