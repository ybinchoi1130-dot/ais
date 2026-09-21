#!/usr/bin/env python
# coding: utf-8

# # 확률적 경사 하강법

# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/04-2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# ## SGDClassifier

# In[1]:


import pandas as pd

# https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fish.csv
# fish = pd.read_csv('https://bit.ly/fish_csv_data')
fish = pd.read_csv('./fish.csv')



# In[2]:

# 특성 컬럼
fish_input = fish[['Weight','Length','Diagonal','Height','Width']]

# 정답 컬럼
fish_target = fish['Species']


# In[3]:

from sklearn.model_selection import train_test_split

# 훈련 세트, 테스트 세트로 분할
train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state=42)


# In[4]:

# 정규화 스케일: 표준화 전처리
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)


# In[5]:

# 확률적 경사 하강법 모델
from sklearn.linear_model import SGDClassifier


# In[6]:

# 모델 객체 생성
# 손실함수: loss='log_loss', 로지스틱 손실함수(Logistic Loss Function)
# 반복횟수: max_iter=10, 에포크(epoch) 10번
sc = SGDClassifier(loss='log_loss', max_iter=10, random_state=42)
sc.fit(train_scaled, train_target)

print(sc.score(train_scaled, train_target)) # 0.773109243697479
print(sc.score(test_scaled, test_target))   # 0.775

#%%

# 경고 발생 이유:
# 사이킷런의 모델이 충분히 수렴하지 않았다는 경고
# max_iter 값을 늘려라    
"""
ConvergenceWarning: 
Maximum number of iteration reached before convergence. 
Consider increasing max_iter to improve the fit.
"""

# In[7]:

# 점진적인 학습
# 호출할 때마다 1에포크씩 이어서 훈련을 진행
# 결과: 훈련 평가는 2.5% 증가, 테스트 평가는 동일
sc.partial_fit(train_scaled, train_target)

print(sc.score(train_scaled, train_target)) # 0.7983193277310925
print(sc.score(test_scaled, test_target))   # 0.775

#%%

# ## 에포크와 과대/과소적합

# In[8]:

import numpy as np

# 모델 객체 생성
# 손실함수: loss='log_loss', 로지스틱 손실함수(Logistic Loss Function)
# 반복횟수: max_iter=1000, 기본값 1000번의 에포크(epoch)
sc = SGDClassifier(loss='log_loss', random_state=42)

# 훈련 및 평가 결과 저장용 변수
train_score = []
test_score = []

# 분류하고자 하는 물고기의 종류: 7개
# ['Bream' 'Parkki' 'Perch' 'Pike' 'Roach' 'Smelt' 'Whitefish']
classes = np.unique(train_target)
print(classes) # numpy Array

classes2 = train_target.unique()
print(classes2) # StringArray
classes3 = pd.unique(train_target)
print(classes3) # StringArray

# In[9]:

for _ in range(0, 300):
    sc.partial_fit(train_scaled, train_target, classes=classes)
    # sc.partial_fit(train_scaled, train_target, classes=classes2)

    train_score.append(sc.score(train_scaled, train_target))
    test_score.append(sc.score(test_scaled, test_target))

#%%

# 100번째 결과
print(train_score[99]) # 0.9411764705882353
print(test_score[99])  # 0.925

# In[10]:

# 그래프 확인 결과
# 100번째에 더 이상 향상 되지 않음을 확인
import matplotlib.pyplot as plt

plt.plot(train_score)
plt.plot(test_score)
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()


# In[11]:

# 손실함수: loss='log_loss', 로지스틱 손실함수(Logistic Loss Function)
# 반복횟수: 100번의 에포크(epoch)
# 조기종료: tol(toerance), Early Stopping, 비활성화(조기종료를 하지 마라)
sc = SGDClassifier(loss='log_loss', max_iter=100, tol=None, random_state=42)
sc.fit(train_scaled, train_target)

print(sc.score(train_scaled, train_target)) # 0.957983193277311
print(sc.score(test_scaled, test_target))   # 0.925

#%%

# 손실함수: loss='log_loss', 로지스틱 손실함수(Logistic Loss Function)
# 반복횟수: 300번의 에포크(epoch)
# 조기종료: tol(toerance), Early Stopping, 활성화
scx = SGDClassifier(loss='log_loss', max_iter=300, tol=0.0001, random_state=42)
scx.fit(train_scaled, train_target)

print("에포크 횟수:", scx.n_iter_)           # 32번에 멈춤
print(scx.score(train_scaled, train_target)) # 0.7226890756302521
print(scx.score(test_scaled, test_target))   # 0.675

#%%

# 손실함수: loss='log_loss', 로지스틱 손실함수(Logistic Loss Function)
# 반복횟수: 300번의 에포크(epoch)
# 조기종료: tol(toerance), Early Stopping, 활성화
# 대기횟수: 기본값 5회, n_iter_no_change=20,
scx = SGDClassifier(loss='log_loss', 
                    max_iter=300, 
                    tol=0.001, 
                    n_iter_no_change=20,
                    random_state=42)
scx.fit(train_scaled, train_target)

print("에포크 횟수:", scx.n_iter_)           # 123번에 멈춤
print(scx.score(train_scaled, train_target)) # 0.9495798319327731
print(scx.score(test_scaled, test_target))   # 0.925


# In[12]:

# 힌지(hinge) 손실 함수
# 서포트 백터 머신(SVM, Support Vector Machine) 알고리즘에서 
# 결정 경계를 찾기 위해 사용하는 손실함수
# 손실함수: loss='hinge' 기본값
sc = SGDClassifier(loss='hinge', max_iter=100, tol=None, random_state=42)
sc.fit(train_scaled, train_target)

print(sc.score(train_scaled, train_target)) # 0.9495798319327731
print(sc.score(test_scaled, test_target))   # 0.925

