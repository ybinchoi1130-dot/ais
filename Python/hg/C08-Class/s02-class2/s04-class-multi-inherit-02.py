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
        
    def printval(self, val):
        self.cnt += 1
        print(f"[A] cnt({self.cnt}), val({val})")
        
#%%

class B:
    def __init__(self, val):
        self.cnt = val
        
    def printval(self, val):
        self.cnt += 10
        print(f"[B] cnt({self.cnt}), val({val})")
        
#%%

# 다중상속
# 명시하지 않고 부모의 속성이나 메서드를 사용할 때
# 기본적으로 선택되는 부모는 먼저 상속한 부모의 것을 사용한다.
class C(B,A):
    def count(self):
        return self.cnt # 어떤 부모의 속성? 부모(B)

class D(A,B):
    def count(self):
        return self.cnt  # 어떤 부모의 속성? 부모(A)

#%%

c = C(1)
c.printval(10) # [B] cnt(11), val(10)
print('count:', c.count())

#%%
d = D(2)
d.printval(20) # [A] cnt(3), val(20)
print('count:', d.count())
       