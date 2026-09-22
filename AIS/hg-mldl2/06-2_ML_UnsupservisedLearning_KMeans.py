#!/usr/bin/env python
# coding: utf-8

# # k-평균
"""
데이터 로드 및 전처리: 과일 데이터 다운로드, 넘파이 로드 및 k-평균 입력을 위한 2차원 배열 펼침(reshape)
KMeans 모델 학습 및 군집 결과 확인: KMeans(n_clusters=3) 모델 훈련, 클러스터 레이블(labels_) 및 군집별 샘플 개수 확인
이미지 시각화 유틸리티 함수: draw_fruits 함수 및 내부 동작
군집별 이미지 출력: 각 레이블(0, 1, 2)별 과일 이미지 시각화
클러스터 중심 및 샘플 분석: 클러스터 중심 이미지 시각화(cluster_centers_), 중심과의 거리 변환(transform), 예측(predict) 및 학습 반복 횟수(n_iter_)
최적의 k 탐색 (엘보우 방법): 클러스터 수(2~6)에 따른 이너셔(inertia_) 값 계산 및 그래프 시각화
"""


# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/06-2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# ## KMeans 클래스

# In[1]:

# 과일 300개 넘파이 데이터셋(.npy)을 다운로드함
# get_ipython().system('wget https://bit.ly/fruits_300_data -O fruits_300.npy')


# In[2]:

import numpy as np

# 넘파이 배열 파일(.npy)에서 과일 데이터를 로드함
fruits = np.load('fruits_300.npy')
# k-평균 모델에 입력하기 위해 3차원 데이터(300, 100, 100)를 2차원 배열(300, 10000)로 펼침
fruits_2d = fruits.reshape(-1, 100*100)


# In[3]:

from sklearn.cluster import KMeans

# 클러스터 개수를 3개로 지정하고 k-평균 모델을 생성한 후 훈련함
km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_2d)


# In[4]:

# 각 샘플에 할당된 군집 레이블(0, 1, 2)을 확인함
print('총 갯수:', len(km.labels_)) # 300개
print(km.labels_)


# In[5]:

# 각 클러스터(0, 1, 2)에 배정된 샘플 개수를 확인함
print(np.unique(km.labels_, return_counts=True))

# 파인애플(0), 바나나(1), 사과(2)
# (array([0, 1, 2], dtype=int32), array([112,  98,  90]))

# In[6]:

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


# In[7]:

# 파인애플    
# 레이블이 0인 클러스터의 과일 이미지들을 시각화함
draw_fruits(fruits[km.labels_==0])


# In[8]:

# 바나나    
# 레이블이 1인 클러스터의 과일 이미지들을 시각화함
draw_fruits(fruits[km.labels_==1])


# In[9]:

# 레이블이 2인 클러스터의 과일 이미지들을 시각화함
draw_fruits(fruits[km.labels_==2])


# ## 클러스터 중심

# In[10]:

# 각 클러스터 중심(center)의 픽셀값을 100x100 크기로 변환하여 대표 이미지로 시각화함
draw_fruits(km.cluster_centers_.reshape(-1, 100, 100), ratio=3)


# In[11]:

# 100번째 샘플(인덱스 100)에서 각 클러스터 중심까지의 거리를 변환하여 확인함
print(km.transform(fruits_2d[100:101]))


# In[12]:

# 100번째 샘플이 속하는 클러스터 레이블을 예측함
print(km.predict(fruits_2d[100:101])) # [0] 파일애플


# In[13]:

# 100번째 샘플의 실제 이미지를 출력하여 확인해 봄
draw_fruits(fruits[100:101]) # 파인애플


# In[14]:

# 알고리즘이 클러스터 중심을 최적화하기 위해 반복(반복 학습)한 횟수를 출력함
print(km.n_iter_) # 4


# ## 최적의 k 찾기

# In[15]:

# 클러스터 개수(k)를 2부터 6까지 변경하면서 이너셔(inertia) 값을 기록함
inertia = []
for k in range(2, 7):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(fruits_2d)
    inertia.append(km.inertia_)

# k 값에 따른 이너셔 변화를 선 그래프로 그려 엘보우(Elbow) 지점을 확인함
plt.plot(range(2, 7), inertia)
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()

# 결과: 3의 지점에서 미세하게 꺾임




