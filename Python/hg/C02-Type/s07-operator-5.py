# 연산자(operator)
# 사칙연산: +, -, /, *
# 정수나누기 : //
# 나머지: %, divmod(x, y)
# 지수: **

#%%

print("10의 3승은? ", 10 ** 3)

#%%

# 지수: **
a = 10
b = 3
c = a ** b
print(c) # 1000

#%%

# 연산 우선순위: 지수 -> 곱합기
x = 2.0 * 10 ** 3
print(x) # 2000.0

#%%

y = (2.0 * 10) ** 3
print(y) # 8000.0

#%%

# 10의 3승
d = 1.0E3  # 1.0 * 10 ** 3
print(d) # 1000.0

#%%

# 지수: **
# g = 3
# print(1.0Eg)    # SyntaxError: invalid decimal literal


#%%

# 2의 3승
x = 2
y = 3
z = x ** y
print(z)  # 8

t = x * x * x
print(t) # 8

