# 리스트에 요소 삽입: insert

lst = [3,5,7]

lst.append(9) # 맨 마지막에 넣기
print(lst) # [3, 5, 7, 9]

# 0번째 위치에 값을 넣고 기존의 내용은 뒤로 밀림
pos = 0 # 삽입할 위치
val = 1 # 삽입할 값
lst.insert(pos, val)

print(lst) # [1, 3, 5, 7, 9]

# insert()를 이용해서 맨 마직막에 요소를 삽입
pos = len(lst) # 맨 마지막 요소 다음
val = 99       # 삽입할 값
lst.insert(pos, val)

print(lst)