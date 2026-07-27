# 딕셔너리(Dictionary)
# 자료형: dict

# 키와 값으로 구성된 자료형
# 파이썬의 표기: dict
# 
# 중괄호로 감싼 형태
# { 키1:값1, 키1:값2, ... }

#############################################
# 키(Key)는 해시(Hash)로 만들어 진다.
# 특징:
#   - 장점: 검색속도가 빠르다.
#   - 단점: 용량을 많이 차지한다.
#   - 단점: 순차적으로 처리하는 속도가 느리다.
# 키(key)는 변하는 않는 값을 사용해야 한다.
#   - 리스트(list)는 사용할 수 없다.(값을 변경 가능)
#   - 중복을 허용하지 않는다.(유일한 값)
#############################################

# 빈 딕셔너리

de = {}
dt = dict()

print(type(de), de)
print(type(dt), dt)

#%%
student = {
    "name": "홍길동",
    "age": 28,
    "주소": "한양",
    "생존": False
}

print(student)
# {'name': '홍길동', 'age': 28, '주소': '한양', '생존': False}

#%%

# 키를 이용하여 값을 찾기
# 값 = dict[키]
print("name:", student['name'])
print("age:",  student['age'])
print("주소:", student['주소'])
print("생존:", student['생존'])

#%%

# 추가 : 지정된 키가 존재하지 않으면 새로 추가
student['결혼'] = 28
print(student)

#%%
6
# 수정: 동일한 키가 있으면 변경
student['결혼'] = 30
print("결혼:", student['결혼'])

print(student)
#%%

# 삭제 : 키를 지정하여 삭제
# del dict[키]
del student['생존']
print(student)

#%%

# 키가 존재하지 않으면?
# 예외발생: KeyError: '생존'
del student['생존']

print("종료")




