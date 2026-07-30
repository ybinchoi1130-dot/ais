# 반복문(while)
# continue : 
#   반복문에서 continue 아래의 문장을 실행하지 않고 
#   다시 반복문의 조건식이 있는 처음으로 되돌아 간다.

# 리스트에서 자료 꺼내기
lists = [1,2,4,6,-1,8,-2,10] # 원본
tot = 0

listx = lists[:] # 복사: 메모리 낭비 발생

# 리스트의 값에서 마이너스 값을 계산하지 않음
# 음수이면 continue로 처리
while listx:
    val = listx.pop(0)
    print(f"> [val={val}, tot={tot}")

    if val < 0:
        print(f'리스트에 마이너스({val}) 값을 계산하지 않음')    
        continue

    tot += val

print('리스트의 합:', tot)    

