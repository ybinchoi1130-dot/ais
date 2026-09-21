#!/usr/bin/env python
# coding: utf-8

# # 선형 회귀(LinearRegression)
# ## - 선형회귀, 다항회귀


# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/03-2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# k-최근접 이웃 회귀(KNeighborsRegressor)의 한계
#   - k-최근접 이웃 알고리즘을 사용해 가장 가까운 이웃의 샘플을 찾고
#     이 샘플들의 타깃값을 평균하여 값을 예측한다.
#   - 예측 데이터가 훈련 데이터의 범위에 있으면 예측을 잘 한다.
#     그러나 범위를 벗어나면 이웃의 평균으로 예측하는 문제가 있다.

# In[1]:


import numpy as np

# 농어의 길이: 훈련
perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )

# 농어의 무게: 타깃
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )


# In[2]:


from sklearn.model_selection import train_test_split

# 훈련 세트와 테스트 세트로 나눕니다
train_input, test_input, train_target, test_target = train_test_split(
    perch_length, # 훈련 데이터
    perch_weight, # 정답 데이터
    random_state=42)

# 2차원 배열로 변환
# 훈련 세트와 테스트 세트를 2차원 배열로 바꿉니다
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)


# In[3]:

# k-최근접 이웃 회귀(KNeighborsRegressor)
from sklearn.neighbors import KNeighborsRegressor

# 이웃의 갯수 3개
knr = KNeighborsRegressor(n_neighbors=3)

# k-최근접 이웃 회귀 모델을 훈련합니다
knr.fit(train_input, train_target)


# In[4]:

# 농어 무게 50g으로 예측
perch = [50]

# 예측:  [1033.33333333]
perch_predict = knr.predict([perch])
print(perch_predict) # [1033.33333333]


# In[5]:

import matplotlib.pyplot as plt

# In[6]:


# 50cm 농어의 이웃을 구합니다
distances, indexes = knr.kneighbors([perch])

# 훈련 세트의 산점도를 그립니다
plt.scatter(train_input, train_target)

# 훈련 세트 중에서 이웃 샘플만 다시 그립니다
plt.scatter(train_input[indexes], 
            train_target[indexes], marker='D')

# 50cm 농어 데이터
plt.scatter(perch,         # 농어의 길이(50cm)
            perch_predict, # 예측된 무게(1033g)
            marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[7]:

# 훈련 세트 중에서 예측된 이웃 샘플 3개의 평균
print(np.mean(train_target[indexes])) # 1033.3333333333333


# In[8]:

# 농어의 길이 100cm의 무게를 예측: [1033.33333333]
perch_100cm_predict = knr.predict([[100]])
print(knr.predict([perch_100cm_predict])) # 1033g


# In[9]:

# 농어의 길이 100cm의 무게를 예측: [1033.33333333]
perch_100cm = [100]

# 100cm 농어의 이웃을 구합니다
distances, indexes = knr.kneighbors([perch_100cm])

# 훈련 세트의 산점도를 그립니다
plt.scatter(train_input, train_target)
# 훈련 세트 중에서 이웃 샘플만 다시 그립니다
plt.scatter(train_input[indexes], train_target[indexes], marker='D')
# 100cm 농어 데이터
plt.scatter(perch_100cm, perch_100cm_predict, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

#%%

# THE END

