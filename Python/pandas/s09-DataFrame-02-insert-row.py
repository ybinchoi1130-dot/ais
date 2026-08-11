# 판다스(pandas)

# 리스트(list)로 판다스 데이터프레임 만들기
# 행 추가: DataFrame.loc(), DataFrame.iloc()
# 열 추가: DataFrame.insert()
#       

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

print(df.shape) # (3, 2)

#%%

# 새로운 행 추가
# loc[인덱스] = [값1, 값2, ...]
# 행에 해당하는 컬럼 값을 리스트로 지정
# 리스트는 컬럼의 갯수와 동일해야 한다.
df.loc['춘향'] = [18, '광한루']
print(df)

#%%

"""
    나이   학교
영빈  15  장안중
정명  16  수성중
수정  17  연세중
춘향  18  광한루
"""

#%%

# [변경]
# 행의 내용을 변경
# 기존에 인덱스가 존재하면 값이 변경 된다.
df.loc['춘향'] = [19, '남원중']
print(df)

#%%

"""
    나이   학교
영빈  15  장안중
정명  16  수성중
수정  17  연세중
춘향  19  남원중
"""

#%%

# [추가] 
# iloc : 순번을 이용하여 추가
# 맨 마지막에 추가
dlen = len(df)
print(dlen) # 현재 행의 갯수: 4
print(df.iloc[dlen-1]) # 맨 마지막 행: '춘향'

#%%

"""
나이     19
학교    남원중
Name: 춘향, dtype: object
"""

#%%

# 맨 마지막 행의 내용을 변경
# 변경: iloc[순번] = 값
# 인덱스('춘향')의 iloc를 사용하여 순번으로 변경
dend = len(df) - 1
df.iloc[dend] = [20, '광한중']

#%%

# 주의: iloc는 새로운 행을 추가할 수 없다.
# IndexError: iloc cannot enlarge its target object
# dlen = len(df)
# df.iloc[dlen] = [21, '수원중']








