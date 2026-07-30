# -*- coding: utf-8 -*-

# 함수(Function)

# 가변인자
# 키워드 매개변수(kwargs)
# 호출할 때 반드시 인자에 키를 명시해야 한다.
# 인자: 키=값
#%%

# 파라미터 : dict로 받음
def move(**kwargs):
    print(f"[move] type:{type(kwargs)}, {kwargs}")
    for key in kwargs.keys():
        print(f"key={key}, value={kwargs[key]}")
    

#%%

# 호출할 때 반드시 인자에 파라미터를 명시해야 한다.
# TypeError: move() takes 0 positional arguments but 3 were given
move(1,2,3)

#%%

# 파라미터를 명시적으로 지정을 해야 한다.
move(x=10, y=20) # <class 'dict'>, {'x': 10, 'y': 20}

#%%

move(x=10, y=20, z=30) # <class 'dict'>, {'x': 10, 'y': 20, 'z': 30}

#%%
move(a=10, b=20, c=30) # <class 'dict'>, {'a': 10, 'b': 20, 'c': 30}
    