# -*- coding: utf-8 -*-

# 함수(Function)

# 기본값: default value
# 파라미터 : z의 기본값은 5
# 호출할 때 값을 전달하지 않으면 기본값으로 처리

#%%
def move(x, y, z=5):
    print(f"move: x({x}), y({y}), z({z})")
    
    
#%%

# 함수 move()를 호출할 때 z에 해당하는 인자는 생략 가능
move(10, 20)        # x(10), y(20), z(5)

#%%

move(10, 20, 30)    # x(10), y(20), z(30)

#%%

move(x=1, y=2, z=3) # x(1), y(2), z(3)