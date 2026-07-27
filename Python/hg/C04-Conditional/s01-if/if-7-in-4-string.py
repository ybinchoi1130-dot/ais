# 제어문(if)
# x in s
# x not in s

# 문자열
s = "Hello, World!"
print("문자열:", s)

# 문자열안에 해당하는 값이 존재하는지 확인
x = 'World'
y = '.'
rx = x in s
ry = y in s

print(f'rx({x})=', rx)
print(f'ry({y})=', ry)

if rx and ry:   # 양쪽 다 만족
    print(f'문자열 s({s})에 값({x})과 값({y})가 있다')
elif rx or ry:  # 한쪽만 만족
    print(f'문자열 s({s})에 값({x}) 또는 값({y})이 있다.')
else: # 위 조건에 만족하는 것이 없다.
    print(f'문자열 ({s})s에 값({x})과 값({y})이 없다.')
