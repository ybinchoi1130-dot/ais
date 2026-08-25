# In[49]:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pit    

"""
데이터셋 설명
ig_type: 간선유형('학교')

"""
#%%

filename = '../data/epi_sim.zip'
print(f"파일 이름: {filename}")
print(f"파일 {filename} 읽는 중...")

intv_df = pd.read_csv('../data/epi_sim.zip')
print(intv_df)


# In[50]:


count_only = (
    intv_df
    .groupby(["rep", "intervened", "tr"]) #그룹 컬럼
    ["ig_type"] # 집계 대상 컬럼
    .count()    # 건수 집계
)

print(count_only)


# In[51]:

# 집계대상 컬럼[ig_type]이 1개이므로
# 결과는 시리즈이다.

print(type(count_only))


# In[52]:


print(count_only.index)


# In[53]:

# 레벨: level =[0,1,2]
# 멀티 인덱스( MuitiIndex)의 순번:
    # - 0번째('rep')
    # - 1번째('intervened')
    # - 2번째('tr')
# 레벨로 지정된 그룹별로 평균값(mean)을 구함
count_mean = count_only.groupby(level=[0, 1, 2]).mean()
print(count_mean.head())


# In[54]:

# 위의 2개의 과정을 하나로 매서드 체이닝을 통해서 연속적인 처리 
count_mean = (
    intv_df
    .groupby(["rep", "intervened", "tr"])["ig_type"]
    .count() # count_only
    .groupby(level=[0, 1, 2])
    .mean()  # count_mean
)
print(count_mean.head())

#%%
# 값은 같지만 데이터 타입이 다르다. equals 사용할 경우 값과 데이터 인덱스 모두 비교
print(count_only.equals(count_mean)) # False

#각 항목별로 하나씩 비교 후 모든 항목이 일치하는지 확인

count_equals=(count_only == count_mean).all() # True
print(count_equals)

# In[55]:


import seaborn as sns
import matplotlib.pyplot as plt

fig = sns.lmplot(data=count_mean.reset_index(),
                 x="intervened",    # x축
                 y="ig_type",       # y축
                 hue="rep",         # 색상구분
                 col="tr",          #화면분할
                 fit_reg=False,     #추세선(감추기)
                 palette="viridis") # 색상테마

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

