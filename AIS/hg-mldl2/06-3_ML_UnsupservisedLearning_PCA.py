#!/usr/bin/env python
# coding: utf-8

# # 주성분 분석
"""
데이터 로드 및 2차원 변환: 과일 넘파이 데이터 다운로드, 로드 및 2차원 배열(reshape) 변환 
PCA 모델 학습 및 주성분 추출: PCA(n_components=50) 모델 생성 및 주성분(components_) 시각화
차원 축소 및 데이터 복원: 주성분 변환(transform), 역변환(inverse_transform)을 통한 원본 복원 및 이미지 손실도 확인
설명된 분산 비율 분석: 총 분산 비율 합계 및 explained_variance_ratio_ 그래프 시각화
지도학습 분류 모델과의 결합: 로지스틱 회귀(Logistic Regression) 교차 검증을 통해 원본 특성(10,000개)과 축소 특성(50개) 간의 정확도 및 학습 시간 비교
설명 분산 기준 PCA(50%) 및 군집 분석: 분산 비율 기반 PCA 설정, 주성분 개수 확인 및 차원 축소 데이터에 대한 KMeans 군집화 및 2차원 산점도 시각화
"""



# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/06-3.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# ## PCA 클래스

# In[1]:

# 과일 300개 넘파이 데이터셋(.npy)을 다운로드함
# get_ipython().system('wget https://bit.ly/fruits_300_data -O fruits_300.npy')


# In[2]:

import numpy as np

# 넘파이 배열 파일(.npy)에서 과일 데이터를 로드함
fruits = np.load('fruits_300.npy')
# PCA 모델에 적용하기 위해 3차원 데이터(300, 100, 100)를 2차원 배열(300, 10000)로 펼침
fruits_2d = fruits.reshape(-1, 100*100)


# In[3]:

from sklearn.decomposition import PCA

# 50개의 주성분을 추출하는 PCA 모델을 생성하고 훈련함
pca = PCA(n_components=50)
pca.fit(fruits_2d)


# In[4]:

# 추출된 주성분(components_)의 형태를 확인함 
# 50개 주성분, 각 10000개 픽셀 특성
print(pca.components_.shape) # (50, 10000)


# In[5]:

import matplotlib.pyplot as plt

# 과일 이미지 배열을 받아 격자 형태로 시각화하는 함수를 정의함
def draw_fruits(arr, ratio=1):
    n = len(arr)    # n은 샘플 개수를 나타냄
    # 한 줄에 10개씩 이미지를 그리기 위해 전체 행 개수를 계산함
    rows = int(np.ceil(n/10))
    # 행이 1개이면 열 개수는 샘플 개수가 되고, 그렇지 않으면 10개로 설정함
    cols = n if rows < 2 else 10
    fig, axs = plt.subplots(rows, cols,
                            figsize=(cols*ratio, rows*ratio), squeeze=False)
    for i in range(rows):
        for j in range(cols):
            if i*10 + j < n:    # 샘플 개수(n)까지만 이미지를 출력함
                axs[i, j].imshow(arr[i*10 + j], cmap='gray_r')
            axs[i, j].axis('off')
    plt.show()


# In[6]:

# 50개 주성분을 100x100 크기로 변환하여 
# 주성분이 학습한 대표 이미지 패턴을 시각화함
draw_fruits(pca.components_.reshape(-1, 100, 100))


# In[7]:

# 원본 2차원 데이터의 형태를 확인함 (300, 10000)
print(fruits_2d.shape) # (300, 10000)


# In[8]:

# 학습된 PCA(pca) 모델을 이용해서
# 10000개의 특성을 가진 고차원 데이터를 50개의
# 핵심 주성분으로 압축(차원 축소)
# 원본 데이터를 50개의 주성분 공간으로 투영하여 차원을 축소함
fruits_pca = pca.transform(fruits_2d)


# In[9]:

# 10000(100 * 100) -> 50개의 새로운 주성분 축으로 직교 투영(새로운 좌표계로 변환)   
# 50개 차원으로 축소된 데이터의 형태를 확인함 (300, 50)
# 감소율: 99.5%
print(fruits_pca.shape) # (300, 50)


# ## 원본 데이터 재구성

# In[10]:

# 50개로 축소된 주성분 데이터를 원래의 10,000개 특성으로 복원하고 형태를 확인함
fruits_inverse = pca.inverse_transform(fruits_pca)
print(fruits_inverse.shape) # (300, 10000)


# In[11]:

# 복원된 데이터를 100x100 크기의 3차원 이미지 배열로 변환함
fruits_reconstruct = fruits_inverse.reshape(-1, 100, 100)


# In[12]:

# 복원된 사과, 파인애플, 바나나 이미지를 각각 100개씩 출력하여 손실 정도를 확인함
for start in [0, 100, 200]:
    draw_fruits(fruits_reconstruct[start:start+100])
    print("\n")


# ## 설명된 분산

# In[13]:

# 설명된 분산
# 각 주성분이 원본 데이터가 가지고 있던 전체 정보량 중 몇 퍼센트(%)를
# 보존하고 있는가?
# 50개 주성분이 원본 데이터의 분산을 설명하는 총 비율의 합을 출력함
# 보존율: 약 0.9215(92.15%)
# 손실율: 7.85%
print(np.sum(pca.explained_variance_ratio_)) # 0.9215145953326257


# In[14]:

# 분석 및 평가    
# 뒤쪽 주성분으로 갈수록 설명된 분산 비율이 급격히 0에 수렴
# 50개 이후의 주성분들은 과일 분류에 큰 영향을 주지 않는 
# 미세한 노이즈나 세부 질감에 불과
    
# 주성분별 설명된 분산 비율의 변화를 선 그래프로 시각화함
plt.plot(pca.explained_variance_ratio_)
plt.show()


# ## 다른 알고리즘과 함께 사용하기

# In[15]:

from sklearn.linear_model import LogisticRegression

# 분류를 위한 로지스틱 회귀 모델을 생성함
lr = LogisticRegression()


# In[16]:

# 사과(0), 파인애플(1), 바나나(2)를 나타내는 정답 타깃 레이블(0, 1, 2)을 생성함
target = np.array([0] * 100 + [1] * 100 + [2] * 100)


# In[17]:

from sklearn.model_selection import cross_validate

# 원본 데이터(10,000개 특성)로 교차 검증을 수행하여 
# 평균 정확도 점수와 훈련 시간을 확인함
# 평균 훈련 시간: 약 0.211초
scores = cross_validate(lr, fruits_2d, target)
print(np.mean(scores['test_score'])) # 0.9966666666666667
print(np.mean(scores['fit_time']))   # 0.21064352989196777


# In[18]:

# 50개로 차원 축소된 데이터로 교차 검증을 수행하여 
# 점수와 훈련 시간을 원본과 비교함
# 평균 훈련 시간: 약 0.011초
scores = cross_validate(lr, fruits_pca, target)
print(np.mean(scores['test_score'])) # 0.9966666666666667
print(np.mean(scores['fit_time']))   # 0.011246442794799805

# 결과: 훈련시간이 19배 단축(94.7%)


# In[19]:

# 설명된 분산 비율이 50%(0.5)에 도달할 때까지 
# 주성분을 자동으로 찾도록 PCA 모델을 설정하고 훈련함
pca = PCA(n_components=0.5)
pca.fit(fruits_2d)


# In[20]:

# 분산 50%를 설명하기 위해 선택된 주성분 개수를 확인함
print(pca.n_components_) # 2개


# In[21]:

# 분산 50%에 해당하는 주성분으로 원본 데이터를 변환하고 형태를 확인함
fruits_pca = pca.transform(fruits_2d)
print(fruits_pca.shape) # (300, 2)


# In[22]:

# 분산 50% 주성분 데이터로 로지스틱 회귀 모델의 교차 검증을 수행함
scores = cross_validate(lr, fruits_pca, target)
print(np.mean(scores['test_score'])) # 0.9933333333333334
print(np.mean(scores['fit_time']))   # 0.030715560913085936


# In[23]:

from sklearn.cluster import KMeans

# 차원이 축소된 데이터에 대해 3개 클러스터를 찾는 k-평균 모델을 훈련함
km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_pca)


# In[24]:

# 군집화 결과 각 클러스터에 배정된 샘플 개수를 확인함
print(np.unique(km.labels_, return_counts=True))

# (array([0, 1, 2], dtype=int32), array([110,  99,  91]))

# In[25]:

# 군집화된 각 레이블(0, 1, 2)별로 해당하는 실제 과일 이미지를 출력함
for label in range(0, 3):
    draw_fruits(fruits[km.labels_ == label])
    print("\n")


# In[26]:

# 2개의 주요 주성분을 x, y축으로 하여 각 군집의 분포를
# 2차원 산점도로 시각화함
for label in range(0, 3):
    data = fruits_pca[km.labels_ == label]
    plt.scatter(data[:,0], data[:,1])
plt.legend(['apple', 'banana', 'pineapple'])
plt.show()

