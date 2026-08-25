#!/usr/bin/env python
# coding: utf-8

# In[88]:

# seaborn
# pip install matplotlib
# pip install seaborn    
# pip install scipy

#%%    

# 그래프 반복 호출로 생기는 경고 감추기
import warnings
warnings.filterwarnings('ignore')


# ## 04-1 데이터 시각화란?

# In[89]:


import seaborn as sns

anscombe = sns.load_dataset("anscombe")
print(anscombe)


# ## 04-2 matplotlib 라이브러리란?

# In[90]:


import matplotlib.pyplot as plt


# In[91]:


dataset_1 = anscombe[anscombe['dataset'] == 'I']

plt.plot(dataset_1['x'], dataset_1['y'])
plt.show()


# In[92]:


plt.plot(dataset_1['x'], dataset_1['y'], 'o')
plt.show()


# In[93]:


dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']


#%%
# ### 그림 영역과 하위 그래프 이해하기

# #### [Do It! 실습] 한 번에 4개의 그래프 그리기

# In[94]:


# 2행 2열
fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1) # 0,0
axes2 = fig.add_subplot(2, 2, 2) # 0,1 
axes3 = fig.add_subplot(2, 2, 3) # 1,0
axes4 = fig.add_subplot(2, 2, 4) # 1,2

plt.show()


# In[95]:


fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

plt.show()


# In[96]:


fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

fig.suptitle("Anscombe Data") # 제목

fig.set_tight_layout(True)

plt.show()


# ## 04-3 matplotlib으로 그래프 그리기

# In[97]:


tips = sns.load_dataset("tips")
print(tips)


# ### 일변량 그래프 그리기

# #### [Do It! 실습] 히스토그램 그리기

# In[98]:

# 히스토그램: 빈도수
fig = plt.figure()

axes1 = fig.add_subplot(1, 1, 1)

axes1.hist(data=tips, x='total_bill', bins=10)

axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Frequency')

plt.show()


#%%

# ### 이변량 그래프 그리기

# #### [Do It! 실습] 산점도 그래프 그리기

# In[99]:

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)

axes1.scatter(tips['total_bill'], tips['tip'])

axes1.set_title('Scatterplot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')

plt.show()

#%%
# #### [Do It! 실습] 박스 그래프 그리기

# In[100]:

# boxplot: 상자 수염 그림
# 데이터의 분포 상태와 이상치를 파악
# 이상치: 극단적인 값
# 최대값(Maximum): 정상적인 범위 내에서 가장 큰 값, 윗쪽 수염의 끝
# 제3사분위(Q3,75%): 상위 25%
# 중앙값(Q2, 50%): 데이터의 정중앙, 박스 가로선
# 제1사분위(Q1,25%): 하위 25%
# 최솟값(Minimum): 정상적인 범위 내에서 가장 작은 값, 아랫쪽 수염의 끝

boxplot = plt.figure()
axes1 = boxplot.add_subplot(1, 1, 1)

axes1.boxplot(
    x=[
        tips[tips['sex'] == 'Female']['tip'],
        tips[tips['sex'] == 'Male']['tip']
    ],
    # labels=['Female', 'Male']
    # 버전: 3.9.0
    tick_labels=['Female', 'Male']
)

axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Sex')

plt.show()


# ### 다변량 그래프 그리기

# #### [Do It! 실습] 변수가 여러 개인 그래프 그리기

# In[101]:


colors = {"Female": "#f1a340", "Male": "#998ec3"}

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)

axes1.scatter(data=tips,
              x='total_bill',
              y='tip',
              s=tips['size']**2*10,
              c=tips['sex'].map(colors),
              alpha=0.5)

axes1.set_title('Colored by Sex and Sized by Size')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')

scatter_plot.suptitle('Total Bill vs Tip')

plt.show()


# ## 04-4 seaborn으로 그래프 그리기

# In[102]:


import seaborn as sns
tips = sns.load_dataset("tips")


# In[103]:


sns.set_context("paper")


# ### 다양한 그래프 그려 보기

# #### [Do It! 실습] 일변량 그래프 그리기

# ##### 1. 히스토그램 그리기

# In[104]:


hist, ax = plt.subplots()

sns.histplot(data=tips, x='total_bill', ax=ax)
ax.set_title('Total Bill Histogram')
plt.show()


# ##### 2. 밀도분포 그래프 그리기

# In[105]:


den, ax = plt.subplots()

sns.kdeplot(data=tips, x='total_bill', ax=ax)

ax.set_title('Total Bill Density')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Unit Probability')

plt.show()


# ###### 3. 러그 그래프 그리기

# In[106]:


rug, ax = plt.subplots()

sns.rugplot(data=tips, x='total_bill', ax=ax)
sns.histplot(data=tips, x='total_bill', ax=ax)

ax.set_title('Rug Plot and Histogram of Total Bill')

plt.show()


# ##### 4. 분포 그래프 그리기

# In[107]:


fig = sns.displot(data=tips, x='total_bill', kde=True, rug=True)

fig.set_axis_labels(x_var='Total Bill', y_var='Count')
fig.figure.suptitle('Distribution of Total Bill')

plt.show()


# ##### 5. 막대그래프 그리기

# In[108]:


count, ax = plt.subplots()

sns.countplot(data=tips, x='day', palette='viridis', ax=ax)

ax.set_title('Count of days')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Frequency')

plt.show()


# ### 이변량 그래프 그리기

# #### [Do It! 실습] 이변량 그래프 그리기

# ##### 1. 산점도 그래프 그리기 ①

# In[109]:


scatter, ax = plt.subplots()

sns.scatterplot(data=tips, x='total_bill', y='tip', ax=ax)

ax.set_title('Scatter Plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

plt.show()


# ##### 2. 산점도 그래프 그리기 ②

# In[110]:


reg, ax = plt.subplots()

sns.regplot(data=tips, x='total_bill', y='tip', ax=ax)

ax.set_title('Regression Plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

plt.show()


# In[150]:


fig = sns.lmplot(data=tips, x='total_bill', y='tip')
print(type(fig))
plt.show()


# ##### 3. 조인트 그래프 그리기

# In[112]:


joint = sns.jointplot(data=tips, x='total_bill', y='tip')
joint.set_axis_labels(xlabel='Total Bill', ylabel='Tip')

joint.figure.suptitle('Joint Plot of Total Bill and Tip', y=1.03)

plt.show()


# ##### 4. 육각 그래프 그리기

# In[113]:


hexbin = sns.jointplot(data=tips, x="total_bill", y="tip", kind="hex")

hexbin.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
hexbin.figure.suptitle('Hexbin Joint Plot of Total Bill and Tip', y=1.03)

plt.show()


# ##### 5. 2차원 밀도분포 그래프 그리기

# In[114]:


kde, ax = plt.subplots()

sns.kdeplot(data=tips, x="total_bill", y="tip", fill=True, ax=ax)

ax.set_title('Kernel Density Plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

plt.show()


# In[115]:


kde2d = sns.jointplot(data=tips, x="total_bill", y="tip", kind="kde")

kde2d.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
kde2d.figure.suptitle('Hexbin Joint Plot of Total Bill and Tip', y=1.03)

plt.show()


# ##### 6. 막대그래프 그리기

# In[116]:


import numpy as np

bar, ax = plt.subplots()

sns.barplot(data=tips, x="time", y="total_bill", estimator=np.mean, ax=ax)

ax.set_title('Bar Plot of Average Total Bill for Time of Day')
ax.set_xlabel('Time of Day')
ax.set_ylabel('Average Total Bill')

plt.show()


# ##### 7. 박스 그래프 그리기

# In[117]:


box, ax = plt.subplots()

sns.boxplot(data=tips, x='time', y='total_bill', ax=ax)

ax.set_title('Bar Plot of Total Bill for Time of Day')
ax.set_xlabel('Time of Day')
ax.set_ylabel('Total Bill')

plt.show()


# ##### 8. 바이올린 그래프 그리기

# In[118]:


violin, ax = plt.subplots()

sns.violinplot(data=tips, x='time', y='total_bill', ax=ax)

ax.set_title('Violin plot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')

plt.show()


# In[119]:


box_violin, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

sns.boxplot(data=tips, x='time', y='total_bill', ax=ax1)
sns.violinplot(data=tips, x='time', y='total_bill', ax=ax2)

ax1.set_title('Box Plot')
ax1.set_xlabel('Time of Day')
ax1.set_ylabel('Total Bill')

ax2.set_title('Violin plot')
ax2.set_xlabel('Time of day')
ax2.set_ylabel('Total Bill')

box_violin.suptitle("Comparison of Box Plot with Violin Plot")

box_violin.set_tight_layout(True)

plt.show()


# ##### 9. 관계 그래프 그리기 ①

# In[120]:


fig = sns.pairplot(data=tips)

fig.figure.suptitle('Pairwise Relationships of the Tips Data', y=1.03)

plt.show()


# ##### 10. 관계 그래프 그리기 ②

# In[121]:


pair_grid = sns.PairGrid(tips, diag_sharey=False)

pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.histplot)

plt.show()


# #### [Do It! 실습] 다변량 그래프 그리기

# ##### 1. 그래프에 색상 입히기

# In[122]:


violin, ax = plt.subplots()

sns.violinplot(data=tips,
               x="time",
               y="total_bill",
               hue="smoker",
               split=True,
               palette="viridis",
               ax=ax)

plt.show()


# In[123]:


scatter = sns.lmplot(data=tips,
                     x="total_bill",
                     y="tip",
                     hue="smoker",
                     fit_reg=False,
                     palette="viridis")

plt.show()


# In[124]:


fig = sns.pairplot(tips, hue="time", palette="viridis")

plt.show()


# ##### 2. 그래프 크기와 모양 조절하기

# In[125]:


fig, ax = plt.subplots()

sns.scatterplot(data=tips,
                x="total_bill",
                y="tip",
                hue="time",
                size="size",
                palette="viridis",
                ax=ax)

plt.show()


# #### [Do It! 실습] 그래프 나눠 그리기

# ##### 1. 1개의 범주형 변수로 그래프 나누기

# In[126]:


anscombe = sns.load_dataset("anscombe")


# In[127]:


anscombe_plot = sns.relplot(data=anscombe,
                            x="x",
                            y="y",
                            kind="scatter",
                            col="dataset",
                            col_wrap=2,
                            height=2,
                            aspect=1.6)

anscombe_plot.figure.set_tight_layout(True)

plt.show()


# ##### 2. 여러 개의 범주형 변수로 그래프 나누기

# In[128]:


colors = {
    "Yes": "#f1a340", # 주황색
    "No" : "#998ec3", # 보라색
}

facet2 = sns.relplot(data=tips,
                     x="total_bill",
                     y="tip",
                     hue="smoker",
                     style="sex",
                     kind="scatter",
                     col="day",
                     row="time",
                     palette=colors,
                     height=1.7)

# 여기서부터는 그래프를 꾸미는 코드입니다.
# 나눠진 각 그래프에 제목을 붙입니다.
facet2.set_titles(row_template="{row_name}", col_template="{col_name}")

# 그래프에 범주를 추가하는 코드입니다.
sns.move_legend(facet2,
                loc="lower center",
                bbox_to_anchor=(0.5, 1),
                ncol=2,         # 범주의 열 개수
                title=None,     # 범주 제목
                frameon=False)  # 범주 테두리를 숨깁니다.

facet2.figure.set_tight_layout(True)

plt.show()


# ##### 3. FacetGrid 객체로 그래프 직접 나누기

# In[129]:


facet = sns.FacetGrid(tips, col='time')

facet.map(sns.histplot, 'total_bill')
plt.show()


# In[130]:


facet = sns.FacetGrid(tips, 
                      col='day', 
                      col_wrap=2, 
                      hue='sex', 
                      palette="viridis")

facet.map(plt.scatter, 'total_bill', 'tip')
facet.add_legend()
plt.show()


# In[131]:


facet = sns.FacetGrid(tips, 
                      col='time', 
                      row='smoker', 
                      hue='sex', 
                      palette="viridis")

facet.map(plt.scatter, 'total_bill', 'tip')
plt.show()


# In[132]:


facet = sns.catplot(x="day",
                    y="total_bill",
                    hue="sex",
                    data=tips,
                    row="smoker",
                    col="time",
                    kind="violin",
                    height=3)
plt.show()


# ### seaborn 스타일 알아보기

# #### [Do It! 실습] 스타일 알아보기

# In[133]:


fig, ax = plt.subplots()
sns.violinplot(data=tips, 
               x="time", 
               y="total_bill", 
               hue="sex", 
               split=True, 
               ax=ax)

plt.show()


# In[134]:


# 전체 스타일을 darkgrid로 변경하고 싶다면 아래 코드를 주석 해제하고 실행하세요.
# sns.set_style("darkgrid")
# fig, ax = plt.subplots()
# sns.violinplot(data=tips, 
#                x=”time”, 
#                y="total_bill", 
#                hue="sex", 
#                split=True, 
#                ax=ax)

# 특정 그래프만 다른 스타일로 그리는 코드입니다.
with sns.axes_style("darkgrid"):
    fig, ax = plt.subplots()
    sns.violinplot(data=tips, 
                   x="time", 
                   y="total_bill", 
                   hue="sex", 
                   split=True,
                   ax=ax)

plt.show()


# In[135]:


seaborn_styles = ["darkgrid", "whitegrid", "dark", "white", "ticks"]

fig = plt.figure()
for idx, style in enumerate(seaborn_styles):
    plot_position = idx + 1
    with sns.axes_style(style):
        ax = fig.add_subplot(2, 3, plot_position)
        violin = sns.violinplot(data=tips, x="time", y="total_bill", ax=ax)
        violin.set_title(style)

fig.set_tight_layout(True)
plt.show()


# #### [Do It! 실습] 그래프 컨텍스트 설정하기

# In[136]:


import pandas as pd

contexts = pd.DataFrame({
    "paper": sns.plotting_context("paper"),
    "notebook": sns.plotting_context("notebook"),
    "talk": sns.plotting_context("talk"),
    "poster": sns.plotting_context("poster"),
})
print(contexts)


# In[137]:


context_styles = contexts.columns

fig = plt.figure()
for idx, context in enumerate(context_styles):
    plot_position = idx + 1
    with sns.plotting_context(context):
        ax = fig.add_subplot(2, 2, plot_position)
        violin = sns.violinplot(data=tips, x="time", y="total_bill", ax=ax)
        violin.set_title(context)

fig.set_tight_layout(True)
plt.show()


# ### seaborn 공식 문서를 읽는 방법

# ##### matplotlib의 Axes 객체

# In[138]:


box_violin, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

sns.boxplot(data=tips, x='time', y='total_bill', ax=ax1)
sns.violinplot(data=tips, x='time', y='total_bill', ax=ax2)

ax1.set_title('Box Plot')
ax1.set_xlabel('Time of Day')
ax1.set_ylabel('Total Bill')

ax2.set_title('Violin plot')
ax2.set_xlabel('Time of day')
ax2.set_ylabel('Total Bill')

box_violin.suptitle("Comparison of Box Plot with Violin Plot")

box_violin.set_tight_layout(True)
plt.show()


# In[139]:


print(type(ax2))


# ##### matplotlib의 Figure 객체

# In[140]:


print(type(box_violin))


# ##### seaborn의 객체

# In[141]:


fig = sns.pairplot(data=tips)
fig.figure.suptitle('Pairwise Relationships of the Tips Data', y=1.03)
plt.show()


# In[142]:


print(type(fig))


# ## 04-5 판다스로 그래프 그리기

# #### [Do It! 실습] 판다스로 다양한 그래프 그리기

# ##### 1. 히스토그램 그리기

# In[143]:


fig, ax = plt.subplots()
tips['total_bill'].plot.hist(ax=ax)
plt.show()


# In[144]:


fig, ax = plt.subplots()
tips[['total_bill', 'tip']].plot.hist(alpha=0.5, bins=20, ax=ax)
plt.show()


# ##### 2. 밀도분포 그래프 그리기

# In[145]:


fig, ax = plt.subplots()
tips['tip'].plot.kde(ax=ax)
plt.show()


# ##### 3. 산점도 그리기

# In[146]:


fig, ax = plt.subplots()
tips.plot.scatter(x='total_bill', y='tip', ax=ax)
plt.show()


# ##### 4. 육각 그래프 그리기

# In[147]:


fig, ax = plt.subplots()
tips.plot.hexbin(x='total_bill', y='tip', ax=ax)
plt.show()


# In[148]:


fig, ax = plt.subplots()
tips.plot.hexbin(x='total_bill', y='tip', gridsize=10, ax=ax)
plt.show()


# ##### 5. 박스 그래프 그리기

# In[149]:


fig, ax = plt.subplots()
tips.plot.box(ax=ax)
plt.show()


# In[ ]:




