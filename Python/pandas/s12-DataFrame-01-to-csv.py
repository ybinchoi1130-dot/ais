# 판다스(pandas)

# 데이터프레임 CSV(Comma Separated Values) 다루기
# CSV(Comma Separated Values)
#   - 콤마 즉 쉼표(,)로 구분한 텍스트 데이터 및 텍스트 파일
# 텍스트 파일 포맷: 
#   - CSV(Comma Separated Values)  구분자가 콤마(,)
#   - TSV(Tab Separated Values)    구분자가 탭
#   - SSV(Space Separated Values)  구분자가 스페이스(공백)

# 파일 처리
#   - DataFrame.to_csv(filename) 
#     데이터프레임 객체를 텍스트(csv) 파일로 저장
#   - DataFrame = pandas.read_csv(filename) 
#     판다스가 텍스트(csv) 파일을 읽어서 데이터프레임 객체를 생성

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

# CSV 파일로 저장
# 데이터프레임.to_csv(파일이름)
# 현재 데이터프레임의 정보를 지정된 텍스트 파일로 저장
df.to_csv("학생정보.txt")

#%%

# CSV 파일 읽기
rdf = pd.read_csv("학생정보.txt")
print(rdf)

#%%

# 컬럼 이름 변경
rdf.rename(columns={ 'Unnamed: 0': 'Index'}, inplace=True)
print(rdf)

#%%

# 원본(df)와 동일한 형태로 변경
# 컬럼('이름')을 인덱스로 이동
ndf = rdf.set_index('Index')
print(ndf)

#%%

# 읽은 원본의 데이터프레임을 변경
# 컬럼('이름')을 인덱스로 이동
rdf.set_index('Index', inplace=True)
print(rdf)


