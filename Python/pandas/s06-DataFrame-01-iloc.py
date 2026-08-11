# 판다스(pandas)

# 리스트(list)로 판다스 데이터프레임 만들기
# 인덱스 지정하기
# 컬럼 지정하기
# 인덱스 참조하기: iloc

#%%

import pandas as pd

# list data
data = [
    [20, '남', '한양대'],
    [21, '여', '장안대'],
    [22, '남', '연세대'],
    [23, '여', '수원대']
]

index_names = ['길동', '성희', '연성', '수희']
column_names = ['나이', '성별', '학교']

df = pd.DataFrame(data, 
                  index=index_names, 
                  columns=column_names)

print(df)

#%%

# 단일행 
# iloc: 인덱스 순번 선택, 행을 추출
# 결과: Series
gildong = df.iloc[0]
print(type(gildong))
print(gildong)

#%%

"""
<class 'pandas.Series'>
나이    20
성별    남
학교    한양대
Name: 길동, dtype: object
"""

#%%

# 다중행: 1개만 지정
# iloc: 인덱스 순번 선택, 행들을 추출
# 인덱스 순번을 리스트로 전달
# 결과: DataFrame
gildong1 = df.iloc[ [0] ]
print(type(gildong1))
print(gildong1)

#%%

"""
<class 'pandas.DataFrame'>
    나이 성별   학교
길동  20  남  한양대
"""

#%%

# 다중행: 2개 지정
# 인덱스의 순번에서 길동(0), 연성(2)을 선택
students = df.iloc[ [0,2] ]
print(type(students))
print(students)

#%%

"""
<class 'pandas.DataFrame'>
    나이 성별   학교
길동  20  남  한양대
연성  22  남  연세대
"""

#%%

# 다중행: 범위 지정
# 인덱스의 순서에 의해 지정된다.
# 인덱스의 순번에서 '길동'부터 '연성'까지 선택
# 인덱스의 순번 사이에 콜론(:)을 넣는다.

# ※ 주의 ※ 
# 리스트에 범위를 지정하는 형태는 오류
# SyntaxError: invalid syntax
# students = df.iloc[ [0:3] ]

#%%

# iloc[ 슬라이싱 ]
# 슬라이싱: 시작번호:끝번호(n-1까지 지정된다)
istart = 0 # 시작번호
iend = 3   # 종료번호 - 1
students = df.iloc[ istart:iend ]
print(type(students))
print(students)

#%%

"""
<class 'pandas.DataFrame'>
    나이 성별   학교
길동  20  남  한양대
성희  21  여  장안대
연성  22  남  연세대
"""

#%%

# 행(인덱스)과 열을 동시에 지정
# 형식: DataFrame.iloc[행,열]
#   - 콤마(,)를 기준으로 행과 열을 지정

#%%

# 전체행과 전체열을 선택
dfx1 = df.iloc[:]    # 동일
dfx2 = df.iloc[:,:]  # 동일
print(dfx1)
print(dfx2)

#%%

# 전체행과 열(성별, 학교)
# 열도 행과 마찬가지로 숫자로 지정해야 한다.
# df2 = df.loc[:, ['성별', '학교']]
df2 = df.iloc[:, 1:3]
print(df2)

#%%

# 일부행(순번)과 열(성별, 학교)
# 행: 성희(1)부터 끝까지
# 열: 성별(1)부터 끝까지
df3 = df.iloc[1:, 1:]
print(df3)

#%%

"""
   성별   학교
성희  여  장안대
연성  남  연세대
수희  여  수원대
"""




