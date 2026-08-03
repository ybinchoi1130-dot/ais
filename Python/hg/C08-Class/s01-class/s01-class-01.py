# -*- coding: utf-8 -*-

# 클래스(class)
# - 설계도(blue print)
# 객체지향 프로그래밍: 객체, 인스턴스
# 클래스: 속성, 함수를 하나의 묶음으로 처리
# 속성: 동일한 자료들의 그룹, 멤버 변수, 공개(정보은폐를 지원하지 않음)
# 함수: 멤버 함수, 메서드, 멤버 변수에 접근할 수 있는 함수
# self: 생성된 객체의 식별자
# 메서드를 호출할 때는 self를 생략
# 멤버변수(속성):
#   - 멤버변수 생성: self.이름 = 초깃값    
#   - 멤버변수 참조: self.이름

#%%
# 클래스 정의
# 학생 정보를 다루는 전용 클래스 
# 속성: 이름, 점수(국어, 영어, 수학)
class Student:
    def who(self):
        print("나는 학생입니다.")
        
    def name(self, val): #setter
        self.sid = val
    
    def korean(self, val): #setter
        self.kor = val
        
    def english(self, val): #setter
        self.eng = val
        
    def maths(self, val): #setter
        self.math = val
        
    def score(self): #getter
        return self.sid, self.kor, self.eng, self.math
        
#%%        

# 학생(Student) 클래스 선언
# 함수를 호출하듯이 클래스 ()
s1 = Student()    # 객체 생성

s1.who()
#%%
# AttributeError: 'Student' object has no attribute 'sid'
print(s1.score())


#%%
# 메서드 호출
s1.name('홍길동') # 객체 멤버 메서드에 접근(세터)
s1.korean(90)
s1.english(80)
s1.maths(70)
print(s1.score()) # ('홍길동', 90, 80, 70)

#%%

# AttributeError: 'Student' object has no attribute 'abc'
s1.abc()





