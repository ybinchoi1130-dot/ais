#!/usr/bin/env python
# coding: utf-8

# ## 10-1 자료형 살펴보기
#
# 판다스의 자료형인 카테고리(category)
#   - 범주형 자료형
#   - 메모리를 적게 사용하고 속도도 빠르다
#   - 문자열과 차이
#     - 문자열은 행마다 데이터를 저장
#     - 데이터의 고유한 값을 한 번만 저장하고 실제 데이터는 코드화
#   - 정렬(sort), 그룹화(groupby) 할 때 효율적
#
# astype(자료형) : 자료형 변환
#   - 파이썬 자료형: bool, int, str, float, datetime, object
#   - 판다스 자료형: 
#     - 정수형: int8, int16, int32, int64
#     - 실수형: float32, float64
#     - 범주형: category
#     - 날짜형: datetime64, datetime[ns](나노초, 10억분의 1), timedelta64(시간차)
#   ※ 변환하려는 데이터 중에 단 하나라도 바꿀 수 없는 데이터가 있다면
#     즉시 에러를 발생시키고 실행을 멈춤
#   ★ 데이터가 완벽하게 깔끔할 때만 사용할 수 있다. 
#
# to_numeric()
#   - 숫자형(정수, 실수)으로 변환
#   - 문자를 숫자로 바꿀 때만 사용
#   - 에러가 발생 시 유연하게 처리할 수 있다.
#   - 에러처리 옵션: errors
#     - raise: 기본값. 변환할 수 없는 값이 있을 때 astype()과 같이 에러를 발생
#     - coerce: 변환할 수 없는 값이 있을 때 NaN(결측치). 나중에 결측치 처리 가능
#     - ignore: 변환할 수 없는 값이 있을 때 그대로 사용. 변환하지 않고 원래 데이터를 유지
#   - 옵션: downcast= integer, float
#     - 데이터의 크기를 스스로 판단해서 메모리를 가장 적게 차지하는 숫자형으로 압축해 줌

# In[29]:

import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")


# In[30]:

print(tips.dtypes)

#%%

# ## 10-2 자료형 변환하기

# #### [Do It! 실습] 문자열로 변환하기

# In[32]:

# 타입변환: 문자열('str')로 변환
# 컬럼추가: 'sex_str'
tips['sex_str'] = tips['sex'].astype('str')
print(tips.dtypes)

#%%

# #### [Do It! 실습] 숫자로 변환하기

# In[18]:

# 원래 있던 타입을 다른 타입으로 변경
# 컬럼('total_bill'): float64 -> str
tips['total_bill'] = tips['total_bill'].astype('str') 
print(tips.dtypes)


# In[19]:

# 다시 원래 타입을호 변경
# 컬럼('total_bill'): str -> 파이썬타입(float) -> 판다스(float64)
# 파이썬 타입(float)를 하면 판다스(float64)로 변환된다.
# 운영체제(OS)에 맞춰서 변환: 32bit, 64bit에 따라 달라짐
tips['total_bill'] = tips['total_bill'].astype('float') 
print(tips.dtypes)

#%%

# 명시적으로 float64로 변환
tips['total_bill'] = tips['total_bill'].astype('str') 
tips['total_bill'] = tips['total_bill'].astype('float64') 
print(tips.dtypes)

#%%

# 명시적으로 float32로 변환
tips['total_bill'] = tips['total_bill'].astype('str') 
tips['total_bill'] = tips['total_bill'].astype('float32') 
print(tips.dtypes)

#%%

# 정수형으로 변환: 
# 파이썬 자료형: int   -> int64
# 판다스 자료형: int32 -> int32
# 판다스 자료형: int34 -> int64
tips['total_bill_int'] = tips['total_bill'].astype('int') 
tips['total_bill_int32'] = tips['total_bill'].astype('int32') 
tips['total_bill_int64'] = tips['total_bill'].astype('int64') 
print(tips.dtypes)

#%%


# #### [Do It! 실습] 숫자형으로 변환하는 to_numeric() 메서드 사용하기

# In[20]:

# 데이터프레임의 10개를 복사
tips_sub_miss = tips.head(10).copy()

print(tips_sub_miss.dtypes)

# total_bill의 타입: float64

#%%

# 판다스 버전: 2.x
# 오류: TypeError: Invalid value 'missing' for dtype 'float64'
# ※ 자료형이 float64에 문자열을 넣을 수 없다.
# tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'
# print(tips_sub_miss)

#%%

# 컬럼('total_bill')을 오브젝트('object') 타입으로 변환
tips_sub_miss['total_bill'] = tips_sub_miss['total_bill'].astype('object')
print(tips_sub_miss.dtypes) # total_bill:  object

# In[21]:

# 변경 행: [1, 3, 5, 7]    
# 컬럼('total_bill')에 문자열 'missing'을 넣음
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'
print(tips_sub_miss)

# In[22]:

# ValueError: Unable to parse string "missing" at position 1
# 문자열('missing')을 숫자형으로 변환하는 방법을 모르기 때문
# pd.to_numeric(tips_sub_miss['total_bill'])  # 오류


# In[23]:

print(pd.__version__) # 3.0.5

#%%

# ValueError: invalid error value specified    
# errors='ignore': 변환할 수 없는 값이 있을 때 해당 값을 그대로 사용하라.
# 판다스 버전: 2.x 지원중단.
# tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'], errors='ignore')
# print(tips_sub_miss)


# In[24]:


print(tips_sub_miss.dtypes)


# In[25]:

# errors='coerce'
# 변환할 수 없는 값: nan
tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'],
                                            errors='coerce')
print(tips_sub_miss)


# In[26]:


print(tips_sub_miss.dtypes)


#%%
# ## 10-3 범주형 데이터

# #### [Do It! 실습] 범주형으로 변환하기
# 범주형을 사용하면 문자열보다 메모리 사용량을 절감

# In[27]:

# 메모리 사용량 확인
# 컬럼('sex'): category -> str
tips['sex'] = tips['sex'].astype('str') 
tips.info() # 데이터프레임 정보 출력
# memory usage: 14.8 KB


# In[28]:

# 컬럼('sex'): str -> category
tips['sex'] = tips['sex'].astype('category')
tips.info()
# memory usage: 12.2 KB

#%%

# THE END


