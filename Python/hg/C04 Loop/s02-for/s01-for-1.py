# 반복문(for)
# for 변수 in 리스트, 튜플, 문자열, ...

lists = ['one', 'two', 'three', 'four']

#%%

print(lists[0])
print(lists[1])
print(lists[2])
print(lists[3])

#%%

# 리스트에 들어 있는 내용의 갯수만큼 반복하면서
# 아이템을 하나씩 꺼내서 변수에 담아준다.
for item in lists: # 4번 반복
    print(item)


#%%

cnt=0
for it in lists:
    cnt +=1
    print(f"{cnt} : {it}")

#%%
for cnt, it in enumerate(lists):
    print(f"{cnt}: {it}")    

#%%
tp= (0,'하나')
inx, val =tp
print(inx,val)
print(tp[0],tp[1])