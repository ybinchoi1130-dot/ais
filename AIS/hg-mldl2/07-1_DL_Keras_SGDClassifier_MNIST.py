#!/usr/bin/env python
# coding: utf-8

# # 인공 신경망

# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/07-1.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# In[1]:

# pip install tensorflow==2.18.0    
# 결과: Keras 3.15.1

# 실행마다 동일한 결과를 얻기 위해 케라스에 랜덤 시드를 사용하고 텐서플로 연산을 결정적으로 만듭니다.
import keras
import tensorflow as tf

# 케라스에 지정된 백엔드: tensorflow
print("# 케라스에 지정된 백엔드:", keras.config.backend())

#%%

# 실행할 때마다 항상 동일한 결과를 얻기 위한 재현성 보장
# 난수 생성기 고정
keras.utils.set_random_seed(42)

"""
역할: 텐서플로(TensorFlow) 내부의 모든 연산을 
'결정론적(Deterministic)'으로 실행하도록 강제합니다.

배경:
GPU나 멀티스레드 환경에서는 속도 최적화를 위해 비동기/병렬 처리를 수행하는데, 
이 과정에서 덧셈이나 곱셈 등의 연산 순서가 미세하게 뒤바뀌어 
랜덤 시드를 고정해도 실행할 때마다 결과값(손실, 가중치)이 조금씩 달라지는 문제가 발생합니다.
이 함수를 활성화하면 연산 순서와 방식을 엄격히 통제하여 
동일한 하드웨어에서 항상 비트 단위로 동일한 연산 결과를 내도록 보장합니다.
"""
tf.config.experimental.enable_op_determinism()


#%%
# ## 패션 MNIST

# In[2]:

import keras

# 전체 데이터: 70,000개(70000, 28, 28)
# 비율: 85.7: 14.3
# 샘플 데이터셋에서 패션 데이터를 로드하고 훈련 데이터와, 테스트 데이터로 분할
(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()


# In[3]:

# (60000, 28, 28) (60000,)
print(train_input.shape, train_target.shape) 


# In[4]:

# (10000, 28, 28) (10000,)
print(test_input.shape, test_target.shape)


# In[5]:

# 훈련 데이터 셋의 10개 샘플 출력
# 훈련용 이미지: 검은색(0) 바탕에 흰색(255) 이미지
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 10, figsize=(10,10))
for i in range(10):
    axs[i].imshow(train_input[i], cmap='gray_r') # 반전: 흰색 배경
    axs[i].axis('off')
plt.show()


# In[6]:

# 정답    
item_targets = [
'티셔츠', '바지', '스웨터', '드레스', '코드',
'샌달', '셔츠', '스니커즈', '가방', '앵클부츠'
]

for n, item in enumerate(item_targets):
    print(f"[{n}] {item}")
    
#%%

"""
[0] 티셔츠
[1] 바지
[2] 스웨터
[3] 드레스
[4] 코드
[5] 샌달
[6] 셔츠
[7] 스니커즈
[8] 가방
[9] 앵클부츠
"""    
    
#%%

# [9 0 0 3 0 2 7 2 5 5]
print(train_target[:10])


# In[7]:


import numpy as np

# 각 정답은 6000개 * 10 = 총 60,000개
print(np.unique(train_target, return_counts=True))
# (array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint8), 
#  array([6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000]))

#%%

# ## 로지스틱 회귀로 패션 아이템 분류하기

# In[8]:

# 스케일
# 이미지가 0부터 255까지의 값이므로 255로 나누어
# 0~1 사이의 값으로 정규화
train_scaled = train_input / 255.0

# 2차원으로 변환
train_scaled = train_scaled.reshape(-1, 28*28)


# In[9]:

print(train_input.shape) # (60000, 28, 28)

# 60000 = 784(28 * 28)
print(train_scaled.shape) # (60000, 784)


# In[10]:

# 머신러닝: 확률적 경사 하강 모델로 교차 검증을 하여 성능확인
from sklearn.model_selection import cross_validate
from sklearn.linear_model import SGDClassifier

sc = SGDClassifier(loss='log_loss', max_iter=5, random_state=42)
scores = cross_validate(sc, train_scaled, train_target, n_jobs=-1)
print(np.mean(scores['test_score'])) # 0.81945

#%%

sc = SGDClassifier(loss='log_loss', max_iter=10, random_state=42)
scores = cross_validate(sc, train_scaled, train_target, n_jobs=-1)
print(np.mean(scores['test_score'])) # 0.83115

#%%

sc = SGDClassifier(loss='log_loss', max_iter=20, random_state=42)
scores = cross_validate(sc, train_scaled, train_target, n_jobs=-1)
print(np.mean(scores['test_score'])) # 0.84375

#%%

sc = SGDClassifier(loss='log_loss', max_iter=200, random_state=42)
scores = cross_validate(sc, train_scaled, train_target, n_jobs=-1)
print(np.mean(scores['test_score'])) # 0.8415833333333333


#%%
# ## 인공신경망

# ### 텐서플로와 케라스

# In[11]:


import tensorflow as tf


# In[12]:


import keras


# In[13]:


keras.config.backend()


# In[14]:


# import os
# os.environ["KERAS_BACKEND"] = "torch"   # 또는 "jax"


# ## 인공신경망으로 모델 만들기

# In[15]:


from sklearn.model_selection import train_test_split

# 스케일된 훈련 데이터(60,000건)로 훈련(80%), 검증용(20%으로 분할
train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)


# In[16]:

# (48000, 784) (48000,)
print(train_scaled.shape, train_target.shape)


# In[17]:

# (12000, 784) (12000,)
print(val_scaled.shape, val_target.shape)


# In[18]:

# 입력층: 784개
inputs = keras.layers.Input(shape=(784,))


# In[19]:

# 밀집층: 뉴런(10개)
# 정답의 갯수가 10개이므로 뉴런의 갯수를 10개 맞춤
# 활성함수: 소프트맥스('softmax')
# 소프트맥스: 출력값을 0~1 사이로 합축하고 
#             전체 합이 1이 되도록 하기 위한 정규화된 지수함수
dense = keras.layers.Dense(10, activation='softmax')


# In[20]:

# 신경망 모델 만듦
# 입력층과 밀집층을 리스트 묶어서 Sequential에 전달
model = keras.Sequential([inputs, dense])


# ## 인공신경망으로 패션 아이템 분류하기

# In[21]:

# 손실함수: 'sparse_categorical_crossentropy' 다중분류
# 타깃값을 원-핫 인코딩(One-Hot-Encoding)을 하지 않고 그냥 사용 할 때
# 정확도출력: metrics=['accuracy'] 훈력 할 때마다 정확도를 출력
# 옵티마이저: optimizer='rmsprop' 기본값, RMSprop
# RMSprop: 적응적 학습률. 동일한 보폭을 정하지 않고 스스로 조절, SGD보다 빠르고 안정적
model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# In[22]:

# [7 3 5 8 6 9 3 3 9 9]
print(train_target[:10])


# In[23]:

# 훈련
# 에포크(epochs): 반복횟수 5회
model.fit(train_scaled, train_target, epochs=5)

#%%

# 전체 훈련 데이터(train_scaled): 48,000건
# 케라스의 미니배치 크기: 기본값(32). 한 번의 가중치 업데이트 단위
# 총 스텝 수: 48,000 = 1500스텝 * 배치크기(32)
# 데이터를 32개씩 묶어서 1,500번에 나누어 학습(가중치 업데이트)을 진행
"""
Epoch 1/5
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 3s 1ms/step - accuracy: 0.7925 - loss: 0.6082     
Epoch 2/5
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 2s 1ms/step - accuracy: 0.8378 - loss: 0.4744  
Epoch 3/5
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 2s 1ms/step - accuracy: 0.8467 - loss: 0.4501  
Epoch 4/5
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 2s 1ms/step - accuracy: 0.8513 - loss: 0.4372  
Epoch 5/5
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 2s 1ms/step - accuracy: 0.8536 - loss: 0.4290  
"""

# In[24]:

# 검증용 데이터 셋으로 평가
val_score = model.evaluate(val_scaled, val_target) # [0.4437466263771057, 0.8464999794960022]
print("평가 점수:", val_score)

#%%

# 결과: [손실값, 정확도]
# [0.4437466263771057, 0.8464999794960022]
# model.compile()에서 설정한 손실함수와 평가 지표 순서대로 출력
# model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# 손실값(Loss): 손실함수('sparse_categorical_crossentropy') 계산된 오차값
#               0에 가까울 수록 오차가 적고 모델이 정답을 확신을 갖고 맞췄음을 의미
# 정확도(Accuracy): 모델의 분류 정확도

# 평가:
#   - 훈련점수: 0.8536
#   - 평가점수: 0.8464
#   - 훈련 데이터와 검증 데이터 성능 차이가 크지 않다.
#   - 성능은 높게(95% 이상) 나오지 않았지만 안정적이다.
#   - 과대적합(Overfitting) 경향이 없다.


