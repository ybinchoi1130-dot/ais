# 반복문(while)
"""
조건식: 불(bool) 타입, 참(True), 거짓(False)

while 조건식:
    실행문1
    실행문2
    ...
"""

#%%

# 반복회수를 변수에 담아서 출력하라.
count = 1
while count <= 10:  # 1,2,3,4, ... 10
    print('나무를 {0}번 찍는다.'.format(count))
    count += 1

print('count=', count) # 11
print("THE END")