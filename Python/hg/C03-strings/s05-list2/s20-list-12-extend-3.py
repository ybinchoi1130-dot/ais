# 리스트 확장
# 리스트.extend(리스트)
# 리스트 더하기(+) 연산자와 동일하다.
# list(리스트)하면 변화가 없으며 원래 리스트 자료형이 된다.

l1 = ['DB', 'LG', 'SM']
l2 = ['LG', 'IBM', '삼성']
print(l1)        # ['DB', 'LG', 'SM']
print(l2)        # ['LG', 'IBM', '삼성']
print(list(l2))  # ['LG', 'IBM', '삼성']

#%%

l1.extend(list(l2))
print(l1) # ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']


#%%