# -*- coding: utf-8 -*-


# from 모듈명 import 목록
# 해당 모듈에서 목록을 지정
# from cals import * 
# from cals import add, sub, PI
from calx.cals import add, sub

# 모듈 이름을 생략하고 사용할 때 
a = 10
b = 20
print(f" 더하기({a} + {b}): ", add(a,b))
print(f"   빼기({b} - {a}): ", sub(b,a))

# NameError: name 'PI' is not defined
# print(f"     원주율(PI)): {PI}")


