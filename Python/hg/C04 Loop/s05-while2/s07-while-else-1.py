# 반복문(while)
# while 문에서 break를 만나지 못하면 else 실행

# 리스트에서 자료 꺼내기
lists = [2,4,6,8,9,10] # 홀수(9)가 존재
cnt = 0
tot = 0

# 처음부터 끝까지 이동을 하면서 홀수를 만나면 탈출
# 홀수를 만나기 전까지의 짝수의 합
# 리스트에 들어 있는 값 가운데 짝수의 합
while cnt < len(lists):
    val = lists[cnt]
    if val % 2 == 1: # 홀수
        print('브레이크...')
        break
    tot += val
    print(f"[cnt={cnt}] val={val}, tot={tot}")
    cnt += 1
else: # 홀수가 없으면 실행된다.
    print('홀수가 없습니다.')    

print(f'인덱스 0부터 {cnt-1}까지의 짝수의 합은? {tot}') # 2,4,6,8의 합은 20

#%%

# 리스트에서 자료 꺼내기
lists = [2,4,6,8,10]   # 홀수가 존재하지 않음
cnt = 0
tot = 0

# 리스트에 들어 있는 값 가운데 짝수의 합
# 리스트(lists)에 홀수가 없으므로 break를 만나지 않고 끝남
while cnt < len(lists):
    val = lists[cnt]
    if val % 2 == 1: # 홀수
        print('브레이크...')
        break
    tot += val
    print(f"[cnt={cnt}] val={val}, tot={tot}")
    cnt += 1
else: # 홀수가 없으면 실행된다.
    print('홀수가 없습니다.')    # 실행이 된다.

print(f'인덱스 0부터 {cnt-1}까지의 짝수의 합은? {tot}') # 인덱스 0부터 4까지의 짝수의 합은? 30






