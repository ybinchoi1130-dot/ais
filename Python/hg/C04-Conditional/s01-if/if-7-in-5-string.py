# 제어문(if)
# x in s
# x not in s

# 문자열
s = "Hello, World!"
print("문자열:", s)

# 문자열안에 해당하는 값이 존재하는지 확인
x = 'World'
y = '.'

print(f'rx({x})=', x)
print(f'ry({y})=', y)

if x in s or y in s:
    print(f'문자열 s에 값({x}) 또는 값({y})가 있다')
else:
    print(f'문자열 s에 값({x}, {y})가 없다.')


# 괄호로 묶어서 구분
b = (x in s) or (y in s)
print(b)
if b == True:
    print(f'문자열 s에 값({x}) 또는 값({y})가 있다')
else:
    print(f'문자열 s에 값({x}, {y})가 없다.')

