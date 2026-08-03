# -*- coding: utf-8 -*-

# 클래스(class) : 사용자 자료형
# 객체지향 프로그래밍: 객체, 인스턴스
# 클래스: 속성, 함수를 하나의 묶음으로 처리
# 속성: 동일한 자료들의 그룹, 멤버 변수, 공개(정보은폐를 지원하지 않음)
# 함수: 멤버 함수, 메서드, 멤버 변수에 접근할 수 있는 함수
# self: 생성된 객체의 식별자
# 메서드를 호출할 때는 self를 생략
# 멤버변수(속성):
#   - 멤버변수가 생성: self.이름 = 초깃값    
#   - 멤버변수가 참조: self.이름
# 생성자(constructor) : __init__(self)
#   - 객체가 생성될 때 가장 먼저 실행되는 메서드
# 소멸자(destructor) : __del__(self)
#   - 객체가 소멸될 때 맨 마지막에 실행되는 메서드
# 멤버의 메서드를 호출: 
#   - self.메서드()

#%%
# 함수형 프로그램으로 바꾸어라
#
def Student(name='아무개',basescore=0):
    tot = basescore
    def score(kor=0,eng=0,sci=0):
        nonlocal tot
        tot += kor
        tot += eng
        tot += sci
        avg = tot // 3
        print(f"나의 이름은 '{name}'입니다.")
        print(f"\t 국어 : {kor}")
        print(f"\t 영어 : {eng}")
        print(f"\t 과학 : {sci}")
        return tot,avg

    return score
#%%        



who0 = Student()
who1 = Student('홍길동', 0 )    # 이름, 국어
who2 = Student('강감찬', 0) # 이름, 국어, 영어

print(who0())
print(who1(60,90,90))
print(who2(90,90,95))