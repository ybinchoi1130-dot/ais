# 인스턴스(instance)
# 자료형이 객체화 된 상태를 인스턴스라 한다.
# 객체(object) : 고유한 자료의 실체

#%%

class Parent:
    pass
class Child(Parent):
    pass

P=Parent()
C=Child()

print("P=",isinstance(P,Parent))
print("C=",isinstance(C, Child))
print("C=",isinstance(C, Parent))
print("P=",isinstance(P, Child))