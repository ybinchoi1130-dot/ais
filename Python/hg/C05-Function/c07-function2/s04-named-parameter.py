# -*- coding: utf-8 -*-

# 함수(Function)
# 매개변수를 지정하여 호출하기(named parameter)
#   - 함수를 호출할 때 함수에 정의되어 있는 파라미터를 명시적으로 지정하여 호출
#   - 인자의 순서를 무시하고 전달할 수 있다.

#%%

# 함수(function) 정의(define)
def move(x, y, z):
    print(f"x={x}, y={y}, z={z}")
    
#%%

# 함수 호출
# 순서 대로 인자를 지정
move(10, 20, 30)    # x=10, y=20, z=30


#%%

# 함수 호출
# 매개변수를 지정하여 호출하기
# 매개변수 전체의 이름 지정
move(z=33, x=11, y=22) # x=11, y=22, z=33


#%%

# 매개변수를 일부만 지정하여 호출하기
# 지정되지 않은 인자는 순서대로 호출
move(1, z=3, y=2)       # x 생략
move(110, 120, z=130)   # x, y 생략

#%%

# 생략하는 매개변수는 지정순서가 앞에서부터 지정해야 한다.
# SyntaxError: positional argument follows keyword argument
move(z=30, 10, 20 )   # x,y 생략

#%%

# SyntaxError: positional argument follows keyword argument
move(y=20, 10, z=30) # x 생략

#%%

# SyntaxError: positional argument follows keyword argument
move(10, y=20, 30)   # x,z 생략




