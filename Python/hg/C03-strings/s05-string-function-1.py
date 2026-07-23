# -*- coding: utf-8 -*-

# 문자열 관련 함수들(functions)
#   - 문자열  클래스 멤버 함수, 또는 메서드(method)
#   - 메서드: 특정 클래스에 종속되어 있는 전용 함수

# 결과 = 문자열.함수()
#   cnt = str.count('x')
#
# 문자열 전용 메서드(method)
# count(), find(), index(), join(), upper(), lower()
# lstrip(), rstrip(), strip(), replace(), split()

# String Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods

#%%
# 1. 클래스(설계도) 정의 ➡️ "붕어빵은 이런 맛과 모양을 가질 거야"
class FishBread:
    def __init__(self, taste):
        self.taste = taste  # 특징 (속성)
        
    def eat(self):          # 기능 (메서드)
        print(f"{self.taste} 붕어빵을 한 입 먹었습니다!")

# 2. 객체(실체) 생성 ➡️ 설계도를 사용해 진짜 붕어빵 두 개를 구워냄
bread_A = FishBread("팥")
bread_B = FishBread("슈크림")

# 3. 객체 사용
bread_A.eat()  # 출력: 팥 붕어빵을 한 입 먹었습니다!
bread_B.eat()  # 출력: 슈크림 붕어빵을 한 입 먹었습니다!
