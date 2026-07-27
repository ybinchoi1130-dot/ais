# 제어문(if)
# x in s
# x not in s

# 리스트
s = [1,3,5,7,9]

b = 6 not in s
print(f'(b = 6 not in s) -> {b}') # True

# 리스트안에 해당하는 값이 존재하는지 확인
if 6 not in s: # 6이 s안에 없으면 참
    print('리스트 s에 값(6)가 없다')
else:
    print('리스트 s에 값(6)가 있다.')

