# 반복문(while)

# 리스트에서 자료 꺼내기
lists = [1,2,4,6,8,10,7]
cnt = 0
tot = 0

# while에 break가 없으므로 출력
# while 문에서 break를 발견하지 못하면 else 실행
while cnt < len(lists):
    val = lists[cnt]
    if val < 0:
        print('리스트에 마이너스(-1) 값이 있어서 처리를 종료했습니다.')    
        break
    tot += val
    print(f"> [cnt={cnt}] val={val}, tot={tot}")
    cnt += 1
else:
    print('리스트에 마이너스(-1) 값이 없습니다.')    

print('리스트의 합:', tot)    

