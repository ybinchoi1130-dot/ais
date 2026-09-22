#!/usr/bin/env python
# coding: utf-8

# # 데이터 전처리

# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/02-2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# ## 넘파이로 데이터 준비하기

# In[1]:


fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]


# In[2]:


import numpy as np


# In[3]:

np.column_stack(([1,2,3], [4,5,6]))

#%%

"""
array([[1, 4],
       [2, 5],
       [3, 6]])
"""


# In[4]:


fish_data = np.column_stack((fish_length, fish_weight))


# In[5]:


print(fish_data[:5])


# In[6]:

# 넘파이 배열(5개)을 생성 후 생성된 배열의 값을 1로 채움
print(np.ones(5))  # [1. 1. 1. 1. 1.]

# 넘파이 배열(5개)을 생성 후 생성된 배열의 값을 0로 채움
print(np.zeros(5)) # [0. 0. 0. 0. 0.]


# In[7]:

# 넘파이 배열 도미 35개(1), 빙어 14개(0) -> 총 49개 배열 생성
# 정답(타겟) 데이터
fish_target = np.concatenate((np.ones(35), np.zeros(14)))

# In[8]:

print(fish_target)

#%%

# ## 사이킷런으로 훈련 세트와 테스트 세트 나누기

# In[9]:


from sklearn.model_selection import train_test_split


# In[10]:

# 훈련데이터, 테스트데이터, 훈련데이터정답, 테스트데이터정답 
# 함수: train_test_split(전체데이터, 정답데이터)
# 비율: 훈련(0.75, 75%) : 테스트(0.25, 25%)
# 섞음: random_state=42
train_input, test_input, train_target, test_target = train_test_split(
    fish_data, fish_target, random_state=42)


# In[11]:

# 비율: 0.734: 0.265
# 훈련데이터, 테스트데이터
print(train_input.shape, test_input.shape) # (36, 2) (13, 2)


# In[12]:

# 훈련데이터 정답, 테스트데이터 정답: 
print(train_target.shape, test_target.shape) # (36,) (13,)


# In[13]:

# 전체 데이터    
# 넘파이 배열 도미 35개(1), 빙어 14개(0) -> 총 49개 배열 생성
# 도미(70%): 빙어(30%)

print(test_target)
# 테스트 데이터
# 도미(76%): 빙어(23%)
# [1. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

# In[14]:

# stratify=fish_target: 층화추출(Stratified Sampling)
# 타깃 데이터(fish_target)의 클래스 비율(도미와 빙어)에 맞춰서
# 훈련 세트와 테스트 세트를 분할
train_input, test_input, train_target, test_target = train_test_split(
    fish_data, fish_target, stratify=fish_target, random_state=42)


# In[15]:

# 원래비율: 도미(35개, 2.5): 빙어(14개, 1)
# 갯수: 13개 = 도미(9) : 빙어(4)
# 비율: 도미(70%) : 빙어(30%)
print(test_target) # [0. 0. 1. 0. 1. 0. 1. 1. 1. 1. 1. 1. 1.]


#%%

# ## 수상한 도미 한마리

# In[16]:


from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
kn.score(test_input, test_target)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 


# In[17]:

# 수상한 도미 한마리
bream = [25,150]

print("수상한 도미 한마리:", end='')
print(kn.predict([bream])) # [0.] 빙어?


# In[18]:

import matplotlib.pyplot as plt


# In[19]:


plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(bream[0], bream[1], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[20]:

# kneighbors() : 주어진 샘플에서 가장 가까운 k개(기본값 5개)의 이웃 정보를 반환
# distances: 가장 가까운 이웃 k(5개)까지의 직선 거리(유클리디안 거리) 배열
# indexes: 훈련 세트(train_input)에서 해당 이웃들의 인덱스(위치 번호) 배열
distances, indexes = kn.kneighbors([bream])

print(distances)  # [[ 92.00086956 130.48375378 130.73859415 138.32150953 138.39320793]]
print(indexes)    # [[21 33 19 30  1]]


# In[21]:

plt.scatter(train_input[:,0], train_input[:,1])  # 훈련 세트 전체 (동그라미)
plt.scatter(bream[0], bream[1], marker='^')      # 새로운 샘플 (삼각형 ^)
plt.scatter(train_input[indexes,0], # 길이
            train_input[indexes,1], # 무게
            marker='D')             # 가장 가까운 이웃 5개 (다이아몬드 D)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[22]:


print(train_input[indexes]) # 5개 이웃의 특성값(길이, 무게)


# In[23]:


print(train_target[indexes]) # 5개 이웃의 정답 레이블 (도미: 1, 빙어: 0)
# [[1. 0. 0. 0. 0.]]

# In[24]:

print(distances)
# [[ 92.00086956 130.48375378 130.73859415 138.32150953 138.39320793]]

#%%

# ## 기준을 맞춰라
# 특성값(길이, 무게)의 기준을 동일하게 맞춤

# In[25]:

plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(bream[0], bream[1], marker='^')
plt.scatter(train_input[indexes,0], train_input[indexes,1], marker='D')
plt.xlim((0, 1000))  # x 축의 범위를 y축과 같이 1000으로 맞춤
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[26]:

# 평균과 표준편차 
# 각 특성(길이와 무게)별로 데이터가 평균에서 
# 얼마나 떨어져 있는지 확인하기 위해 평균과 표준편차를 구함
# axis=0: 행(샘플) 방향을 따라 계산하여, 
# 각 열(특성 0: 길이, 특성 1: 무게)마다 각각 평균 1개, 
# 표준편차 1개씩 총 2개의 값이 들어있는 1차원 배열이 생성
mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis=0)


# In[27]:

# 특성: 길이, 무게
print('특성의 평균:', mean)    # [ 27.29722222 454.09722222]
print('특성의 표준편차:', std) # [  9.98244253 323.29893931]

# In[28]:

# 편차(Deviation): 데이터 - 평균
# 분산(Variance) : 편차의 제곱합의 평균
# 표준편차(Standard Deviation): 분산의 제곱근(루트)

# 표준점수(Z-score): 표준점수 = (데이터 - 평균) / 표준편차
# 원본 데이터에서 평균을 빼고 표준편차로 나누어, 
# 평균이 0이고 표준편차가 1인 정규분포 형태로 변환
# 넘파이 브로드캐스팅(Broadcasting): 
# train_input의 모든 행에 대해 mean을 빼고 
# std로 나눠주는 연산이 한 줄로 자동 수행
# 길이와 무게 모두 단위가 사라지고 동일한 
# 기준(-2 ~ +2 사이 등)으로 평가되므로 거리가 왜곡되지 않음
train_scaled = (train_input - mean) / std

#%%

# ## 전처리 데이터로 모델 훈련하기

# In[29]:

plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(bream[0], bream[1], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[30]:

# 표준점수(Z-score)로 변환
bream_scaled = (bream - mean) / std


# In[31]:

# 스케일된 수상한 도미 데이터
plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(bream_scaled[0], bream_scaled[1], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[32]:

kn.fit(train_scaled, train_target)


# In[33]:

# 스케일 변환: 테스트(평가) 데이터
test_scaled = (test_input - mean) / std


# In[34]:

kn.score(test_scaled, test_target) # 1.0

# In[35]:

# 수상한 도미 데이터: 정상
print(kn.predict([bream_scaled])) # [1.]


# In[36]:

distances, indexes = kn.kneighbors([bream_scaled])


# In[37]:

# 수상한 도미 데이터의 이웃(5개)이 모두 도미로 선택 됨
plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(bream_scaled[0], bream_scaled[1], marker='^')
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

