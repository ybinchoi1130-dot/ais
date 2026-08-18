# -*- coding: utf-8 -*-

# 학생 성적 처리
# 과목별 총점, 평균을 구함
# Series.sum(), Series.mean()을 이용하여 총점, 평균을 구함
# 반복문(for in)을 사용하지 않고 판다스 만으로 계산
#
# 엑셀 파일로 저장
#   - pip install openpyxl
#   - DataFrame.to_excel(filename)
#   - 예) ndf.to_excel("학생성적결과.xlsx")
#


#%%

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장 
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')

#%%

# 컬럼('이름')을 인덱스로 이동
ndf = df.set_index('이름')
print(ndf)

#%%

# 학생별 전체 과목의 총점 및 평균
# 가로축: axis=1
# 결과: 각 행별 시리즈()
tot = ndf.sum(axis=1)          # 총점
avg = ndf.mean(axis=1).round() # 평균

# 컬럼 추가: 각 인덱스에 일치하는 곳에 지정
ndf['총점'] = tot
ndf['평균'] = avg
print(ndf)

#%%

"""
# 문제점: 컬럼의 총점과 평균이 계산 됨
# 과목별 전체 학생의 총점 및 평균
# 세로축: axis=0
# 결과: 각 열별 시리즈()
tot2 = ndf.sum(axis=0)          # 총점
avg2 = ndf.mean(axis=0).round() # 평균

# 행(인덱스) 추가
ndf.loc['총점'] = tot2
ndf.loc['평균'] = avg2
print(ndf)
"""

#%%

# 해결책: 컬럼의 총점과 평균을 제외 시킴
# 과목별 전체 학생의 총점 및 평균
# 세로축: axis=0
# 결과: 각 열별 시리즈()
tot2 = ndf.loc[:, '수학':'체육'].sum(axis=0)          # 총점
avg2 = ndf.loc[:, '수학':'체육'].mean(axis=0).round() # 평균

# 행(인덱스) 추가
ndf.loc['총점'] = tot2
ndf.loc['평균'] = avg2
print(ndf)

#%%

# CSV 파일로 저장
ndf.to_csv("학생성적결과.txt")

#%%

# ModuleNotFoundError: No module named 'openpyxl'
# pip install openpyxl
# Excel 파일로 저장
ndf.to_excel("학생성적결과.xlsx")





