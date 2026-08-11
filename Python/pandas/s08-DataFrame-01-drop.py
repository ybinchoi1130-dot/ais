# 판다스(pandas)

# 리스트(list)로 판다스 데이터프레임 만들기
# 행, 열 삭제: DataFrame.drop()
#       

#%%

import pandas as pd

# list
data = [ 
# 컬럼: 0,    1,   2     
       [15, '남', '장안중'], # 0행
       [16, '여', '수성중'], # 1행
       [17, '여', '연세중']  # 2행
]

# 판다스 데이터프레임 생성: 3행 * 3열
df = pd.DataFrame(data, 
                  index=['영빈', '정명', '수정'],
                  columns=['나이', '성별', '학교'])

print(df.shape) # (3, 3)

#%%

# 행을 삭제하고 새로운 데이터프레임을 리턴
# 원본의 변화는 없음
# 행삭제: axis=0 기본값
ndf = df.drop('정명')
print(ndf)

#%%

ndf = df.drop('정명', axis=0)
print(ndf)

#%%

# 다중행 삭제
# 인덱스를 리스트로 지정
ndf = df.drop(['정명', '수정'], axis=0)
print(ndf)

#%%

# 없는 행을 삭제하려면 예외발생
# KeyError: "['수희'] not found in axis"
name = '수희'
try:
    ndf = df.drop(name) # 행 삭제 시도
    print(ndf)
except KeyError as e:
    print(f"학생중에 ({name}) 학생이 존재하지 않아 삭제를 실패했습니다.")
    print(e) # "['수희'] not found in axis"

#%%

# 열삭제: axis=1
ndf = df.drop('학교', axis=1)
print(ndf)

#%%

# 다중 열 삭제
# 삭제할 열의 목록을 리스트로 전달
ndf = df.drop(['성별', '학교'], axis=1)
print(ndf)

#%%

# 다중 행 삭제
# 삭제할 행의 목록을 리스트로 전달
ndf = df.drop(['영빈', '수정'], axis=0)
print(ndf)

#%%
# 원본삭제: inplace=True
# 열삭제: axis=1
# 리턴: None
xdf = df.drop('학교', axis=1, inplace=True)
print(xdf) # None

