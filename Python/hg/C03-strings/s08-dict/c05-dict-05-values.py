# 딕셔너리(Dictionary) 함수

st = {
    "name": "홍길동",
    "age":   28,
    "주소": "한양",
    "생존":  False
}

# 딕셔너리에서 값을 리스트 형태의 객체을 얻음
dv = st.values()
print(dv) # dict_values(['홍길동', 28, '한양', False])

#%%

# 딕셔너리 값 객체를 리스트 변환
lv = list(dv)
print("리스트:", lv)

#%%

# 딕셔너리 값 객체를 튜플 변환
tv = tuple(dv)
print("튜플:", tv)

#%%

# 값 목록 출력
print("# 값 목록 출력")
for v in dv:
    print(v)

#%%

# 딕셔너리에서 키 목록을 출력
print("# 딕셔너리에서 키 목록을 출력")
for v in st.values():
    print(v)



