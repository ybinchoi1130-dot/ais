# -*- coding: utf-8 -*-

# 파일이름: cals-test.py

# 모듈을 임포트(import)
# cals.py 파이썬 코드를 사용 가능하도록 임포트
# 모듈명.함수(), 모듈명.변수

# 해당 모듈(cals.py)을 로드 즉 임포트해서 사용
import cals

print("[작업시작] __name__ : ", __name__)

a = 10
b = 20
print(f" 더하기({a} + {b}): ", cals.add(a,b))
print(f"   빼기({b} - {a}): ", cals.sub(b,a))
print(f"원주율({cals.PI}): ", cals.PI)


