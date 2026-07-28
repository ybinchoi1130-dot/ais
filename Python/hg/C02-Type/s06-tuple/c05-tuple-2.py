# 튜플(Tuple)

jobs = ('요리사', '교사', '사무원')
print(jobs)

# 언패킹(unpacking)
# 언패킹된 변수는 개별 요소의 자료형이다.
chef, teacher, officer = jobs
print(type(chef), chef)       # 요리사
print(type(teacher), teacher) # 교사
print(type(officer), officer) # 사무원

#%%

# 언패킹
# 요소의 갯수가 일치해야 한다.
# 생략: 언더스코어(_)
_, _, off = jobs
print(off) # 사무원

#%%

# 언패킹: 요소의 갯수가 일치해야 한다.
# ValueError: too many values to unpack (expected 2)
tech, off = jobs


#%%

abc = ('홍길동', 34, jobs)
a, b, c = abc
print(type(a), a) # <class 'str'> 홍길동
print(type(b), b) # <class 'int'> 34
print(type(c), c) # <class 'tuple'> ('요리사', '교사', '사무원')

#%%

# 바꿀 없다.
# c[0] = '조리사'
print(c, jobs)

#%%

abc = ('홍길동', 34, jobs)
a, b, (c, d, e) = abc
print(type(a), a) # <class 'str'> 홍길동
print(type(b), b) # <class 'int'> 34
print(type(c), c) # <class 'str'> 요리사
print(type(d), d) # <class 'str'> 교사
print(type(e), e) # <class 'str'> 사무원





