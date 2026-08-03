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
# 생성자(constructor)
#   - 객체가 생성될 때 가장 먼저 실행되는 메서드
# 멤버의 메서드를 호출: 
#   - self.메서드()

#%%
# 클래스 정의
# 학생 정보를 다루는 전용 클래스
# 속성: 이름, 점수(국어, 영어, 수학)
class Student:
    def __init__(self, sid='이름없음', kor=0, eng=0, math=0): # 생성자(constructor)
        self.sid = sid
        self.kor = kor
        self.eng = eng
        self.math = math
    def who(self):
        print(f"나의 이름은 '{self.sid}'입니다.")
        
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

# 학생(Student) 클래스 선언
s1 = Student('홍길동', 90)    # 이름, 국어, 영어(0), 수학(0)
print(s1.score()) # ('홍길동', 90, 0, 0)

#%%

s2 = Student('강감찬', 100,100) # 이름, 국어, 영어, 수학(0)
print(s2.score(), s2.total(), s2.avg()) # ('강감찬', 100, 100, 0) 200 66

#%%

s3 = Student('이순신', 100,100,100) # 이름, 국어, 영어, 수학
print(s3.score(), s3.total(), s3.avg()) # ('이순신', 100, 100, 100) 300 100

