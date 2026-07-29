# 반복문(for)

# [문제]
# 아래와 같이 피라미드 형태로 출력을 하라.
#   - 다중 루프(for)를 이용하라
#   - 문자열 곱하기를 이용하라.
'''
1:    *
3:   ***
5:  *****
7: *******
9:*********
'''

#%%
sn=1
end=10

for n in range(sn,end,2):
    st = '*' * n
    print(f"{n}: {st:^9}")
    
#%%
tot =  9
for n in range(1,tot+1,2):
    x=(tot-n)//2
    print(f"{n}: ",end='')
    for _ in range(x): #공백출력
        print(' ', end='')
    for _ in range(n): #'*' 출력
        print('*', end='')
    print()