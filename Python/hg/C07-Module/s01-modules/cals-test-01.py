# -*- coding: utf-8 -*-

# 파일이름: cals-test.py

# 모듈을 임포트(import)
# cals.py 파이썬 코드를 사용 가능하도록 임포트

# import 모듈이름 as 별칭
# 별칭.함수(), 별칭.변수

import cals as cs

a = 10
b = 20
print(f" 더하기({a} + {b}): ", cs.add(a,b))
print(f"   빼기({b} - {a}): ", cs.sub(b,a))
print(f"     원주율(PI)): {cs.PI}")


