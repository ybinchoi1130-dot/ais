# -*- coding: utf-8 -*-


# from 패키지 import *

from calx import * # cals에 있는 모든 함수, 변수를 사용

# 폴더 이름을 생략하고 사용
# 모듈.함수()
a = 10
b = 20
print(f" 더하기({a} + {b}): ", cals.add(a,b))
print(f"   빼기({b} - {a}): ", cals.sub(b,a))
print(f"     원주율(PI)): {cals.PI}")


