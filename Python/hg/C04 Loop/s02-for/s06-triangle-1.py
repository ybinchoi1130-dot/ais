# 반복문(for)

# [문제]
# 1부터 5까지 증가하면서 *를 동일한 라인에 출력
'''
1:*
2:**
3:***
4:****
5:*****
'''
#%%

for n in range(1,6):
    st='*'*n
    print(f"{n} :{st}")
    
#%%
for n,st in enumerate(range(5),1):
     st='*'*n
     print(f"{n}:{st}")