# 리스트 요소 꺼내기
# 값 = 리스트.pop(index)
# 인덱스에 해당하는 위치의 요소 값을 리턴하고 꺼낸 요소는 삭제된다.

lst = ['DB', 'LG', 'SM', 'IBM', '삼성']
print('작업전:', lst)

# 특정한 위치의 요소를 꺼냄
index = 3
value = lst.pop(index)
print(f"'{value}' = lst.pop({index})")
print('작업후:', lst)

#%%

# 인덱스의 범위를 넘어 서면?
# IndexError: pop index out of range
index = len(lst)
value = lst.pop(index)
print(f"'{value}' = lst.pop({index})")
print('작업후:', lst)

#%%

# 맨 마지막 요소를 꺼냄
index = len(lst) - 1
value = lst.pop(index)
print(f"'{value}' = lst.pop({index})")
print('작업후:', lst)
