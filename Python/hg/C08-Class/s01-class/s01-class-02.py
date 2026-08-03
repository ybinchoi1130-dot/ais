# -*- coding: utf-8 -*-

# 클래스(class)
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
#   - 파이썬 인터프리터가 자동으로 호출


#%%
# 클래스 정의
# 학생 정보를 다루는 전용 클래스
# 속성: 이름, 점수(국어, 영어, 수학)
class Student:
    def __init__(self): # 생성자(constructor)
        # 속성
        self.sid = '이름없음'
        self.kor = 0
        self.eng = 0
        self.math = 0
        
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
        
#%%        

# 학생(Student) 클래스 선언
s1 = Student()    # 객체 생성

print(s1.score()) # ('이름없음', 0, 0, 0)

#%%

# NameError: name 'score' is not defined
# score()

#%%

# TypeError: Student.score() missing 1 required positional argument: 'self'
# Student.score()

#%%

# 클래스(Student)에 멤버 메서드(score)에 다른 객체를 전달하면
# Student.score()는 self로 그 객체를 받을 수 있다.
Student.score(s1) # ('이름없음', 0, 0, 0)

#%%

s1.name('홍길동') # 객체 멤버 메서드에 접근(세터)
s1.korean(90)
s1.english(80)
s1.maths(70)
print(s1.score())        # ('홍길동', 90, 80, 70)
print(Student.score(s1)) # ('홍길동', 90, 80, 70)

#%%

Student.name(s1, '전우치')

print(s1.score())        # ('전우치', 90, 80, 70)
print(Student.score(s1)) # ('전우치', 90, 80, 70)

#%%


