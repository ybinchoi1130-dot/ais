# 판다스(pandas)

# 리스트(list)로 판다스 데이터프레임 만들기
# 컬럼 선택

#%%

import pandas as pd

# list
data = [ 
       [15, '남', '장안중'],  # 0행
       [16, '여', '수성중'],  # 1행
       [17, '여', '연세중']]  # 2행

# 판다스 데이터프레임 생성: 3행 * 3열
df = pd.DataFrame(data, index=['영빈', '정명', '수정'],
                  columns=['나이', '성별', '학교'])

#%%

# 없는 컬럼을 참조
# 오류: KeyError: '주소'
# print(df['주소'])

#%%

# 결과: 인덱스, 컬럼('학교')
school = df['학교']
print(type(school)) # <class 'pandas.Series'>
print(school)

#%%

"""
index   학교
------------------
영빈    장안중
정명    수성중
수정    연세중
Name: 학교, dtype: str
"""

#%%

# 컬럼을 참조하여 새로운 데이터프레임 생성
# 컬럼목록을 리스트로 전달하면 데이터프레임 생성
school_df = df[ ['학교'] ]
print(type(school_df)) # <class 'pandas.DataFrame'>
print(school_df)

#%%

"""
     학교
영빈  장안중
정명  수성중
수정  연세중
"""

#%%

students = df[ ['학교', '나이'] ]
print(type(students)) # <class 'pandas.DataFrame'>
print(students)

#%%

"""
     학교  나이
영빈  장안중  15
정명  수성중  16
수정  연세중  17
"""

