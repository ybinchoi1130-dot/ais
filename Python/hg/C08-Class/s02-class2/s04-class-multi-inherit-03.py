# -*- coding: utf-8 -*-

# 다중상속
#
# 상속: 속성, 메서드를 상속

# 상속된 부모 클래스에서 동일한 속성과 메서드가 있으면?
#   -> 먼저 상속된 클래스의 메서드가 사용된다.
#   -> 먼저 상속된 클래스의 속성을 사용한다.

#%%

class A:
    def __init__(self, val):
        self.cnt = val
        
    def count(self, val): # 인자로 받을 값을 증가
        self.cnt += val
        print(f"[A] self({self}), count={self.cnt}")
        
    def printval(self, val):
        print(f"[A] self({self}), cnt({self.cnt}), val({val})")
        
#%%

class B:
    def __init__(self, val):
        self.cnt = val

    def count(self):  # 무조건 1씩 증가
        self.cnt += 1
        print(f"[B] self({self}), count={self.cnt}")
        
    def printval(self, val):
        print(f"[B] self({self}), cnt({self.cnt}), val({val})")
        
#%%

# 다중상속
# 명시적으로 부모를 지정: 부모클래스.메서드(self, ...)
# 여러 부모에 동일한 이름으로 있는 속성은 하나로 처리한다.
class C(B, A):
    def count(self, val): # 재정의
        print(f"[C] self({self}), count={self.cnt}")
        
        # 다중 상속인 경우 명시적으로 부모를 지정해야 한다.
        # TypeError: B.count() takes 1 positional argument but 2 were given
        # 부모(A)의 count()를 호출하려고 의도 했지만 부모(B)를 상속
        # super().count(val) 
        
        # 가능: 부모 B.count()
        # super().count() 
        
        A.count(self,val) # 명시적으로 부모(A)를 지정
        return self.cnt   # 어떤 부모의 속성? 부모(B)

#%%

# 부모 A, B를 상속받은 클래스 C에서
# self : A, B, C의 인스턴스가 하나이다. 즉 C의 인스턴스이다.

c = C(1)
cnt = c.count(7)
c.printval(10)     # [B] cnt(8), val(10)
print('cnt=', cnt) # cnt= 8

#%%

# B의 메서드를 호출할 수 있는가?
# 즉 메서드 오버로딩(중복)을 지원하지 않는다.
# C에서 count()를 재정의 했기 때문에 ...
# TypeError: C.count() missing 1 required positional argument: 'val'    
# c.count()

