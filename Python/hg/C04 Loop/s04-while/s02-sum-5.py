# 반복문(while)

# [문제]
# 반복문(while)을 사용하여 1부터 100까지 홀수의 합과 짝수의 합을 각각 구하라.
# 1부터 100까지 숫자는 1씩 증가한다. (1,2,3,4,5,.... 99, 100)
# 나머지 연산자(%)를 사용하지 않고 계산하라.
# 정수 나눗셈(//)을 이용하라.

count =1
osum=0
esum=0

while count <= 100:
    if (count // 2)*2 == count:
        esum += count
        count += 1
    else :
        osum += count
        count += 1
        
print("홀수의 합 =",osum)
print("짝수의 합 =",esum)