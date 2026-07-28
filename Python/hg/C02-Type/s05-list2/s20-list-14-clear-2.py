# 리스트에서 모든 요소를 제거
# 리스트.clear()

import sys

l1 = ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']
l2 = l1

print('l1:', hex(id(l1)), sys.getrefcount(l1), l1) # 참조 카운트 : 3
print('l2:', hex(id(l2)), sys.getrefcount(l2), l2) # 참조 카운트 : 3

#%%

l1 = []  # 참조 카운트 : 2
l3 = l1  # 참조 카운트 : 3
l4 = l3  # 참조 카운트 : 4

print('l1:', hex(id(l1)), sys.getrefcount(l1), l1) # 참조 카운트 : 4
print('l2:', hex(id(l2)), sys.getrefcount(l2), l2) # 참조 카운트 : 2

