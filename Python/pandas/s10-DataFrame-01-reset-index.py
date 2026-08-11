# 판다스(pandas)

# 리스트(list)로 판다스 데이터프레임 만들기
# set_index()   : 인덱스 지정, 컬럼을 인덱스로 지정(이동)
# reset_index() : 인덱스 리셋, 인덱스를 컬럼으로 지정(이동)

#%%

import pandas as pd

# list
data = [ 
       [15, '장안중'], # 0행
       [16, '수성중'], # 1행
       [17, '연세중']  # 2행
]

# 판다스 데이터프레임 생성: 3행 * 2열
df = pd.DataFrame(data, 
                  index=['영빈', '정명', '수정'],
                  columns=['나이', '학교'])

#%%

# 리셋 인덱스: reset_index()
# index가 컬럼으로 이동하여 새로운 컬럼이 생성
# 컬럼이름: index
# index: 0부터 순번이 부여된다.(iloc와 같아 진다.)
ndf = df.reset_index()
print(ndf)

#%%

# 컬럼이름변경: 'index' -> '이름'
sdf = ndf.rename(columns={'index': '이름'})
print(sdf)

#%%

# 특정 컬럼을 인덱스로 이동
# 컬럼('이름') -> Index
# 기존의 Index는 사라짐
tdf = sdf.set_index('이름')
print(tdf)

#%%

print(tdf.loc['정명'])

#%%

"""
나이     16
학교    수성중
Name: 정명, dtype: object
"""


#%%

xdf = tdf.set_index('나이')
print(xdf)

#%%

zdf = xdf.set_index('학교')
print(zdf)
print(zdf.shape) # (3, 0)


