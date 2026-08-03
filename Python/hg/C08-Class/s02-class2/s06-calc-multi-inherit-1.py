# -*- coding: utf-8 -*-

"""
# [전자] 전자계산기
1. 다중 상속을 이용하라.
2. 사칙연산을 수행하는 클래스를 각각 정의
    - 덧셈 클래스
    - 뺄셈 클래스
    - 곱셈 클래스
    - 나눗셈 클래스
3. 최하위 클래스에서 다중상속을 하여 통합
    - 총점, 평균 처리
4. 각 클래스들은 생성자 정의하여 초깃값을 넣어라.   
5. 히스토리를 관리하라.

"""
#%%

class Add:
    def __init__(self,a,b):
        self.add_val=a+b
        
class Sub:
    def __init__(self,a,b):
        self.sub_val=a-b
        
class Mul:
    def __init__(self,a,b):
        self.mul_val=a*b

class Div:
    def __init__(self,a,b):
        if b!=0: 
            self.div_val=a/b
        else:
            self.dic_val=0
            
class Cal(Add,Sub,Mul,Div):
    
    def __init__(self, a, b):
        Add.__init__(self,a,b)
        Sub.__init__(self,a,b)
        Mul.__init__(self,a,b)
        Div.__init__(self,a,b)
        self.histories=[]
        
        self.histories.append(f"{a} + {b} = {self.add_val}")
        self.histories.append(f"{a} - {b} = {self.sub_val}")
        self.histories.append(f"{a} * {b} = {self.mul_val}")
        self.histories.append(f"{a} / {b} = {self.div_val}")
        
    def total(self):
        return  self.add_val+self.sub_val+self.mul_val+self.div_val
    
    def average(self):
        return self.total() / 4
    
    def History(self):
        print("\n [ 계산 히스토리 기록 ]")
        for record in self.histories:
            print(record)
        
    
my_cal= Cal(45, 9)    

print("--- 사칙연산 결과 ---")
print(f"덧셈: {my_cal.add_val}")
print(f"뺄셈: {my_cal.sub_val}")
print(f"곱셈: {my_cal.mul_val}")
print(f"나눗셈: {my_cal.div_val}")

print("\n--- 최종 결과 ---")
print(f"총점: {my_cal.total()}")
print(f"평균: {my_cal.average()}")

my_cal.History()