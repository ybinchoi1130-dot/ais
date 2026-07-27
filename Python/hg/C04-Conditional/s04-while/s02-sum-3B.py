# 반복문(while)


# [문제]
# 반복문(while)을 사용하여 1부터 100까지 짝수의 합을 구하라.

cnt = 2
sum = 0

while cnt <= 10: # 2,4,6,8,10 ... 98, 100
    print('cnt=', cnt)
    sum += cnt
    cnt += 2

print('sum=', sum)

