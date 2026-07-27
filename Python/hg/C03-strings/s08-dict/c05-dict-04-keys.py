# 딕셔너리(Dictionary) 함수

st = {
    "name": "홍길동",
    "age": 28,
    "주소": "한양",
    "생존": False
}

# 딕셔너리에서 키 리스트 형태의 객체을 얻음
dk = st.keys()
print(dk) # dict_keys(['name', 'age', '주소', '생존'])

#%%

# 딕셔너리 키 객체를 리스트 변환
lk = list(dk)
print("리스트:", lk)

#%%

# 딕셔너리 키 객체를 튜플 변환
tk = tuple(dk)
print("튜플:", tk)

#%%

# 키 목록 출력
# dk 객체가 담고 있는 키의 갯수만큼 반복하면서 키를 출력
for k in dk: 
    print(k)

#%%

# 딕셔너리에서 키 객체를 얻는 메서드를 호출해서
# 반복문을 통해서 키의 요소의 갯수만큼 목록을 출력
for k in st.keys() :
    print(k)

#%%

# 딕셔너리에서 키을 얻어서 해당 키로 값을 참조해서 출력
for k in dk:
    val=st[k]
    print(f"[{k}] : {st[k]}")
    print(f"[{k}] : {[val]}")


