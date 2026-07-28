# 반복문(for)
# range(시작, 끝) 
#   - 시작부터 끝까지 연속적인 숫자를 생성

# 1부터 10까지 합
sum = 0
for cnt in range(1, 11): # 1,2,3, ... 10
    sum += cnt
    print(f"cnt={cnt}, sum={sum}")

print('sum=', sum)    
