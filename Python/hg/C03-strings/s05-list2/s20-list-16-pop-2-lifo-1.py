# 리스트 요소 꺼내기
# 리스트.pop()
# 주의: 꺼낸 요소는 삭제된다.
# LIFO(Last In First Out)
# 후입선출: 스택(Stack)
# 나중에 들어온 것을 먼저 꺼냄

lst = ['DB', 'LG', 'SM', 'IBM', '삼성']

# 리스의 pop() 함수에 인자를 주지않으면?
# 가장 마지막 요소를 꺼냄
print(lst.pop()) # 삼성
print(lst.pop()) # IBM
print(lst.pop()) # SM
print(lst.pop()) # LG
print(lst.pop()) # DB

#%%

# IndexError: pop from empty list
print(lst.pop()) # ?
