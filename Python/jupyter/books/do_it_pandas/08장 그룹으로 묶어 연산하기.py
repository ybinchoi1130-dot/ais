#!/usr/bin/env python
# coding: utf-8

# ## 08-1 데이터 집계하기

# #### [Do It! 실습] groupby() 메서드로 데이터 집계하기

# In[1]:


import pandas as pd

df = pd.read_csv('../data/gapminder.tsv', sep='\t')


# In[2]:

# 그룹 : year    
# 컬럼 : lifeExp
# 평균 : mean()

avg_life_exp_by_year = df.groupby('year')["lifeExp"].mean()
print(avg_life_exp_by_year)


# In[3]:


years = df.year.unique()
print(years)

#%%

years2 =df["year"].unique()
print(years2)

print(df.year.value_counts())

"""
year
1952    142
1957    142
1962    142
1967    142
1972    142
1977    142
1982    142
1987    142
1992    142
1997    142
2002    142
2007    142
"""
#%%
# 빈도수의 값으로 오름차순으로 정렬
print(df.year.value_counts(ascending=True))

#%%
# 년도로 정렬 오름차순으로 정렬
print(df["year"].value_counts().sort_index(ascending=False))

#%%
print(df.groupby('year')['lifeExp'].count())

#%%
print(df.groupby('year')['lifeExp'].min())

#%%
print(df.groupby('year')['lifeExp'].max())

#%%
#표준편차
print(df.groupby('year')['lifeExp'].std())

# In[4]:


y1952 = df.loc[df.year == 1952, :]
print(y1952)


# In[5]:


y1952_mean = y1952["lifeExp"].mean()
print(y1952_mean)


# ### groupby() 메서드와 함께 사용하는 집계 메서드

# In[6]:
# 요약 통계 : describe()
# 그룹 : 대륙별  continent
# 컬럼 : lifeExp
continent_describe = df.groupby('continent')["lifeExp"].describe()
print(continent_describe)


# ### agg() 메서드와 groupby() 메서드 조합하기

# #### [Do It! 실습] 다른 라이브러리의 집계 함수 사용하기

# In[7]:
# 판다스는 넘파이를 기반으로 만든 프레임워크

# agg 매서드에 평균을 구하는 넘파이 함수를 전달
import numpy as np

cont_le_agg = df.groupby('continent')["lifeExp"].agg(np.mean)
print(cont_le_agg)



#%%
#판다스의 평균 함수를 사용
cont_le_mean = df.groupby('continent')['lifeExp'].mean()

# In[8]:
# 사용자의 평균 계산 함수
# 파라미터 : value는 지정된 그룹('year') 단위로 전달된다.
my_mean_cnt = 0
def my_mean(values):
    global my_mean_cnt
    my_mean_cnt += 1
    print("[my_mean] count=",my_mean_cnt)
    print(values)
    
    n = len(values)   # 숫자 개수를 구합니다.
    sum = 0           # 합계를 0으로 초기화합니다.
    for value in values:
        sum += value  # 각 값을 더합니다.
    return sum / n    # 합계를 숫자 개수로 나눈 값을 반환합니다.7


# In[9]:


agg_my_mean = df.groupby('year')["lifeExp"].agg(my_mean)
print(agg_my_mean)


# In[10]:
# 연도나 대륙과 상관없이 전체 기대 수명의 평균!
# diff_value : 연도나 대륙과 상관없이 전체 기대 수명의 평균
# 결과 : 그룹별 기대수명의 평균 - 전체 기대 수명의 평균
def my_mean_diff(values, diff_value):
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    mean = sum / n
    return(mean - diff_value)


# In[11]:


global_mean = df["lifeExp"].mean()
print(global_mean)


# In[12]:


agg_mean_diff = (
    df
    .groupby("year")
    ["lifeExp"]
    .agg(my_mean_diff, diff_value=global_mean)
)

print(agg_mean_diff)


# ### 여러 개의 집계 함수 한 번에 사용하기
#%%

# 데이터프레임의 info()와 같은 정보를 데이터프레임으로 생성
info_df=pd.DataFrame({
    'Non-Null Count':df.count(),
    'Dtype':df.dtypes
    })
print(df.count())
print(df.dtypes)

#%%
# 인덱스를 컬럼으로 이동
# 컬럼으로 이동된 인덱스명('index')를 'Colum'으로 변경

info_df2=pd.DataFrame({
    'Non-Null Count':df.count(),
    'Dtype':df.dtypes
    }).reset_index().rename(columns={'index':'Column'})
print(df.count())
print(df.dtypes)

# In[13]:


gdf = (
    df
    .groupby("year")
    ["lifeExp"]
    .agg([np.count_nonzero, np.mean, np.std])
)

print(gdf)


# #### [Do It! 실습] agg()나 aggregate() 메서드에 딕셔너리 사용하기

# ##### 1. 데이터프레임에 사용하기

# In[14]:


gdf_dict = df.groupby("year").agg(
    {
        "lifeExp": "mean",     #기대수명의 평균
        "pop": "median",       #인구수의 중간값
        "gdpPercap": "median"  #GDP의 중간값
    }
)

print(gdf_dict)


# ##### 2. 시리즈에 사용하기

# In[15]:


gdf = (
    df
    .groupby("year")
    ["lifeExp"]
    .agg(
        [
            np.count_nonzero,
            np.mean,
            np.std,
        ]
    )
    .rename(
        columns={
            "count_nonzero": "count",
            "mean": "avg",
            "std": "std_dev",
            }
    )
    .reset_index() # 평탄화한 데이터프레임 반환하기
)

print(gdf)
#%%

# ## 08-2 데이터 변환하기

# ### 표준점수 계산하기

# #### [Do It! 실습] 표준점수 계산 함수 만들기


# 표준점수는 응시자의 원점수가
# 전체 수험생의 평균 점수로부터 얼마나 떨어져 있는지를
# 표준편차를 기준으로 변환한 점수

# In[16]:

# 표준편차를 구하는 함수 
cntx = 0
def my_zscore(x):
    global cntx
    cntx += 1
    print(f"[{cntx:02}] x:{len(x)}, mean :{round(x.mean(),2)}, std:{round(x.std(),2)}")
    print("="*30)
    print(x)
    print("="*30)
    return((x - x.mean()) / x.std())


# In[17]:


transform_z = df.groupby('year')["lifeExp"].transform(my_zscore)
print(len(transform_z))


# In[18]:


print(df.shape)


# In[19]:


print(transform_z.shape)


# In[20]:
"""
사이파이(SciPy)는 파이썬을 이용한 과학 기술 및 수학적 계산을 위한 라이브러리입니다. 
'Scientific Python'의 줄임말로, 앞서 설명해 드린 넘파이(NumPy)를 기반으로 
그 위에 구축된 확장판이라고 생각하시면 이해하기 쉽습니다
"""

from scipy.stats import zscore

sp_z_grouped = df.groupby('year')["lifeExp"].transform(zscore)
sp_z_nogroup = zscore(df["lifeExp"])

print(transform_z.head())

# sp_z_grouped VS transform_z VS sp_z_nogroup : 결과값이 모두 다르다
# 표준 편차를 구하는 방식의 차이 

#%%

def my_zscore(x):
    return((x-x.mean())/x.std(ddof=0))
transform_z2 = df.groupby('year')["lifeExp"].transform(my_zscore)

# In[21]:


print(sp_z_grouped.head())


# In[22]:


print(sp_z_nogroup[:5])


# ### 평균값으로 결측값 채우기

# #### [Do It! 실습] 평균값으로 결측값 채우기 
############################################################
"""
결측치 : 누락된 상태
- NaN : np.nan(넘파이), Not a Number, 숫자가 아니다
- NA :  Not Availiable, 이용할 수 없다.  
- fillna() : 누락된 데이터를 채워라   
- None : 파이썬의 자료형, 판다스(NaN)
- pd.NA : 판다스
넘파이 -> np.nan 
판다스 -> pd.NA      
"""    
# In[23]:

import pandas as pd
import seaborn as sns
import numpy as np

np.random.seed(42)

tips_10 = sns.load_dataset("tips").sample(10)

tipx_10 = tips_10.copy()
# In[24]:


tips_10.loc[
    np.random.permutation(tips_10.index)[:4],
    "total_bill"
] = np.nan

print(tips_10)

#%%

tipx_10.loc[
    np.random.permutation(tipx_10.index)[:4],
    "total_bill"
]= np.nan


print(np.random.permutation([1,2,3,4,5]))


# In[25]:


count_sex = tips_10.groupby('sex').count()
print(count_sex)
#%%
"""
        total_bill  tip  smoker  day  time  size
sex                                             
Male             7    7       7    7     7     7
Female           3    3       3    3     3     3

"""

# In[26]:

#평균값으로 결측값을 채움

avg_sex_mean = tips_10.groupby("sex")['total_bill'].agg(np.mean)

print(avg_sex_mean)
#%%
def fill_na_mean(x):
    avg = x.mean() 
    return x.fillna(avg)

total_bill_group_mean = (
    tips_10
    .groupby("sex")
    .total_bill
    .transform(fill_na_mean)
)


# In[27]:


tips_10["fill_total_bill"] = total_bill_group_mean
print(tips_10[['sex', 'total_bill', 'fill_total_bill']])


# ## 08-3 원하는 데이터 걸러내기

# #### [Do It! 실습] 데이터 필터링하기

# In[28]:

import pandas as pd
import seaborn as sns
import numpy as np


tips = sns.load_dataset('tips')
print(tips.shape)

#%%
print(tips['time'].unique())
# Categories (2, str): ['Lunch', 'Dinner']
# In[29]:

print(tips['day'].value_counts())
print(tips['time'].value_counts())
print(tips['size'].value_counts())

#%%

print(tips['day'].unique())
# Categories (4, str): ['Thur', 'Fri', 'Sat', 'Sun']

# In[30]:

# 함수(filterd) : 특정한 조건에 해당 데이터를 추출
tips_filtered = (
    tips
    .groupby("size")
    .filter(lambda x: x["size"].count() >= 30)
)


# In[31]:


print(tips_filtered.shape)


# In[32]:


print(tips_filtered['size'].value_counts())

#%%
# ## 08-4 그룹 객체

# ### 그룹 객체란?
# 평탄화(flatten):
# - 일반 데이터프레임처럼 하기 위해 reset_index() 사용
# - reset_index()를 하면 인덱스의 값이 컬럼으로 이동




# In[33]:


import pandas as pd
import seaborn as sns
import numpy as np

#np.random.seed(42) :모든 랜덤시드에 값을 준다

tips_10 = sns.load_dataset('tips').sample(10, random_state=42) #명령어 한해서만
print(tips_10)


# In[34]:


grouped = tips_10.groupby('sex')
print(grouped)


# In[35]:


print(type(grouped.groups),grouped.groups)

# 딕셔너리 형태: 키(sex), 값(index)
# #### [Do It! 실습] 그룹 객체로 여러 열에 집계 함수 적용하기

# In[36]:

# 숫자인 컬럼만 연산을 수행: numeric_only =True
avgs = grouped.mean(numeric_only=True)
print(avgs)

#%%
# category dtype does not support aggregation 'mean'
# category 범주형 자료형, 분류라서 안된다.
avgs = grouped.mean()
print(avgs)

# In[37]:


print(tips_10.columns)


# #### [Do It! 실습] 그룹 추출하고 순회하기

# In[38]:

female = grouped.get_group('Female')
print(female)

#%%

male = grouped.get_group('Male')
print(male)

# In[39]:


for sex_group in grouped:
    print(sex_group)


# In[40]:


#print(grouped[0])  # 오류


# In[41]:


for sex_group in grouped:
    # 객체 자료형 (튜플)
    print(f'the type is: {type(sex_group)}\n')

    # 객체 길이 (2)
    print(f'the length is: {len(sex_group)}\n')

    # 첫 번째 요소
    first_element = sex_group[0]
    print(f'the first element is: {first_element}\n')

    # 첫 번째 요소의 자료형(문자열)
    print(f'it has a type of: {type(sex_group[0])}\n')

    # 두 번째 요소
    second_element = sex_group[1]
    print(f'the second element is:\n{second_element}\n')

    # 두 번째 요소의 자료형 (데이터프레임)
    print(f'it has a type of: {type(second_element)}\n')

    # 그룹 출력
    print(f'what we have:')
    print(sex_group)

    # for문 중단
    break


# #### [Do It! 실습] 여러 개의 변수로 그룹화하고 결과 평탄화하기
# 평탄화 : 일반 데이터프레임처럼 하기 위해 reset_index() 사용
# reset_index()를 하면 인덱스의 값이 컬럼으로 이동
# In[42]:

# 그룹을 여러 개로 지정하면 다중 인덱스 형태로 구성된다. 
# 단계별 그룹 
bill_sex_time = tips_10.groupby(['sex', 'time'])

group_avg = bill_sex_time.mean(numeric_only=True)


# In[43]:


print(type(group_avg))


# In[44]:


print(group_avg)


# In[45]:


print(group_avg.columns)


# In[46]:


print(group_avg.index)

#%%

print(group_avg.loc[('Male','Lunch')])
print(group_avg.loc[('Female','Dinner')])

# In[47]:


group_method =( tips_10.groupby(['sex','time'])
    .mean(numeric_only=True)
    .reset_index()) # 데이터 평탄화
    
print(group_method)

#%%
# 멀티 인덱스였던 컬럼('sex','time')이 컬럼으로 이동
# 인덱스는 새로 0부터 순차적으로 부여

"""
      sex    time  total_bill       tip      size
0    Male   Lunch   28.440000  2.560000  2.000000
1    Male  Dinner   18.616667  2.928333  2.666667
2  Female   Lunch   12.740000  2.260000  2.000000
3  Female  Dinner   15.380000  3.000000  2.000000

"""
# In[48]:

# 매서드 groupby의 옵션 as_index=False를 지정하여
# reset_index() 효과를 냄
group_param = (tips_10.groupby(['sex', 'time'],
     as_index=False)
     .mean(numeric_only=True))

print(group_param)


# ## 08-5 다중 인덱스 다루기

# #### [Do It! 실습] 다중 인덱스 다루기

# In[49]:


intv_df = pd.read_csv('../data/epi_sim.zip')
print(intv_df)


# In[50]:


count_only = (
    intv_df
    .groupby(["rep", "intervened", "tr"])
    ["ig_type"]
    .count()
)

print(count_only)


# In[51]:


print(type(count_only))


# In[52]:


print(count_only.index)


# In[53]:


count_mean = count_only.groupby(level=[0, 1, 2]).mean()
print(count_mean.head())


# In[54]:


count_mean = (
    intv_df
    .groupby(["rep", "intervened", "tr"])["ig_type"]
    .count()
    .groupby(level=[0, 1, 2])
    .mean()
)
print(count_mean.head())


# In[55]:


import seaborn as sns
import matplotlib.pyplot as plt

fig = sns.lmplot(data=count_mean.reset_index(),
                 x="intervened",
                 y="ig_type",
                 hue="rep",
                 col="tr",
                 fit_reg=False,
                 palette="viridis")

plt.show()


# In[56]:


cumulative_count = (
    intv_df
    .groupby(["rep", "intervened", "tr"])["ig_type"]
    .count()
    .groupby(level=["rep"])
    .cumsum()
    .reset_index()
)

fig = sns.lmplot(
    data=cumulative_count,
    x="intervened",
    y="ig_type",
    hue="rep",
    col="tr",
    fit_reg=False,
    palette="viridis"
)

plt.show()


# In[ ]:




