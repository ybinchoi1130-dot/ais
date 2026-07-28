# 반복문(for)
#직접 사용하는것은 일회성인 코드들
# 튜플
for al in 1,3,5,6,"end!":
    print(al)
    
#%%    

# 리스트
for item in [1,3,5,6,"end!"]:
    print(item)

#%%
# 문자열
for item in "Hello, World!":
    print(item,end=', ')
#%%
#방법1
text = "abcdefg" 
for item in text[:-1]:
    print(item, end=', ')
print(text[-1])
#%%
text = "abcdefg"
last_tx = len(text)-1
for cnt, it in enumerate(text):
    if cnt == last_tx:
        print(it)
    else :
        print(it, end=', ')
 
#%% 
#문자열 함수를 이용한 방법
text = "abcdefg" 
print(", ".join(text))
#%%
#for in 한줄코드로 사용
print(", ".join([it for it in "abcdefg"]))
