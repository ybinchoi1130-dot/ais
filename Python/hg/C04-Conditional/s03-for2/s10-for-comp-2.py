# 리스트 내포 사용하기
# [표현식 for 항목 in 반복 기능 객체 if 조건]
#
# [표현식 for 항목1 in 반복 기능 객체1 if 조건1
#         for 항목2 in 반복 기능 객체2 if 조건2
#         ...
#         for 항목n in 반복 기능 객체n if 조건n]

#
a = [1,2,3,4,5,6]
result = []
for num in a:
    if num % 2 == 0:
        result.append(num * num)

print(result)   

# 리스트 내포 사용
result2 = [n * n for n in a if n % 2 == 0] # 짝수만 처리
print(result2)