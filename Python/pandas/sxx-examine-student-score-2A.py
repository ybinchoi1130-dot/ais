# -*- coding: utf-8 -*-

# 학생 성적 처리
# 학생별 총점, 평균을 구함

#%%
import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장 
# dict로 데이터프레임 생성
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df, '\n')

#%%
# '이름'을 인덱스로 지정
ndf = df.set_index('이름')
print(ndf)

# 전체 행, 전체 칼럼 새로운 데이터프레임으로 만들어서 확인
# sr = ndf.loc[:,'수학':'체육'] 
sr = ndf.loc[:,:]

print(sr)

#%%
#  학생별 총점, 평균을 구하기 위해서
print(ndf.columns)
subject_cnt = len(ndf.columns) 
print("과목건수: ", subject_cnt) # 4건

#%%

# 칼럼 추가
ndf['총점'] = 0
ndf['평균'] = 0
print(ndf)

#%%

print("# 학생별 총점 및 평균 #")

student_len = len(ndf) # 행의 건수
print("총 학생 수: ", student_len) # 3명

for n in range(student_len): # n: 0, 1, 2
    subjects = ndf.iloc[n, :] # 하나의 행을 추출(학생별)
    tot = 0
    # 각 학생의 과목을 탐색
    for score in subjects: # 칼럼 1개씩 탐색하면 누적
        tot += score
    ndf.iloc[n,4] = tot                # 총점
    ndf.iloc[n,5] = tot // subject_cnt # 평균

print(ndf)    



