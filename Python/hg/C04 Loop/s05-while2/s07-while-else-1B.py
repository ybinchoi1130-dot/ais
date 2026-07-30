# 반복문(while)
# while 문에서 break를 만나지 못하면 else 실행

# 리스트에서 자료 꺼내기
lists = [2,4,5,6,8,10] # 홀수는 인덱스 2번째

cnt = 0
tot = 0

# 리스트에 들어 있는 값 가운데 짝수의 합
while cnt < len(lists):
    val = lists[cnt]

    if val % 2: # 홀수
        print(f'홀수는 인덱스 ({cnt})번째 있으며 값은 ({lists[cnt]}) 이다.')
        break

    tot += val
    print(f"[cnt={cnt}] val={val}, tot={tot}")
    cnt += 1
else:
    print('홀수 값이 없습니다.')

print(f'인덱스 0부터 {cnt-1}까지의 짝수의 합은? {tot}')    

