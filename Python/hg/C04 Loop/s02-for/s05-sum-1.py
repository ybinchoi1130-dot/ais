# 반복문(for)
# range(시작, 끝) 
#   - 시작부터 끝까지 연속적인 숫자를 생성

# 0부터 10까지 합
n = 10 + 1
tot = 0
for cnt in range(n): # 0부터 10까지
    tot += cnt
    print(f"cnt={cnt}, tot={tot}")

print('tot=',tot) # 55
#%%
n = 10 
tot = 0
for cnt in range(n): # 0부터 10까지
    tot += cnt +1
    print(f"cnt={cnt}, tot={tot}")

print('tot=',tot) # 55
