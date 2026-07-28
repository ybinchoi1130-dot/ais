# 리스트 내포 사용하기
# [표현식 for 항목 in 반복 기능 객체 if 조건]
#
# [표현식 for 항목1 in 반복 기능 객체1 if 조건1
#         for 항목2 in 반복 기능 객체2 if 조건2
#         ...
#         for 항목n in 반복 기능 객체n if 조건n]

#
a = [1,3,5,7]
result = []
for num in a:
    result.append(num * num)

print(result)   

# 리스트 내포 사용
result2 = [n * n for n in a]
print(result2)