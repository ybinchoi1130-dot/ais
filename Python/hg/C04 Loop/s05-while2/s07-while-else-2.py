# 반복문(while)

# 리스트에서 자료 꺼내기
lists = [1,2,4,6,8,10]
cnt = 0
tot = 0

# 리스트에 들어 있는 값 가운데 짝수의 합
# while에 break가 없으므로 출력
while cnt < len(lists):
    val = lists[cnt]
    if val % 2 == 0:
        tot += val
        print(f"> [cnt={cnt}] val={val}, tot={tot}")
    cnt += 1
else:
    print('break를 만나지 않았습니다.')    

print('짝수의 합:', tot)    

