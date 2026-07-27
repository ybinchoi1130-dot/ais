# 리스트에 요소 추가 : append()
# 기존에 있는 리스트에 하나의 요소를 추가

lst = []

# 하나의 개별 요소를 맨 뒤에 추가
lst.append(9)
lst.append(8)
lst.append(7)

print(lst)

#%%

# 리스트를 하나의 요소로서 맨 뒤에 추가
lst.append([6,5,4])
print(len(lst), '개: ', lst) # [9, 8, 7, [6, 5, 4]]

