# 리스트 삭제
# 요소에서 해당하는 값을 찾아서 삭제
# 해당하는 값 첫번째 요소를 삭제
# 리스트.remove(값)

lst = ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']
print(lst) # ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']

lst.remove('LG')
print(lst) # ['DB', 'SM', 'LG', 'IBM', '삼성'] 

#%%

# [문제]
# 'IBM'을 del을 이용해서 삭제하라.
# del 리스트[인덱스]
ibm = lst.index('IBM')
del lst[ibm]
print(lst) # ['DB', 'SM', 'LG', '삼성']