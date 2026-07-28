# 반복문(while)
# break : 반복문을 중단하고 빠져 나옴

cnt = 1
tot = 0

# 무한루프
# 1부터 100까지 합
# cnt가 100보다 크면 탈출
while True:
    if cnt > 100:   # cnt가 101이 되면 루프를 탈출
        break

    tot += cnt
    print(f'cnt={cnt}, tot={tot}')    
    cnt += 1

print('tot=', tot)    
