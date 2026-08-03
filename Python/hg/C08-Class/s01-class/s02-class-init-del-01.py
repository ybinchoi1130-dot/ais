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
# 클래스 정의
# 학생 정보를 다루는 전용 클래스
# 속성: 이름, 점수(국어, 영어, 수학)
class Student:
    def __init__(self, sid='이름없음', kor=0, eng=0, math=0): # 생성자(constructor)
        print(f"[생성자] {self}")
        self.sid = sid
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def __del__(self): # 소멸자(destructor)
        print(f"[소멸자] {self}")
        
    def name(self, val):
        self.sid = val
    
    def korean(self, val):
        self.kor = val
        
    def english(self, val):
        self.eng = val
        
    def maths(self, val):
        self.math = val
        
    def score(self):
        return self.sid, self.kor, self.eng, self.math
    
    def total(self):
        return self.kor + self.eng + self.math
    
    def avg(self):
        return self.total() // 3 
        
#%%        

# 소멸자 호출 방법
# 2번 이상 연속해서 실행

# 학생(Student) 클래스 선언
s1 = Student('홍길동', 90)    # 이름, 국어
print(s1.score())

#%%

# 소멸자 호출 방법
# 객체가 생성된 변수에 새로운 객체를 생성

s1 = Student('강감찬', 100,100) # 이름, 국어, 영어
print(s1.score(), s1.total(), s1.avg())

#%%

# 강제로 객체를 제거하면 소멸자가 호출된다.
del s1
