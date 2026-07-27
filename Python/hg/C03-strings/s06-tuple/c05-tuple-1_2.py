# 튜플(Tuple)
# 불변(immutable) 상수 리스트(list)
# 불변 : 요소의 값을 변경할 수 없다.
# 수정(추가, 삭제, 변경)을 할 수 없다.
# 그 외에는 리스트와 비슷하다.
# 장점:
#   - 리스트에 비해서 속도가 빠르다.
#   - 공간절약(메모리)
# 특징:
#   - 딕셔너리(dict) 키로 활용
#   - 함수(function)의 인자로 사용
# 사용:
#   - 요소가 한 개인 경우에는 마지막 요소 뒤에 콤마(,)를 붙여야 한다.     
#   - 튜플변수 = (값, )                         \
#   - 튜플변수 = (값, 값) 

# 튜플 객체 생성
#   - tuple()
#   - 소괄호 : ()
#   - 소괄호 생략 가능
#%%

# 빈 튜플
t0 = ()
te = tuple()
print(type(t0), t0) # <class 'tuple'> ()
print(type(te), te) # <class 'tuple'> ()

#%%

# ※ 주의 : 요소가 1개인 경우 요소 뒤에 콤마(,)를 붙여야 한다.
t1a = 1,
t1b = (9,)
print(type(t1a), t1a) # <class 'tuple'> (1,)
print(type(t1b), t1b) # <class 'tuple'> (9,)

#%%

# 요소가 1개인 경우 마지막에 콤마를 붙이지 않으면 
# 기본 자료형이 된다.
txa = 1
txb = (9)
print(type(txa), txa) # <class 'int'> 1
print(type(txb), txb) # <class 'int'> 9


#%%

# 요소가 2개 이상인 경우에는 콤마를 붙이지 않아도 된다.
t2a = 1,2
t2b = (1,2)
print(type(t2a), t2a) # <class 'tuple'> (1, 2)
print(type(t2b), t2b) # <class 'tuple'> (1, 2)

#%%

tp = (10,20,30)
print(tp[0]) # 참조: 10
print(tp[1]) # 참조: 20
print(tp[2]) # 참조: 30

#%%

# ☆ 특징: 요소의 값을 변경할 수 없다.
# TypeError: 'tuple' object does not support item assignment
tp[0] = 99




