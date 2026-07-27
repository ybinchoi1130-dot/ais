# 딕셔너리(Dictionary) 함수
# dict_items = dict.items()

st = {
    "이름": "홍길동",
    "나이": "이십팔세",
    "주소": "한양",
    "생존": "고인"
}

# 딕셔너리에서 키와 값을 리스트 형태의 객체을 얻음
items = st.items()
print(items) 

#%%
"""
dict_items(
    [
        ('이름', '홍길동'), 
        ('나이', '이십팔세'), 
        ('주소', '한양'), 
        ('생존', '고인')
    ]
) 
"""
#%%

# dict_items -> list
ilst = list(items)
print(ilst)

#%%
"""
[
    ('이름', '홍길동'), 
    ('나이', '이십팔세'), 
    ('주소', '한양'), 
    ('생존', '고인')
]
"""

#%%

# dict.items()을 리스트 변환하면 각 요소(키, 값)는 튜플(tuple)이다.
print(ilst[0], type(ilst[0])) # ('이름', '홍길동') <class 'tuple'>


#%%
print(f"                     [키목록]       [값목록]")
for kv in ilst:
    k, v = kv # unpacking(tuple)
    print(f"kv({type(kv)}): [{k:10}] [{v:10}]")

#%%

"""
[키목록]       [값목록]
kv(<class 'tuple'>): [이름        ] [홍길동       ]
kv(<class 'tuple'>): [나이        ] [이십팔세      ]
kv(<class 'tuple'>): [주소        ] [한양        ]
kv(<class 'tuple'>): [생존        ] [고인        ]
"""

#%%    

print(f"[키목록]       [값목록]")
for key, value in ilst: # unpacking(tuple)
    print(f"[{key:10}] [{value:10}]")
    
    
    
    
    
    
