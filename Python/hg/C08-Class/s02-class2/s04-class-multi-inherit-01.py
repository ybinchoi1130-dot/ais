# -*- coding: utf-8 -*-

# 다중상속
#
# 상속: 속성, 메서드를 상속

# 상속된 부모 클래스에서 동일한 메서드가 있으면?
#   -> 먼저 상속된 클래스의 메서드가 사용된다.

#%%

class A:
    def printval(self, val):
        print("[A] val=", val)
        
#%%

class B:
    def printval(self, val):
        print("[B] val=", val)
        
#%%

# 다중상속
class C(B,A):
    pass

class D(A,B):
    pass

#%%

c = C()
c.printval('C(B,A)') 

#%%
d = D()
d.printval('D(A,B)')
       