# 복합 대입연산자(축약형)
# %=  : 나눠서 나머지를 대입
# **= : 지수(거듭제곱)을 해서 대립

a = 10
b = 3
print('a=', a)
print('b=', b)

a %= b
print('a=', a) # 1

a = a % b

#%%

a = 10
b = 3
b %= a
d = b % a
print('b=', b) # 3 = 3 % 10
print('d=', d) # 3 = 3 % 10


#%%

# %=  : 나눠서 나머지를 대입 : b = b % a
b = 10
a = 3
b %= a
print('b=', b) # 1
print('b %= a : ', b) # 1

