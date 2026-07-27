# 반복문(for)
# range(시작, 끝) 
#   - 시작부터 끝까지 연속적인 숫자를 생성

# 1부터 100까지 합
s = 1       # 시작값
n = 100      # 종료값
l = n + 1   # 지정값 = 종료값 + 1
sum = 0
for cnt in range(s, l):
    sum += cnt
    print(f"cnt={cnt}, sum={sum}")

print('sum=', sum)    

#%%

# 수열의 합
n = 100
tot = n * (n + 1) // 2
print('tot=', tot)  # 5050

#%%

# 검증
ctx = sum == tot
print(f'sum({sum}) == tot({tot}) ?', ctx)


