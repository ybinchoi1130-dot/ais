# -*- coding: utf-8 -*-

# 클래스(class) : 상속(inheritance)

# 정의
"""
class 자식클래스(부모클래스):
    ...
"""

#%%
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
"""
# 자바(java)
# 상속은 확장의 개념
class School extends Student {
}

# C++
# 상속은 연결의 개념
class School : public Student {
}
"""  

#%%

# 상속
# 자식(School)은 부모(Student)의 속성과 메서드를 상속 받음
# 자식(School)은 pass를 하게 되면 자신의 속성과 메서드는 하나도 없음
# 부모의 속성과 메서드만으로 구성되어 있다.
class School(Student):
    pass

#%%

# 학교 클래스
sc = School()
print(sc.score()) # ('이름없음', 0, 0, 0)
 
#%%

sc = School('전교생')
print(sc.score()) # ('전교생', 0, 0, 0)

#%%

sx = School("연세학원")
print('id:', hex(id(sx)))
print(sx.score())

#%%
#빈 함수 
def space():
    pass

sp=space()
print(sp,id(sp))

#%%
# 빈 클래스
class Space:
    pass

spc=Space()

print(spc)



