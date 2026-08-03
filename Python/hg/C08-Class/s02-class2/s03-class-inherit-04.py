# -*- coding: utf-8 -*-

# 클래스(class) : 상속(inheritance)

# 정의
"""
class 자식클래스(부모클래스):
    super().__init__() # 부모 생성자 호출
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

# 부모 생성자 호출
# super().__init__()
# ※ 부모의 생성자를 호출할 때는 부모 생성자의 파라미터에 맞게
#   인자를 전달해야 한다.(함수의 특성과 동일하다)
class School(Student):
    def __init__(self):
        print(f"[School] 생성자: {self}")
        # super().__init__() # 부모 생성자 호출
        # super().__init__('아무개') # 부모 생성자 호출
        super().__init__(sid='아무개', math=99) # 부모 생성자 호출


#%%

# 학교 클래스
sc = School()

#%%

# 부모 생성자에서 만든 속성들을 사용할 수 있게 됨
# print(sc.score()) # ('이름없음', 0, 0, 0)
print(sc.score()) # ('아무개', 0, 0, 99)
 
