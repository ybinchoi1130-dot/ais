# 반복문(for)
# for 변수 in 리스트, 튜플, 딕셔너리, 문자열, ...

# 리스트 -> 세트
sets = set(['one', 'two', 'three', 'four'])

# 셋에 들어 있는 내용의 갯수만큼 반복하면서
# 아이템을 하나씩 꺼내서 변수에 담아준다.
for item in sets: # 4번 반복
    print(item)
    
#%%

# 기본 타입은 반복 가능하지 않다.
y = 10
for x in y: # TypeError: 'int' object is not iterable
    print(x)

#%%

# 문자열
abc = "abcdefg"
for al in abc:
    print(al)

#%%



