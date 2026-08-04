# 인스턴스(instance)
# 자료형이 객체화 된 상태를 인스턴스라 한다.
# 객체(object) : 고유한 자료의 실체

# 원주율
pi = 3.14

print("자료형:", type(pi)) # <class 'float'>

#%%

tpi = type(pi)
print('type(pi)', type(tpi)) # <class 'type'>

#%%

spi = str(type(pi))
print("spi:", spi)

#%%

# instance
print('instance:', isinstance(pi, float)) # True
print('instance:', isinstance(pi, tpi))   # True
print('instance:', isinstance(pi, type(pi)))

