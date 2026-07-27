# 반복문(while)
# break : 반복문을 중단하고 빠져 나옴

cnt = 1
tot = 0

# 무한루프
# 1부터 100까지 합
# cnt가 100보다 크거나 같으면 탈출
while True:
    tot += cnt
    print(f'cnt={cnt}, tot={tot}')    
    if cnt >= 100:
        break
    cnt += 1

print('tot=', tot)    
