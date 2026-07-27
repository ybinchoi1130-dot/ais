# 반복문(while)


# 리스트에서 자료 꺼내기
lists = [2,4,6,8,10]
cnt = 0
tot = 0
lex = len(lists) # 리스트 데이터의 갯수, 갯수 5

# lists에 있는 자료를 하나씩 꺼내서 각 요소의 합을 구함
# 확인한 내용은 사라지지 않음(보존)
while cnt < lex: # cnt가 lex와 같아지면 탈출
    val = lists[cnt] # 참조(확인)
    tot += val
    print(f"[cnt={cnt}] val={val}, tot={tot}")
    cnt += 1 # 참조 인덱스

print(f'lists={lists}')    
print(f'tot={tot}')     # 30

