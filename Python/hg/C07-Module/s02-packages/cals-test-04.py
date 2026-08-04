# -*- coding: utf-8 -*-

# 모듈에서 함수나 변수의 이름을 변경해서 사용할 수 있다.

# from 모듈명 import 함수 as 별칭
# from 모듈명 import 변수 as 별칭

from calx.cals import PI as pi
from calx.cals import add as plus
from calx.cals import sub as minus 

a = 10
b = 20
print(f" 더하기({a} + {b}): ", plus(a,b))
print(f"   빼기({b} - {a}): ", minus(b,a))
print(f"     원주율(PI)): {pi}")


