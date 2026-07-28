# 반복문(for)
# for ... else

lists = [2,4,6,8,10]
tot = 0

# for 문에서 break에 의해서 실행이 종료 되지 않으면
# 반복문을 종료 후 else 실행

for val in lists:
    if val % 2: # 홀수: 나머지가 있으면 홀수
        break
    tot += val
    print(val)
else:
    print('홀수가 없습니다.')    

print('짝수의 합:', tot)    

#%%

"""
2
4
6
8
10
홀수가 없습니다.
짝수의 합: 30
"""