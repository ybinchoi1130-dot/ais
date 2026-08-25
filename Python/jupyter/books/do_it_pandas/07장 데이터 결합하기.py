#!/usr/bin/env python
# coding: utf-8

# ## 07-1 데이터 묶어 분석하기

# ## 07-2 데이터 연결하기

# In[1]:


import pandas as pd

df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')
print(df1)
             

# In[2]:


print(df2)
          

# In[3]:


print(df3)


# ### 데이터프레임 살펴보기

# In[4]:


print(df1.index)


# In[5]:


print(df1.columns)


# In[6]:


print(df1.values)


# ### 행 연결하기

# #### [Do It! 실습] 행 방향 연결하기

# In[7]:

#행 방향으로 데이터프레임 연결
# 데이터 프레임 :[df1,df2,df3]

row_concat = pd.concat([df1, df2, df3])
print(row_concat)


# In[8]:


print(row_concat.iloc[3, :])


# In[9]:


new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(new_row_series)


# In[10]:


print(pd.concat([df1, new_row_series]))

#%%
# 시리즈를 데이터프레임으로 변환

new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(new_row_series)

new_row_series_df=pd.DataFrame(new_row_series,
                               columns=['A','B','C','D'])

# In[11]:


new_row_df = pd.DataFrame(
    data=[["n1", "n2", "n3", "n4"]],
    columns=["A", "B", "C", "D"],
)
print(new_row_df)


# In[12]:


print(pd.concat([df1, new_row_df]))


# #### [Do It! 실습] 새로운 인덱스 설정하기

# In[13]:

# 옵션 : 원본 데이터의 인덱스를 무시하고 새로운 인덱스를 부여 
# ignore_index = True : 기존 인덱스를 무시
row_concat_i = pd.concat([df1, df2, df3], ignore_index=True)
print(row_concat_i)


# ### 열 연결하기

# #### [Do It! 실습] 열 방향 연결하기

# In[14]:


col_concat = pd.concat([df1, df2, df3], axis="columns")
print(col_concat)


# In[15]:


print(col_concat['A'])


# In[16]:

# 새로운 컬럼('new_col_list') 추가
# ★ 리스트 요소의 갯수와 데이터프레임의 행을 갯수가 일치 

col_concat['new_col_list'] = ['n1', 'n2', 'n3', 'n4']
print(col_concat)


# In[17]:


col_concat['new_col_series'] = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(col_concat)


# In[18]:


print(pd.concat([df1, df2, df3], axis="columns", ignore_index=True))


# ### 인덱스나 열 이름이 다른 데이터 연결하기

# #### [Do It! 실습] 열 이름이 다른 데이터 행 방향 연결하기

# In[19]:
# 복사본을 수정해도 원본의 변화는 없다. 

#df1c = df1 : 그냥 할당하면 원본에도 변화가 생긴다.


# 복사본 = 원본.copy()    

df1c = df1.copy()
df2c = df2.copy()
df3c = df3.copy()


df1c.columns = ['A', 'B', 'C', 'D']
df2c.columns = ['E', 'F', 'G', 'H']
df3c.columns = ['A', 'C', 'F', 'H']
print(df1c)
print(df2c)
print(df3c)


# In[21]:

# 행 방향 결합(연결)
row_concat = pd.concat([df1, df2, df3])
print(row_concat)


# In[22]:


print(pd.concat([df1, df2, df3], join='inner'))


# In[23]:


print(pd.concat([df2,df3], ignore_index=False, join='inner'))


# #### [Do It! 실습] 인덱스가 다른 데이터 열 방향 연결하기

# In[24]:

    
df1x =df1c.copy()
df2x =df2c.copy()
df3x =df3c.copy()



df1x.index = [0, 1, 2, 3]
df2x.index = [4, 5, 6, 7]
df3x.index = [0, 2, 5, 7]
print(df1x)
print(df2x)
print(df3x)


# In[26]:


col_concat = pd.concat([df1x, df2x, df3x], axis="columns")
print(col_concat)


# In[27]:


print(pd.concat([df1, df3], axis="columns", join='inner'))


# ## 07-3 분할된 데이터 연결하기

# #### [Do It! 실습] 여러 개의 파일로 분할된 데이터 연 ,결하기

# In[28]:

from pathlib import Path

billboard_data_files = (
    Path(".")
    .glob("../data/billboard_by_week/billboard-*.csv")
)

billboard_data_files = sorted(list(billboard_data_files))
print(billboard_data_files)


# In[29]:


billboard_data_files = list(billboard_data_files)


# In[30]:


billboard01 = pd.read_csv(billboard_data_files[0])
billboard02 = pd.read_csv(billboard_data_files[1])
billboard03 = pd.read_csv(billboard_data_files[2])
print(billboard01)


# In[31]:


# 각 데이터프레임의 shape 확인
print(billboard01.shape)
print(billboard02.shape)
print(billboard03.shape)


# In[32]:


billboard = pd.concat([billboard01, billboard02, billboard03])
# 연결한 데이터프레임의 shape 확인
print(billboard.shape)


# In[33]:


assert (
    billboard01.shape[0]
    + billboard02.shape[0]
    + billboard03.shape[0]
    == billboard.shape[0]
)


# #### [Do It! 실습] 루프 구문으로 여러 개 파일 불러오기

# In[34]:


from pathlib import Path
billboard_data_files = (
    Path(".")
    .glob("../data/billboard_by_week/billboard-*.csv")
)

# 빈 리스트를 생성합니다.
list_billboard_df = []

# CSV 파일명 리스트를 순회합니다.
for csv_filename in billboard_data_files:
    # 필요하다면 아래 코드를 주석 해제하여 각 CSV 파일명을 출력하세요.
    # print(csv_filename)

    # CSV 파일을 데이터프레임으로 불러옵니다.
    df = pd.read_csv(csv_filename)

    # 데이터프레임을 리스트에 저장합니다.
    list_billboard_df.append(df)

# 데이터프레임의 개수를 출력합니다.
print(len(list_billboard_df))


# In[35]:


print(type(list_billboard_df[0]))


# In[36]:


print(list_billboard_df[0])


# In[37]:


billboard_loop_concat = pd.concat(list_billboard_df)
print(billboard_loop_concat.shape)


# #### [Do It! 실습] 리스트 컴프리헨션으로 여러 개 파일 불러오기

# In[38]:


billboard_data_files = (
    Path(".")
    .glob("../data/billboard-by_week/billboard-*.csv")
)

list_billboard_df = []
for csv_filename in billboard_data_files:
    df = pd.read_csv(csv_filename)
    list_billboard_df.append(df)

billboard_data_files = (
    Path(".")
    .glob("../data/billboard-by_week/billboard-*.csv")
)

billboard_dfs = [pd.read_csv(data) for data in billboard_data_files]


# In[39]:


print(type(billboard_dfs))


# In[40]:


print(len(billboard_dfs))


# In[41]:


billboard_concat_comp = pd.concat(billboard_dfs)
print(billboard_concat_comp)


# ## 07-4 여러 데이터셋 병합하기

# In[42]:


person = pd.read_csv('../data/survey_person.csv')
site = pd.read_csv('../data/survey_site.csv')
survey = pd.read_csv('../data/survey_survey.csv')
visited = pd.read_csv('../data/survey_visited.csv')
print(person)


# In[43]:


print(site)


# In[44]:


print(visited)


# In[45]:


print(survey)


# #### [Do It! 실습] 일대일 병합하기

# In[46]:


visited_subset = visited.loc[[0, 2, 6], :]
print(visited_subset)


# In[47]:


print(visited_subset["site"].value_counts())


# In[48]:


o2o_merge = site.merge(visited_subset, left_on="name", right_on="site")
print(o2o_merge)


# #### [Do It! 실습] 다대일 병합하기

# In[49]:


print(visited["site"].value_counts())


# In[50]:


m2o_merge = site.merge(visited, left_on='name', right_on='site')
print(m2o_merge)


# #### [Do It! 실습] 다대다 병합하기

# In[51]:


ps = person.merge(survey, left_on='ident', right_on='person')
vs = visited.merge(survey, left_on='ident', right_on='taken')
print(ps)

#%%

print(person["ident"].value_counts())
print(ps["ident"].value_counts())
print(survey["person"].value_counts())
# In[52]:


print(vs)


# In[53]:


print(ps["quant"].value_counts())


# In[54]:


print(vs["quant"].value_counts())


# In[55]:


ps_vs = ps.merge(
    vs,
    left_on=["quant"],
    right_on=["quant"],
)
ps_vs


# In[56]:


print(ps_vs.loc[0, :])


# #### [Do It! 실습] assert문으로 병합 결과 확인하기

# In[57]:


print(ps.shape)


# In[58]:


print(vs.shape)


# In[59]:


print(ps_vs.shape)


# In[60]:


assert vs.shape[0] == 21


# In[61]:


# assert ps_vs.shape[0] <= vs.shape[0]  # 오류


# ## 07-5 데이터 정규화하기

# #### [Do It! 실습] 표 분할하여 데이터 정규화하기

# In[62]:


import pandas as pd

billboard = pd.read_csv('../data/billboard.csv')

billboard_long = billboard.melt(
    id_vars=["year", "artist", "track", "time", "date.entered"],
    var_name="week",
    value_name="rating",
)

print(billboard_long)


# In[63]:


print(billboard_long.loc[billboard_long.track == 'Loser'])


# In[64]:


billboard_songs = billboard_long[
    ["year", "artist", "track", "time", "date.entered"]
]
print(billboard_songs.shape)


# In[65]:

# 중복 제거 : drop_duplicates()
billboard_songs = billboard_songs.drop_duplicates()
print(billboard_songs.shape)


# In[66]:

# 컬럼 추가 
# 인덱스 +1 : 인덱스보다 1씩 큰 값을 컬럼('id')로 지정
billboard_songs['id'] = billboard_songs.index + 1
print(billboard_songs)


# In[67]:


billboard_ratings = billboard_long.merge(
    billboard_songs, on=["year", "artist", "track", "time", "date.entered"]
)
print(billboard_ratings.shape)


# In[68]:


print(billboard_ratings)


# In[69]:


billboard_ratings = billboard_ratings[
    ["id", "week", "rating"]
]
print(billboard_ratings)


# In[ ]:




