#!/usr/bin/env python
# coding: utf-8

# # 로지스틱 회귀

# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/04-1.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# ## 럭키백의 확률

# ### 데이터 준비하기

# In[1]:


import pandas as pd

# fish = pd.read_csv('https://bit.ly/fish_csv_data')
fish = pd.read_csv('./fish.csv')
fish.head()


# In[2]:

# 종류: 7가지
# ['Bream', 'Roach', 'Whitefish', 'Parkki', 'Perch', 'Pike', 'Smelt']
print(pd.unique(fish['Species']))

# In[3]:

# 특성변수(독립변수)    
# 데이터프레임: 2차원
# 물고기의 종류 컬럼을 제외한 나머지 컬럼을 새로운 데이터프레임으로 구성
fish_input = fish[['Weight','Length','Diagonal','Height','Width']]


# In[4]:

fish_input.head()


# In[5]:

# 시리즈: 1차원
# 정답(타깃): 물고기 종류
fish_target = fish['Species']


# In[6]:

# 훈련셋, 테스트셋으로 분할: 75:25
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    fish_input,  # 훈련 데이터
    fish_target, # 정답 데이터
    random_state=42)


# In[7]:

# 정규화: 스케일
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

#%%

# ### k-최근접 이웃 분류기의 확률 예측

# In[8]:


from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier(n_neighbors=3)
kn.fit(train_scaled, train_target)

print(kn.score(train_scaled, train_target)) # 0.8907563025210085
print(kn.score(test_scaled, test_target))   # 0.85


# In[9]:

# 분류 클래스와 순서를 확인    
# ['Bream' 'Parkki' 'Perch' 'Pike' 'Roach' 'Smelt' 'Whitefish']
print(kn.classes_)

# In[10]:

# 예측: 5개 데이터
print(kn.predict(test_scaled[:5]))


# In[11]:

import numpy as np

# 클래스별 확률값
proba = kn.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=4))


# In[12]:

# 예측: 'Perch'
# 정답: 'Whitefish'
distances, indexes = kn.kneighbors(test_scaled[3:4])
print(train_target.iloc[indexes[0]])
print("정답:", test_target.iloc[3])

#%%

# 이웃이 'Perch'
"""
52     Roach
106    Perch
103    Perch
"""


#%%
# ## 로지스틱 회귀

# In[13]:

# 시그모이드 함수(sigmod function)
# 이진분류(0,1)를 하는데 0.5보다 크면 1이며 0.5보다 작으면 0
# 사이킷런(scikit learn)에서는 0.5이면 음성(0)으로 판단
    
# 시그모이드 그래프
import numpy as np
import matplotlib.pyplot as plt

# x축: -5에서 5사이에 0.1씩 간격
# y축: sigmod 함수 값
z = np.arange(-5, 5, 0.1)
phi = 1 / (1 + np.exp(-z))

plt.plot(z, phi)
plt.xlabel('z')
plt.ylabel('phi')
plt.show()

#%%

# ### 로지스틱 회귀로 이진 분류 수행하기

# In[14]:

# 예시 코드
# True인 값이 선택
char_arr = np.array(['A', 'B', 'C', 'D', 'E'])
print(char_arr[[True, False, True, False, False]]) # ['A' 'C']


# In[15]:

# 도미(Bream)와 빙어(Smelt)를 분류
# 도미와 빙어인 행은 True, 아니면 False인 시리즈
# OR: |
bream_smelt_indexes = (train_target == 'Bream') | (train_target == 'Smelt')

# 행: 119개의 행에서 33개의 행을 선택
# 열: 5개로 동일
# 넘파이 배열: train_scaled(119,5)  -> train_bream_smelt(33,5)
train_bream_smelt = train_scaled[bream_smelt_indexes]

# 정답(119)에서 33개 선택
# 시리즈: train_target(119) -> target_bream_smelt(33)
target_bream_smelt = train_target[bream_smelt_indexes]


# In[16]:

# 로지스틱 회귀 모델
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(train_bream_smelt, target_bream_smelt)


# In[17]:

# 정답: ['Bream' 'Smelt' 'Bream' 'Bream' 'Bream']   
# 결과: ['Bream' 'Smelt' 'Bream' 'Bream' 'Bream']    
print(target_bream_smelt.iloc[:5])       # 정답
print(lr.predict(train_bream_smelt[:5])) # 예측


# In[18]:

# 확률값
print(lr.predict_proba(train_bream_smelt[:5]))

#%%

['Bream' 'Smelt' 'Bream' 'Bream' 'Bream'] 
"""
 [ 'Bream'     'Smelt'   
[[0.99760007 0.00239993]
 [0.02737325 0.97262675]
 [0.99486386 0.00513614]
 [0.98585047 0.01414953]
 [0.99767419 0.00232581]]
"""

# In[19]:

# ['Bream' 'Smelt']
print(lr.classes_) 


# In[20]:

# 계수와 절편
print(lr.coef_, lr.intercept_)
# [[-0.40451732 -0.57582787 -0.66248158 -1.01329614 -0.73123131]] [-2.16172774]

# In[21]:

# z값
decisions = lr.decision_function(train_bream_smelt[:5])
print(decisions)
# [-6.02991358  3.57043428 -5.26630496 -4.24382314 -6.06135688]

# In[22]:

# 사이파이(spipy) 라이브러의 시그모이드 함수(expit)로
# decisions 배열의 값을 확률로 변환
from scipy.special import expit

print(expit(decisions))
# [0.00239993 0.97262675 0.00513614 0.01414953 0.00232581]

# 예측된 확률값 중에서 컬럼 1번째의 'Smelt' 값
print(lr.predict_proba(train_bream_smelt[:5])[:,1])
# [0.00239993 0.97262675 0.00513614 0.01414953 0.00232581]

# 이유:
# lr.classes_: Bream(0, 음성), Smelt(1, 양성)    
# decision_function() 메서드는 양성(1) 클래스에 대한 z값을 반환한다.
# 

#%%

# ### 로지스틱 회귀로 다중 분류 수행하기
# 생선 분류: 7가지 생선
# 이진 분류와 차이점 확인

# In[23]:

# 하이퍼파라미터: C, max_iter
# C: 규제를 제어, 기본값 1, 값이 작을 수록 규제가 커짐, 20은 규제를 완화
# max_iter: 훈련 반복 횟수, 기본값 100
lr = LogisticRegression(C=20, max_iter=1000)
lr.fit(train_scaled, train_target)

print(lr.score(train_scaled, train_target)) # 0.9327731092436975
print(lr.score(test_scaled, test_target))   # 0.925


# In[24]:

# 5개의 샘플 예측
# 예측: ['Perch' 'Smelt' 'Pike' 'Roach' 'Perch']
print(lr.predict(test_scaled[:5]))

# 정답: ['Perch', 'Smelt', 'Pike', 'Whitefish', 'Perch']
print(list(test_target.iloc[:5]))


# In[25]:


proba = lr.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=3))

#%%

"""
[[0.    0.014 0.842 0.    0.135 0.007 0.003]
 [0.    0.003 0.044 0.    0.007 0.946 0.   ]
 [0.    0.    0.034 0.934 0.015 0.016 0.   ]
 [0.011 0.034 0.305 0.006 0.567 0.    0.076]   <-- 예측(Roach), 정답(Whitefish)
 [0.    0.    0.904 0.002 0.089 0.002 0.001]]
"""

# In[26]:

# ['Bream' 'Parkki' 'Perch' 'Pike' 'Roach' 'Smelt' 'Whitefish']
print(lr.classes_)


# In[27]:

# 분류: 7개
# 특성: 5개
# 계수, 절편의 모양: (7, 5) (7,)
print(lr.coef_.shape, lr.intercept_.shape)

#%%

print(lr.coef_, lr.intercept_)


# In[28]:

# z값    
decision = lr.decision_function(test_scaled[:5])
print(np.round(decision, decimals=2))


# In[29]:

# 소프트맥스 함수
# 다중 분류에서 여러 선형 방정식의 출력 결과를 
# 정규화하여 합이 1이 되도록 만듦
# ※ 로지스틱 회귀 모델이 다중 분류일 때 소프트맥스 함수를 사용한다.
from scipy.special import softmax

# axis=1: 각 행별 계산 즉 각 샘플 별 계산
proba = softmax(decision, axis=1)
print(np.round(proba, decimals=3))

#%%

# softmax
"""
[[0.    0.014 0.842 0.    0.135 0.007 0.003]
 [0.    0.003 0.044 0.    0.007 0.946 0.   ]
 [0.    0.    0.034 0.934 0.015 0.016 0.   ]
 [0.011 0.034 0.305 0.006 0.567 0.    0.076]
 [0.    0.    0.904 0.002 0.089 0.002 0.001]]
"""

#%%

# lr.predict_proba(test_scaled[:5])
"""
[[0.    0.014 0.842 0.    0.135 0.007 0.003]
 [0.    0.003 0.044 0.    0.007 0.946 0.   ]
 [0.    0.    0.034 0.934 0.015 0.016 0.   ]
 [0.011 0.034 0.305 0.006 0.567 0.    0.076]
 [0.    0.    0.904 0.002 0.089 0.002 0.001]]
"""