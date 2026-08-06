# 예외처리(Exception)
# IndexError

lst = [1,3,5]

l1 = lst[0]
l3 = lst[1]
l5 = lst[2]

# IndexError: list index out of range
l7 = lst[3]


#%%

try:
    index = 3
    val = lst[index]
# except IndexError as e:
except IndexError:
    print(f"리스트의 {index}번째를 참조하려 했습니다.")
    

#%%


