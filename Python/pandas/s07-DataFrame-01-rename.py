# 판다스(pandas)

# 리스트(list)로 판다스 데이터프레임 만들기
# 이름변경: DataFrame.rename(index={}, columns={}, inplace=True)
#   - 인덱스 변경: index={}
#   - 컬럼명 변경: columns={}
#   - 원본 변경  : inplace=True
#   - 사본 리턴  : inplace=False
#                  기본값은 False이며 원본을 변경하지 않으며 
#                  변경된 내용을 반영하여 사본을 리턴한다.
#       

#%%

import pandas as pd

# list
data = [ 
# 컬럼: 0,    1,   2     
       [15, '남', '장안중'], # 0행
       [16, '여', '수성중']  # 1행
]

# 판다스 데이터프레임 생성: 2행 * 3열
df = pd.DataFrame(data, 
                  index=['영빈', '정명'],
                  columns=['나이', '성별', '학교'])
print(df)

#%%

"""
    나이 성별   학교
영빈  15  남  장안중
정명  16  여  수성중
"""

#%%

# 데이터프레임의 모양: 2행, 3열
# 결과: tuple -> (행, 열)
print(df.shape) # (2, 3)

#%%

# 인덱스 변경
#   - 딕셔너리 자료형(dict)
#   - 키: 원래 인덱스
#   - 값: 새로운 인덱스
# 결과: 변경된 내용을 반영하여 새로운 데이터프레임 생성
ndf = df.rename(index={'영빈': '영수'})
print(ndf)

#%%

# index를 여러개 동시에 변경
ndf = df.rename(index={'영빈': '영수', '정명': '정희'})
print(ndf)

#%%

# 일치하는 이름이 없으면 바뀌지 않는다.
# ※ 오류는 발생되지 않는다.
# ※ 오류가 발생되지 않으므로 확인이 되지 않는다.  
# ※ index('영희')는 존재하지 않으므로 바뀌지 않음
xdf = df.rename(index={'영희': '영수', '정명': '정희'})
print(xdf)

#%%

cdf = df.rename(columns={'나이': '연령', '학교':'중학교'})
print(cdf)

#%%

# 원본으로 사본을 생성
zdf = df.rename(index={'영빈': '영수', '정명': '정희'},
    columns={'나이': '연령', '학교':'중학교'})
print(zdf)

#%%

# 원본 수정
# inplace=True
# 결과: 원본이 수정되면 리턴값은 없다.
xdf = df.rename(index={'영빈': '영수', '정명': '정희'},
    columns={'나이': '연령', '학교':'중학교'}, inplace=True)
print(xdf) # None
print(df)







