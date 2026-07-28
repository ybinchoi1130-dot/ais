# 리스트에 요소의 값의 갯수
# 갯수 = 리스트.count(값)
# 리턴: 요소의 갯수, 없으면 zero(0)

lst = ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']
print(lst)

value = 'LG'
count = lst.count(value)

print("value:", value) # 'LG'
print("count:", count) # 2

#%%

# 해당하는 값이 리스트에 존재하지 않으면?
value = 'HD'
count = lst.count(value)

print("value:", value) # 'HD'
print("count:", count) # 0
