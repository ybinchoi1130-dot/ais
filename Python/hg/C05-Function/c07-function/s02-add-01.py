# -*- coding: utf-8 -*-

"""
함수(Function)
함수정의와 호출은 전달되는 순서, 자료형을 맞춰야 한다.
반환값: 
  - 반환값은 0개 이상    
  - 형식: 
      - return
      - return 값
      - return 값1, 값2, ...
"""
#%%

# 함수 정의
def add(a, b):
    return a + b # 결과리턴

#%%

def mul(a, b):
    c = a * b
    return c # 결과리턴

#%%

# 함수호출
print(add(1,2))    # 3
print(add(10,20))  # 30

#%%
print(mul(1,2))    # 2
print(mul(10,20))  # 200

#%%

# 전달되는 데이터에 따라서 다른 처리 결과가 나올 수 있다.
print(add('ABC', 'DEF')) # ABCDEF
print(mul('*', 10))      # **********

#%%

# TypeError: can't multiply sequence by non-int of type 'str'
print(mul('*', '-'))      

#%%

# TypeError: can only concatenate str (not "int") to str
print(add('ABC', 10)) 



