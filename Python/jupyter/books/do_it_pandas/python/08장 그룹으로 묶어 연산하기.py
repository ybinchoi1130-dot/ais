#!/usr/bin/env python
# coding: utf-8

# ## 08-1 데이터 집계하기

# #### [Do It! 실습] groupby() 메서드로 데이터 집계하기

# In[1]:


import pandas as pd

df = pd.read_csv('../data/gapminder.tsv', sep='\t')


# In[2]:


avg_life_exp_by_year = df.groupby('year')["lifeExp"].mean()
print(avg_life_exp_by_year)


# In[3]:


years = df.year.unique()
print(years)


# In[4]:


y1952 = df.loc[df.year == 1952, :]
print(y1952)


# In[5]:


y1952_mean = y1952["lifeExp"].mean()
print(y1952_mean)


# ### groupby() 메서드와 함께 사용하는 집계 메서드

# In[6]:


continent_describe = df.groupby('continent')["lifeExp"].describe()
print(continent_describe)


# ### agg() 메서드와 groupby() 메서드 조합하기

# #### [Do It! 실습] 다른 라이브러리의 집계 함수 사용하기

# In[7]:


import numpy as np

cont_le_agg = df.groupby('continent')["lifeExp"].agg(np.mean)
print(cont_le_agg)


# #### [Do It! 실습] 사용자 집계 함수 사용하기

# In[8]:


def my_mean(values):
    n = len(values)   # 숫자 개수를 구합니다.
    sum = 0           # 합계를 0으로 초기화합니다.
    for value in values:
        sum += value  # 각 값을 더합니다.
    return sum / n    # 합계를 숫자 개수로 나눈 값을 반환합니다.


# In[9]:


agg_my_mean = df.groupby('year')["lifeExp"].agg(my_mean)
print(agg_my_mean)


# In[10]:


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
        "lifeExp": "mean",
        "pop": "median",
        "gdpPercap": "median"
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


# ## 08-2 데이터 변환하기

# ### 표준점수 계산하기

# #### [Do It! 실습] 표준점수 계산 함수 만들기

# In[16]:


def my_zscore(x):
    return((x - x.mean()) / x.std())


# In[17]:


transform_z = df.groupby('year')["lifeExp"].transform(my_zscore)
print(transform_z)


# In[18]:


print(df.shape)


# In[19]:


print(transform_z.shape)


# In[20]:


from scipy.stats import zscore

sp_z_grouped = df.groupby('year')["lifeExp"].transform(zscore)
sp_z_nogroup = zscore(df["lifeExp"])

print(transform_z.head())


# In[21]:


print(sp_z_grouped.head())


# In[22]:


print(sp_z_nogroup[:5])


# ### 평균값으로 결측값 채우기

# #### [Do It! 실습] 평균값으로 결측값 채우기 

# In[23]:


import seaborn as sns
import numpy as np

np.random.seed(42)

tips_10 = sns.load_dataset("tips").sample(10)


# In[24]:


tips_10.loc[
    np.random.permutation(tips_10.index)[:4],
    "total_bill"
] = np.NaN

print(tips_10)


# In[25]:


count_sex = tips_10.groupby('sex').count()
print(count_sex)


# In[26]:


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


tips = sns.load_dataset('tips')
print(tips.shape)


# In[29]:


print(tips['size'].value_counts())


# In[30]:


tips_filtered = (
    tips
    .groupby("size")
    .filter(lambda x: x["size"].count() >= 30)
)


# In[31]:


print(tips_filtered.shape)


# In[32]:


print(tips_filtered['size'].value_counts())


# ## 08-4 그룹 객체

# ### 그룹 객체란?

# In[33]:


tips_10 = sns.load_dataset('tips').sample(10, random_state=42)
print(tips_10)


# In[34]:


grouped = tips_10.groupby('sex')
print(grouped)


# In[35]:


print(grouped.groups)


# #### [Do It! 실습] 그룹 객체로 여러 열에 집계 함수 적용하기

# In[36]:


avgs = grouped.mean(numeric_only=True)
print(avgs)


# In[37]:


print(tips_10.columns)


# #### [Do It! 실습] 그룹 추출하고 순회하기

# In[38]:


female = grouped.get_group('Female')
print(female)


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

# In[42]:


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


# In[47]:


group_method = tips_10.groupby(['sex',
                                'time']).mean(numeric_only=True).reset_index()
print(group_method)


# In[48]:


group_param = tips_10.groupby(['sex', 'time'],
                              as_index=False).mean(numeric_only=True)
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




