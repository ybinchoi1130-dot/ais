# -*- coding: utf-8 -*-

# 문자열 연산
#   - 더하기 : +
#   - 곱하기 : *

#%%
# 문자열 더하기(+)
# 문자열을 붙이기(결합)
hello = "Hello"
world = "World"
helloworld = hello + ', ' + world + '!'
print(hello)
print(world)
print(helloworld)

#%%

# 복합대입 연산자(+=)
hw = ''   # 빈 문자열
hw += hello
hw += ', '
hw += world
hw += '!'
print(hw)

#%%

# hw2 = hw2 + hello
# 위와 같은 형태는 먼저 hw2를 참조하기 때문에
# 먼저 hw2 변수가 선언 되어 있어야 한다.
hw2 = ''
hw2 = hw2 + hello
hw2 = hw2 + ', '
hw2 = hw2 + world
hw2 = hw2 + '!'
print(hw2)





