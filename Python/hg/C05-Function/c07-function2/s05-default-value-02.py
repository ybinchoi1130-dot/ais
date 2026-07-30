# -*- coding: utf-8 -*-

# 함수(Function)

# 기본값: default value
# 기본값 지정은 파라미터의 뒤에서부터 지정해야 한다.

#%%

# 파라미터의 중간을 지정하지 않고 기본값을 지정할 수 없다.
# SyntaxError: parameter without a default follows parameter with a default
def movex(x=10, y, z=5):
    print(f"move: x({x}), y({y}), z({z})")

#%%    

# 기본값은 y, z만 지정
# 파라미터의 뒤에서부터 지정
def move(x, y=20, z=5):
    print(f"move: x({x}), y({y}), z({z})")
    
    
#%%

# x값으로 10을 지정
# y, z 기본값으로 처리
move(10) # x(10), y(20), z(5)




