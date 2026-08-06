# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:18:02 2024

@author: Solero
"""

# eval()
# evaluate의 약자
# 문자열로 구성된 표현식(expression)을 입력으로 받아서 실행
# 문자열로 구성된 파이썬 코드를 실행
# 파이썬 코드를 외부에 만들어 놓고 읽어서 동적으로 처리할 때 사용

expr = "10 + 20"

print(expr)       # 문자열 출력: 10 + 20
print(eval(expr)) # 처리 결과: 30
print(eval("divmod(10,3)")) # (3, 1)

#%%

a = 3
b = 5
c = a * b
x = eval("f'c={c}'")
print(x) # c=15