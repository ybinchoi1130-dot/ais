# 판다스
# 데이터프레임: DataFrame
#   - 데이터 테이블, 2차원 배열, 행렬(matrix)
#   - 행: 인덱스, row index
#   - 열: column, Pandas.Series
#
# 형식:
#   pandas.DataFrame(data [, index=index_data, columns=columns_data])    
#
# 주의:
#  - 모든 컬럼의 행의 갯수가 일치해야 한다.
#  - 일치하지 않으면? 오류(ValueError)

#%%

import pandas as pd

# dict
data = {  # 3행, 5열
    'c0': [1,2,3],    # 컬럼, 시리즈
    'c1': [4,5,6],    # 컬럼, 시리즈
    'c2': [7,8,9],    # 컬럼, 시리즈
    'c3': [10,11,12], # 컬럼, 시리즈
    'c4': [13,14,15]  # 컬럼, 시리즈
}

# 딕셔너리로 데이터프레임 생성
# 열: 딕셔너리의 키
# 행: 딕셔너리의 요소의 갯수
# 인덱스는 순버으로 자동 부여
df = pd.DataFrame(data, index=['1행', '2행', '3행'])
print(type(df))
print(df)

#%%

"""
    c0  c1  c2  c3  c4
1행   1   4   7  10  13
2행   2   5   8  11  14
3행   3   6   9  12  15
"""
