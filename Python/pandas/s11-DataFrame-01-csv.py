# 판다스(pandas)

# 데이터 프레임 CSV (coma separated values) 다루기
# - 콤마 즉 ,(쉼표)로 구분한 텍스트 데이터 및 텍스트 파일 
# 텍스트 파일 포맷:
#   -csv : 구분자가 ,
#   -tsv : 구분자가 tab
#   -ssv : 구분자가 스페이스(공백)

# 파일처리
#   -DataFrame.to_csv(filename) 데이터프레임 객체를 텍스트(csv) 파일로 저장
#   -DataFrame = pandas.read_csv(filename) 
#    판다스가 텍스트(csv) 파일을 읽어서 데이터프레임 객체를 생성
#%%

import pandas as pd

# list data
data = [  
    [22, '연세대'], #0행
    [23, '수원대'], #1행
    [24, '서울대']  #2행
]

df = pd.DataFrame(data,
                  index=['영빈','정명','수정'],
                  columns=['나이','학교'])

print(df)

#%%
# CSV 파일로 저장
# 데이터프레임.to.csv(파일이름)
# 현재 데이터프레임의 정보를 지정된 텍스프 파일로 저장
df.to_csv("학생정보.txt")
#%%
# CSV 파일 읽기
rdf = pd.read_csv("학생정보.txt")
print(rdf)

#%%
rdf.rename(columns={'Unnamed: 0': '이름'},inplace=True)
print(rdf)
#%% 
ndf = rdf.set_index('이름')
print(ndf)