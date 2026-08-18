# -*- coding: utf-8 -*-

# 학생 성적 처리
# 과목별 총점, 평균을 구함
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

#  학생별 평균을 구하기 위한 과목 수
subject_cnt = len(ndf.columns)
print("과목건수: ", subject_cnt)

# 컬럼 추가
ndf['총점'] = 0
ndf['평균'] = 0
print(ndf)

#%%

# 확인용
for student in ndf.index:
    print(student, ndf.loc[student])


#%%

print("# 학생별 총점 및 평균 #")

for student in ndf.index: # 인덱스: 학생이름
    scores = ndf.loc[student] # 각 학생의 모든 과목점수
    tot = scores.sum()
    
    ndf.loc[student, '총점'] = tot                # 총점
    ndf.loc[student, '평균'] = tot // subject_cnt # 평균

print(ndf)    

#%%

rowcnt = len(ndf) #  전체 행의 갯수 : 3건

# 과목별 총점, 평균을 위한 행 추가
ndf.loc['총점'] = 0
ndf.loc['평균'] = 0

#%%

print("# 과목별 총점 및 평균 #")
print("# 과목의 총 갯수:", subject_cnt) # 4개

for subject in ndf.columns[0:4]: # 수학 -> 체육
    # 각 칼럼의 과목별 전체 학생 데이터의 시리즈(Series)
    scores = ndf.loc[:, subject]    
    tot = scores.sum()
    
    ndf.loc['총점', subject] = tot
    ndf.loc['평균', subject] = tot // rowcnt
    
print(ndf)    


