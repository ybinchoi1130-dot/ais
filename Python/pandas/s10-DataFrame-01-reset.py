# 판다스(pandas)

# 리스트(list)로 판다스 데이터프레임 만들기
# set_index() 인덱스 지정 : 컬럼을 인덱스로 지정
# reset_index() 인덱스 리셋
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

# 인덱스 리셋
# index가 컬럼으로 이동하여 새로운 컬럼이 생성
# index는 0부터 순번이 부여된다.(iloc와 같아 진다.)
ndf=df.reset_index()

print(ndf)

#%%
# 컬럼이름 변경

xdf=ndf.rename(columns={'index': '이름'})
print(xdf)

#%%
#특정 컬럼을 인덱스로 이동
#컬럼('이름') -> index
#기존의 index는 사라짐
tdf=xdf.set_index('이름')

print(tdf)

#%%

sdf=tdf.set_index('학교')
print(sdf)