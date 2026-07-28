# if
# 우선순위

a = 10
b = 3
print(a / b * b)

# 산술연산자가 비교연산자 보다 우선 순위가 높다.
if a // b * b != a:
    print('a=', a) 
    print('b=', b)
    print('c=a/b', a/b)
    print('(a // b * b) ', a // b * b)
else:
    print('none')
