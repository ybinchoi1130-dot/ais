# 리스트 확장
# 리스트.extend(리스트)
# 리스트 더하기(+) 연산자와 동일하다.

l1 = ['DB', 'LG', 'SM']
l2 = ['LG', 'IBM', '삼성']
print(l1)
print(l2)

l1.extend([l2])
print(l1) # ['DB', 'LG', 'SM', ['LG', 'IBM', '삼성']]


#%%

# 리스트 더하기(+) 연산자와 동일하다.
l2 += [['HD', 'SK']]
print(l2) # ['LG', 'IBM', '삼성', ['HD', 'SK']]


