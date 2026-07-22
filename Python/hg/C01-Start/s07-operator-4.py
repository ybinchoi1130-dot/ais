# 연산자(operator)
# 사칙연산: +, -, /, *
# 정수나누기 : //
# 나머지: %, divmod(x, y)
# 지수: **

# 나머지 : %
a = 10
b = 3
d = a % b
print('나머지:', d) # 1


#%%

# [문제] 위 변수 a를 b로 나누었을 때 몫과 나머지를 구하라
m = a // b # 몫
n = a % b  # 나머지
print("{0}를 {1}로 나누었을 때 몫은 ({2}), 나머지 ({3})".format(a, b, m, n))

#%%

x, y = a // b, a % b  # 나머지
print("{0}를 {1}로 나누었을 때 몫은 ({2}), 나머지 ({3})".format(a, b, x, y))


#%%

# divmod() 함수를 이용해서 몫과 나머지를 구함
mn = divmod(a, b)
print("divmod({0}, {1}) -> {2}".format(a,b,mn))
# divmod(10, 3) -> (3, 1)

#%%

a =10
b=3

# unpacking
m, n = divmod(a, b)
print("divmod({0}, {1}) -> 몫({2}), 나머지({3})".format(a,b,m,n))
# divmod(10, 3) -> 몫(3), 나머지(1)

#%%
print("divmod({0}, {1}) -> 몫({2}), 나머지({3})".format(a, b, mn[0], mn[1]))
# divmod(10, 3) -> 몫(3), 나머지(1) 