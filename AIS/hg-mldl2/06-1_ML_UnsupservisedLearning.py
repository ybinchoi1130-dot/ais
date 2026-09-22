#!/usr/bin/env python
# coding: utf-8


#%%

"""
비지도 학습(Unsupervised Learning)
- 입력 데이터만 제공되고 타겟 데이터는 제공되지 않는 머신러닝 방식
- 대표적인 비지도 학습은 군집 알고리즘(Clustering)과 차원 축소(Dimensionality Reduction)

"""


#%%
# # 군집 알고리즘
"""
데이터 다운로드 및 로드: .npy 데이터셋 다운로드 및 로드 과정
데이터 형태 및 픽셀 탐색: 배열 크기 확인 및 특정 픽셀값 출력 과정
이미지 시각화: gray 및 gray_r 반전 컬러맵을 이용한 흑백 출력 및 서브플롯 비교
픽셀 통계 분석: 2차원 이미지의 1차원 펼침(reshape), 샘플별/픽셀별 평균값 계산 및 히스토그램·막대그래프 시각화
평균값 기반 유사 사진 탐색: 평균 이미지 생성, 오차 계산(abs_diff), 가장 유사한 100개 샘플 정렬 및 10×10 격자 출력
"""

# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/06-1.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# ## 과일 사진 데이터 준비하기

# In[1]:

# 과일 300개 넘파이 데이터셋(.npy)을 다운로드함
# get_ipython().system('wget https://bit.ly/fruits_300_data -O fruits_300.npy')


#%%

import os
from urllib.request import urlretrieve

# 파일이 없을 경우에만 다운로드하여 로컬에 저장함
if not os.path.exists('fruits_300.npy'):
    urlretrieve('https://bit.ly/fruits_300_data', 'fruits_300.npy')

# In[2]:

# 데이터 처리 및 시각화에 필요한 넘파이와 맷플롯립 라이브러리를 불러옴
import numpy as np
import matplotlib.pyplot as plt


# In[3]:

# 넘파이 배열 파일(.npy)에서 과일 데이터를 로드함
fruits = np.load('fruits_300.npy')


# In[4]:

# 데이터셋의 형태(샘플 수, 행, 열)를 확인함 (300, 100, 100)
print(fruits.shape)


# In[5]:

# 첫 번째 샘플(사과)의 첫 번째 행 픽셀 값(100개)을 출력함
print(fruits[0, 0, :])


# In[6]:

# 첫 번째 사진(사과)을 흑백(gray) 이미지로 출력함
plt.imshow(fruits[0], cmap='gray')
plt.show()


# In[7]:

# 반전된 흑백(gray_r) 색상 맵을 사용하여 배경을 밝게 출력함
plt.imshow(fruits[0], cmap='gray_r')
plt.show()


# In[8]:

# 파인애플(인덱스 100)과 바나나(인덱스 200) 사진을 나란히 시각화함
fig, axs = plt.subplots(1, 2)
axs[0].imshow(fruits[100], cmap='gray_r')
axs[1].imshow(fruits[200], cmap='gray_r')
plt.show()


# ## 픽셀 값 분석하기

# In[9]:

# 사과, 파인애플, 바나나 데이터를 각각 100개씩 슬라이싱하고 100x100 크기를 10,000개 길이의 1차원 배열로 펼침
apple = fruits[0:100].reshape(-1, 100*100)
pineapple = fruits[100:200].reshape(-1, 100*100)
banana = fruits[200:300].reshape(-1, 100*100)


# In[10]:

# 1차원으로 펼친 사과 데이터의 형태를 확인함 (100, 10000)
print(apple.shape)


# In[11]:

# 각 사과 사진 샘플별로 10,000개 픽셀의 평균값을 계산함 (샘플당 평균값 100개)
print(apple.mean(axis=1))


# In[12]:

# 세 과일의 사진별 픽셀 평균값 분포를 히스토그램으로 비교함
plt.hist(apple.mean(axis=1), alpha=0.8, label='apple')
plt.hist(pineapple.mean(axis=1), alpha=0.8, label='pineapple')
plt.hist(banana.mean(axis=1), alpha=0.8, label='banana')
plt.legend()
plt.show()


# In[13]:

# 픽셀 위치별(10,000개 픽셀) 평균값을 계산하여 막대그래프로 나타냄
fig, axs = plt.subplots(1, 3, figsize=(20, 5))
axs[0].bar(range(10000), apple.mean(axis=0))
axs[1].bar(range(10000), pineapple.mean(axis=0))
axs[2].bar(range(10000), banana.mean(axis=0))
plt.show()


# In[14]:

# 픽셀별 평균값을 원래 100x100 2차원 배열 형태로 복원함
apple_mean = apple.mean(axis=0).reshape(100, 100)
pineapple_mean = pineapple.mean(axis=0).reshape(100, 100)
banana_mean = banana.mean(axis=0).reshape(100, 100)

# 각 과일의 평균 이미지를 흑백으로 시각화함
fig, axs = plt.subplots(1, 3, figsize=(20, 5))
axs[0].imshow(apple_mean, cmap='gray_r')
axs[1].imshow(pineapple_mean, cmap='gray_r')
axs[2].imshow(banana_mean, cmap='gray_r')
plt.show()


# ## 평균값과 가까운 사진 고르기

# In[15]:

# 전체 과일 사진과 사과 평균 이미지 간의 절대값 오차를 구함
abs_diff = np.abs(fruits - apple_mean)
# 사진마다 픽셀 오차의 평균을 계산함
abs_mean = np.mean(abs_diff, axis=(1,2))
print(abs_mean.shape)


# In[16]:

# 사과 평균과 오차가 가장 작은 사진 100개의 인덱스를 정렬하여 추출함
apple_index = np.argsort(abs_mean)[:100]
# 10x10 형태로 인덱스 배열을 변경함
apple_index = apple_index.reshape(10, 10)
# 오차가 가장 작은 100장의 사진을 10x10 격자로 시각화함
fig, axs = plt.subplots(10, 10, figsize=(10,10))
for i in range(10):
    for j in range(10):
        axs[i, j].imshow(fruits[apple_index[i, j]], cmap='gray_r')
        axs[i, j].axis('off')
plt.show()


# ## 확인문제

# In[17]:

# 전체 과일 사진과 바나나 평균 이미지 간의 절대값 오차 및 샘플별 오차 평균을 계산함
abs_diff = np.abs(fruits - banana_mean)
abs_mean = np.mean(abs_diff, axis=(1,2))

# 바나나 평균과 오차가 가장 작은 사진 100개의 인덱스를 추출하고 10x10 배열로 변환함
banana_index = np.argsort(abs_mean)[:100]
banana_index = banana_index.reshape(10, 10)
# 바나나 평균과 가장 가까운 100장의 사진을 10x10 격자로 시각화함
fig, axs = plt.subplots(10, 10, figsize=(10,10))
for i in range(10):
    for j in range(10):
        axs[i, j].imshow(fruits[banana_index[i, j]], cmap='gray_r')
        axs[i, j].axis('off')
plt.show()

#%%

# 결과:
# 맨 마지막 2개가 바나나가 아닌 사과가 선택
