# 리스트 정렬 
# sorted : Built-in Function

# 요소의 위치를 순서대로 변경
# 오름차순 : 작은 값에서 큰 값 순서
# 원본 데이터는 변경 없음
# 리턴 : 정렬 결과
# reverse : True, False

lst = [4,7,3,10,99,22]

print(lst) # [4, 7, 3, 10, 99, 22]

# 정렬 : 오름차순
lst_asc = sorted(lst)

print("오름차순:", lst_asc) # [3, 4, 7, 10, 22, 99]

# 정렬 : 내림차순
lst_desc = sorted(lst, reverse=True) # 뒤집기, 반전
print("내림차순:", lst_desc)

