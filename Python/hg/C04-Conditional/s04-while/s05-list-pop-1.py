# 반복문(while)

lst = [2,4,6,8,10]

# LIFO(Last In Fist Out), 후입선출, Stack(스택)
# list.pop() 자료를 마지막에서 하나씩 꺼냄
# 꺼낸 후 list에서는 자료가 삭제됨

while lst: # lst에 데이터가 있으면 참, 없으면 거짓
    print(lst.pop()) # 10 8 6 4 2

print('lst:', lst)
