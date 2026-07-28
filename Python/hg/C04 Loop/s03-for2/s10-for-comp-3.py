# 리스트 내포 사용하기
# [표현식 for 항목 in 반복 기능 객체 if 조건]
#
# [표현식 for 항목1 in 반복 기능 객체1 if 조건1
#         for 항목2 in 반복 기능 객체2 if 조건2
#         ...
#         for 항목n in 반복 기능 객체n if 조건n]

#

# 리스트 내포 사용 : 구구단
result = [m * n for m in range(2,10) 
            for n in range(1,10)]
print(result)