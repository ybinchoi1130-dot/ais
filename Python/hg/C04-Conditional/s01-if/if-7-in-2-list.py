# 제어문(if)
# x in s
# x not in s

# 리스트
s = [1,3,5,7,9]

# 리스트안에 해당하는 값이 존재하는지 확인
# x = 6
x = 7
b = x in s

print('bool=', b)       # True
print('type=', type(b)) # bool

if b:
    print(f'리스트 s에 값({x})가 있다')
else:
    print(f'리스트 s에 값({x})가 없다.')

