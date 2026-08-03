# -*- coding: utf-8 -*-

# 클래스(class) : 상속(inheritance)
# 부모의 속성에 접근: self.속성
# 부모의 메서드에 접근 
#   -self.메서드() : 자신을 포함한 모든 조상 
#   -super().메서드() : 모든 조상 즉 위로부터 받아온다.

# 정의
"""
class 자식클래스(부모클래스):
    ...
"""

#%%
class Student:
    def __init__(self, sid='이름없음', kor=0, eng=0, math=0): # 생성자(constructor)
        print(f"[Student] 생성자: {self}")
        self.sid = sid
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def __del__(self): # 소멸자(destructor)
        print(f"[Student] 소멸자: {self}")
        
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

# 상속
# 자식이 자신의 생성자를 정의하면 더 이상 부모의 생성자가 자동으로 호출되지 않는다.
# 부모 생성자 호출 : 자식 생성자에서만 호출 가능
class School(Student):
    def __init__(self, name, kor, eng, math):
        print(f"[School] 생성자: {self}")
        super().__init__(name, kor, eng, math) # 부모 생성자 호출

    def score(self): # 메서드를 재정의(오버라이딩): 대체
        print(f"[School] score")
        return self.sid, self.kor, self.eng, self.math, self.total(), self.avg()
       # 동일한 결과
       # return self.sid, self.kor, self.eng, self.math, super().total(), super().avg()

#%%

# 학교 클래스
sc = School('고길동', 60,50,40)

#%%

# 부모 생성자에서 만들 속성들을 사용할 수 있게 됨
print(sc.score()) # ('고길동', 60, 50, 40, 150, 50)
 
