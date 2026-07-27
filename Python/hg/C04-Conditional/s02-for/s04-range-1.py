# 반복문(for)
# range(시작, 끝, [, 간격]) 
#   - 시작부터 끝까지 연속적인 숫자를 생성
#   - 간격: 옵션, 증가값

# 0부터 9까지 숫자를 생성(n-1)
n = 10   # 종료값
ten = range(n)

#%%
print(ten)

#%%

for cnt in ten: # 0, 1, 2, ..., 8, 9
    print(cnt)