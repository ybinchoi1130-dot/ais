# 제어문(if)
# x in s
# x not in s

# 튜플
s = (1,3,5,7,9)
print("튜플:", s)

# 튜플안에 해당하는 값이 존재하는지 확인
x = 6
b = x in s

print('bool=', b)

if b:
    print(f'튜플 s에 값({x})가 있다')
else:
    print(f'튜플 s에 값({x})가 없다.')

