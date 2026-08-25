# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:53:01 2026

@author: shyun
"""

#%%

"""
melt()로 늘린 Long format 데이터를 다시 원래 Wide format 형태로 되돌릴 때는 pivot() 또는 pivot_table()을 사용
두 메서드의 가장 큰 차이는 중복 데이터의 집계(Aggregation) 기능 지원 여부

pivot() vs pivot_table() 한눈에 비교
-------------------------------------------------------------------------------
구분            pivot()                       pivot_table()
-------------------------------------------------------------------------------
중복 데이터     에러 발생 (ValueError)        aggfunc로 자동 처리
집계 연산       불가                          가능 (mean, sum, count 등)
결측치 채우기   미지원 (.fillna() 별도 사용)  fill_value 파라미터 지원
소계/총계       미지원                        margins=True 지원
"""

#%%

#  pivot() 사용법 (중복 데이터가 없을 때)
# 행과 열 인덱스 조합이 유일(Unique)할 때 가장 간단하고 직관적으로 사용

import pandas as pd

# 1. melt된 Long format 데이터 준비
melted_df = pd.DataFrame({
    '이름': ['철수', '영희', '철수', '영희'],
    '과목': ['국어', '국어', '수학', '수학'],
    '점수': [90, 80, 85, 95]
})

print(melted_df)

#%%

#  pivot 적용
# 주의: (index, columns) 조합에 중복된 행이 존재하면 
# ValueError: Index contains duplicate entries, cannot reshape 에러가 발생

wide_df = melted_df.pivot(
    index='이름',      # 행 인덱스로 사용할 열
    columns='과목',    # 새로운 열(Column) 헤더가 될 열
    values='점수'      # 채워 넣을 데이터 값
).reset_index()

print(wide_df)

#%%

# 컬럼 축 이름(name) 정리 (선택사항)
# 데이터 자체의 값을 변경하지는 않지만, 
# 데이터 프레임을 출력했을 때 시각적으로 거슬리는 
# 상단의 열 인덱스 명칭을 지운다. 
wide_df.columns.name = None

print(wide_df)

#%%

###############################################################################
# pivot_table() 사용법 (중복 데이터가 있거나 요약이 필요할 때)
# 동일한 인덱스-컬럼 조합의 값이 여러 개 있거나 평균/합계 등의 집계 연산이 필요할 때 사용
###############################################################################

#%%
# 중복 행이 포함된 데이터 (철수의 국어 시험 기록이 2개인 경우)
dup_df = pd.DataFrame({
    '이름': ['철수', '철수', '영희', '철수', '영희'],
    '과목': ['국어', '국어', '국어', '수학', '수학'],
    '점수': [90, 96, 80, 85, 95]
})

print(dup_df)

#%%
 
# pivot_table 적용 (평균값으로 집계)
wide_table = dup_df.pivot_table(
    index='이름',
    columns='과목',
    values='점수',
    aggfunc='mean'    # 집계 함수 (기본값: 'mean', 'sum', 'max', 'count' 등 가능)
).reset_index()

wide_table.columns.name = None

print(wide_table)




