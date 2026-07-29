# 반복문(while)


# [문제]
# 반복문(while)을 사용하여 1부터 100까지 짝수의 합을 구하라.

count = 1
sum = 0
while count <= 100:
    if count % 2 == 0:
        sum += count
        count += 1
    else: 
        count += 1
        
print("sum =",sum)
print('end')
