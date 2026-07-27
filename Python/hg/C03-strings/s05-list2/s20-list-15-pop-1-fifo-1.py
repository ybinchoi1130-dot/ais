# 리스트 요소 꺼내기
# 리스트.pop()
# 주의: 꺼낸 요소는 삭제된다.
# FIFO(First In First Out)
# 선입선출: 큐(Queue)
# 먼저 들어온 것을 먼저 꺼냄

lst = ['DB', 'LG', 'SM', 'IBM', '삼성']

print(lst.pop(0)) # DB
print(lst.pop(0)) # LG
print(lst.pop(0)) # SM
print(lst.pop(0)) # IBM
print(lst.pop(0)) # 삼성

#%%
# IndexError: pop from empty list
print(lst.pop(0)) # ?
