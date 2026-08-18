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

# 확인용 코드
sr = ndf.loc[:,'수학':'체육']
print(sr)

#%%

#  학생별 평균을 구하기 위한 과목 수
subject_cnt = len(ndf.columns)
print("과목건수: ", subject_cnt)

# 컬럼 추가
ndf['총점'] = 0
ndf['평균'] = 0
print(ndf)

#%%

print("# 학생별 총점 및 평균 #")
for x in range(len(ndf)):
    rows = ndf.iloc[x, :]
    tot = 0
    for val in rows:
        tot += val
  
    # 인덱스: 학생이름
    student_name = ndf.index[x]
    
    # ndf.iloc[x,4] = tot                # 총점
    # ndf.iloc[x,5] = tot // subject_cnt # 평균
    ndf.loc[student_name, '총점'] = tot                # 총점
    ndf.loc[student_name, '평균'] = tot // subject_cnt # 평균

print(ndf)    

#%%

print("# 전체 행의 갯수") # 3건
print(len(ndf))         # 행수 갯수
print(ndf.shape)        # tuple(3,6) : 3 * 6
print(ndf.shape[0])     # 3행
print(len(ndf.index))   # 3행 
print(len(ndf.iloc[:])) # 3행

#%%

# 칼럼 및 칼럼의 갯수
# 컬럼: ['수학', '영어', '음악', '체육', '총점', '평균']
print("칼럼: ", ndf.columns) 
print("칼럼의 갯수: ", len(ndf.columns)) # 6열

#%%

rowcnt = len(ndf) #  전체 행의 갯수 : 3건

# 과목별 총점, 평균을 위한 행 추가
ndf.loc['총점'] = 0
ndf.loc['평균'] = 0

#%%

print("# 과목별 총점 및 평균 #")
print("# 과목의 총 갯수:", subject_cnt) # 4개

for col_cnt in range(subject_cnt):
    cols = ndf.iloc[:, col_cnt]    # 각 칼럼의 과목별 전체 학생 데이터의 시리즈(Series)
    tot = 0
    for val in cols:
        tot += val
        
    subname = ndf.columns[col_cnt]
    
    # ndf.iloc[rowcnt, col_cnt] = tot
    # ndf.iloc[rowcnt+1, col_cnt] = tot // rowcnt
    ndf.loc['총점', subname] = tot
    ndf.loc['평균', subname] = tot // rowcnt
    
print(ndf)    


