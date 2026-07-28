# 리스트에서 요소의 값이 있는 위치를 리턴 
# 인덱스 = 리스트.index(값)
# 가장 먼저 찾은 위치를 리턴

lst = ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']
print(lst)

value = 'LG'
index = lst.index(value)
found = (value == lst[index])

print("value:", value) # LG
print("index:", index) # 1
print("found:", found) # True

#%%

# 두 번째에 위치한 값('LG')을 찾으려면? 
value = 'LG'
index = lst.index(value) # 첫 번째 위치
index = lst.index(value, index + 1) # 두 번째 위치
found = (value == lst[index])
print("value:", value) # LG
print("index:", index) # 3
print("found:", found) # True


#%%


# 찾지 못하면?
# 예외가 발생하며 강제 종료된다.
# ValueError: '현대' is not in list
notfound = lst.index('현대')


