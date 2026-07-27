# 반복문(for)
# range(시작, 끝) 
#   - 시작부터 끝까지 연속적인 숫자를 생성

# 0부터 10까지 합
n = 10 + 1
sum = 0
for cnt in range(n): # 0부터 10까지
    sum += cnt
    print(f"cnt={cnt}, sum={sum}")

print('sum=', sum) # 55
