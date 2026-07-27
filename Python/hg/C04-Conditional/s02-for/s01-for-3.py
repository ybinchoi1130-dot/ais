# 반복문(for)
# for 변수 in 리스트, 튜플, 문자열, ...

# 리스트에 각 요소가 튜플
lists = [(1,'one'), (2,'two'), (3,'three'), (4,'four')]

# 리스트에 들어 있는 내용의 갯수만큼 반복하면서
# 아이템을 하나씩 꺼내서 변수에 담아준다.
for tuples in lists: # 4번 반복
    print(type(tuples), tuples, ': ', end='')
    print(tuples[0], ',', tuples[1])

#%%

for tuple in lists:   # 4번 반복
    for tx in tuple:  # 2번 반복
        print(tx, end=' ')
    print()

#%%    

lists = [(1,'one'), (2,'two'), (3,'three'), (4,'four')]

# 파이썬의 키워드를 변수로 할당하면?
# 오류는 나오지 않지만 원래 기능을 상실한다.
for tuple in lists:   # 4번 반복
    for tx in tuple:  # 2번 반복
        print(tx, end=' ')
    print()

# 원래 튜플(tuple)의 기능이 상실하고 변수가 됨
# for가 처리한 맨 마지막 요소의 값을 가지고 있다.
print(type(tuple), tuple) # <class 'tuple'> (4, 'four')

#%%

# TypeError: 'tuple' object is not callable
# 빈 튜플을 생성하기 못함
tp = tuple()
print(type(tp), tp)
    
#%%

# NameError: name 'printx' is not defined
printx("hello")

#%%

# print() 함수를 printx라는 이름에 지정
printx = print
printx("hello") # "hello"
print("hello")  # "hello"

#%%

print = 10
print("hello") # TypeError: 'int' object is not callable



    
    
    
    
    
