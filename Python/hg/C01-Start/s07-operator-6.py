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

#변수로는 대입이 안된다. 숫자로만 가능 

#%%

# 2의 3승
x = 2
y = 3
z = x ** y
print(z)  # 8

t = x * x * x
print(t) # 8

print(10**5)
#%%
#원의 둘레와 넓이 구하기
pi = 3.14159265
print(pi)

r=10
print("원주율 =",pi)
print("반지름 =", r)
print("원의 둘레 =",2*pi*r)
print("원의 넓이 =", pi *r**2)
#%%

a=10
b=5
bx=b
b /=a
print('b/=a :',b)
print(f"{bx} / {a} -> {b}")


#%%
#문제1
a=10000
b=1000
c=500
d=100
e=10
f=a*4+b*3+c*5+d*9+e*6

print("만원짜리 =",a*4)
print("천원짜리 =",b*3)
print("오백원짜리 =",c*5)
print("백원짜리 =",d*9)
print("십원짜리 =",e*6)
print("총 금액 =",f)
print("지출 금액 =",(a+(b*5))*2)
print("지출하고 남은 금액 =",f-(a+(b*5))*2)


#%%%
#문제2

a= 400
b= 0.3
c= a*0.03
d= a*b
s="만원"

print("월급 =",a,s)
print("보너스 =",a*b,s)
print("세금 =",a*0.03,s)
print("총 연수령액 =",(a*12+d*4)-(c*12),s)
print("총 세금 =",c*12,s)


