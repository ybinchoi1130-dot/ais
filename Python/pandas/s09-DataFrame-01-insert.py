# 판다스(pandas)

# 리스트(list)로 판다스 데이터프레임 만들기
# 행, 열 삭제:DataFrame.drop()

#%%

import pandas as pd

# list data
data = [  
    [22, '연세대'], #0행
    [23, '수원대'], #1행
    [24, '서울대']  #2행
]

df = pd.DataFrame(data,
                  index=['영빈','정명','수정'],
                  columns=['나이','학교'])

print(df)
#%%

#새로운 행 추가

df.loc['춘향']=[21,'충남대']
#%%

dlen = len(df)

print(dlen)
print(df.iloc[dlen-1])
#%%
#iloc는 새로운 행을 추가할 수 없다.
#IndexError: iloc cannot enlarge its target object
dlen = len(df)
df.iloc[dlen]=[23,'부산대']

#%%
#열추가 :주소

df['주소'] ='수원'
print(df.shape)

#%%
# 열을 추가하고 각 행에 개별 값을 지정

df['성별']=['남자','여자','여자']
print(df)

#%%

#insert(위치, 컬럼, 값)
df.insert(2,'전화번호',None)
print(df)

