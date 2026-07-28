# if
# 우선순위

a = 10
b = 3
print(a / b * b)

# 복잡한 수식이 있는 경우는 미리 계산한 후에 변수에
# 담아서 비교하는 것이 좋다.
r = a // b * b
print('r=', r)

if r != a:
    print('a=', a) 
    print('b=', b)
    print('c=a/b', a/b)
    print('(a // b * b) ', a // b * b)
else:
    print('none')
