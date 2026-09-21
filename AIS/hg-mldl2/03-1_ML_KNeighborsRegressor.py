#!/usr/bin/env python
# coding: utf-8

# # k-최근접 이웃 회귀(KNeighborsRegressor)
"""
KNeighborsRegressor(k-최근접 이웃 회귀)는 scikit-learn에서 
제공하는 거리 기반의 대표적인 비모수(non-parametric) 회귀 알고리즘
특정 지점의 값을 예측하기 위해, 
훈련 데이터에서 훈련 데이터에서 가장 가까운 k개의 이웃(neighbor)을 찾음
회귀 문제에서는 이웃한 k개의 샘플들의 타겟 값(target value)의 평균을 예측값으로 사용
##################################################################
비모수 회귀(non-parametric regression)는 변수들 사이의 관계에 대해 
특정한 함수 형태(예: 선형식)를 미리 가정하지 않고, 
데이터가 가진 정보에 따라 유연하게 관계를 추정하는 회귀 분석 방법입니다. 

핵심 특징가정 없음: 데이터가 선형이나 특정 다항식을 따른다고 가정하지 않습니다.
유연성: 실제 데이터의 모습에 따라 곡선이나 복잡한 비선형 형태의 관계를 정확하게 찾을 수 있습니다.
데이터 주도: 모수(파라미터)의 개수가 고정되지 않고, 
    데이터 양이 늘어날수록 모델의 복잡도가 유연하게 변함
    
주요 알고리즘 및 기법
K-최근접 이웃 회귀(K-NN Regression): 예측하려는 데이터 주변의 가까운 K개 데이터 값의 평균을 이용해 결과를 예측
평활 스플라인(Smoothing Spline): 데이터 구간별로 부드러운 다항 함수를 연결해 전체 관계를 추정
커널 회귀(Kernel Regression): 가중치 함수(커널)를 사용해 가까운 데이터에는 높은 가중치를 주어 값을 추정
가우스 과정 회귀(Gaussian Process Regression): 데이터 간의 유사도를 확률적으로 정의하여 비선형 관계를 유연하게 예측

##################################################################
# 장점
# - 구현이 간단하고 직관적
# - 특별한 통계적 가정을 하지 않아 유연한 모델링이 가능
# - 단, 이로 인해 훈련 데이터의 분포에 모델의 성능이 좌우될 수 있음

# 단점
# - 훈련 데이터가 많아질수록 예측 시간이 길어짐
# - 고차원 데이터에서는 거리 계산의 의미가 퇴색될 수 있음(차원의 저주)  
# - k값과 거리 척도(metric) 선택에 따라 성능이 크게 달라질 수 있어, 
#   교차 검증(cross-validation)을 통한 튜닝이 필수적

########################################################################
1. 기본 동작 원리
분류(Classifier)와의 차이점:
    - KNeighborsClassifier (분류): 새로운 데이터 주변의 가장 가까운 k개 이웃을 찾고, 
      가장 많은 클래스(다수결)를 예측값으로 선택
    - KNeighborsRegressor (회귀): 새로운 데이터 주변의 가장 가까운 k개 이웃을 찾고, 
      그 이웃들의 타깃값의 수치 평균(평균값)을 예측값으로 계산
    - 예시 (농어 무게 예측): 길이 25cm인 농어의 무게를 예측할 때, 
      가장 가까운 이웃 3마리(k=3)의 무게가 
      각각 250g, 260g, 270g라면: 예측 무게 = (250 + 260 + 270) / 3 = 260g

2. 주요 하이퍼파라미터
    - n_neighbors (기본값: 5):
      참고할 이웃의 개수(k)
      - k가 작아질 때 (예: k=1): 국소적인 패턴까지 민감하게 반응하여 모델이 복잡해지고 
        과대적합(Overfitting) 가능성이 높아짐
      - k가 커질 때 (예: k=10, k=40): 여러 데이터의 평균을 내므로 모델이 단순해지고 부드러워지며, 
        너무 크면 전체 데이터의 평균에 가까워져 과소적합(Underfitting)이 발생
    - weights (기본값: 'uniform'): 가중치
      - 'uniform': 모든 이웃에 동일한 가중치를 부여(단순 산술 평균).
      - 'distance': 거리에 반비례하여 가까운 이웃에 더 높은 가중치를 부여(가중 평균).
    - metric (기본값: 'minkowski', p=2): 
      거리를 계산하는 공식(기본값은 유클리디안 거리).

3. 모델 평가 방법 (R^2 결정계수)
    분류에서는 맞춘 비율인 정확도(Accuracy)를 사용하지만, 
    회귀는 수치를 예측하므로 결정계수(R^2)를 기본 평가 척도로 사용

    R^2 = 1 - [ (타깃 - 예측)^2의 합 ] / [ (타깃 - 타깃평균)^2의 합 ]

    - 1에 가까울수록: 모델이 데이터를 매우 잘 예측함을 의미
    - 0에 가까울수록: 단순히 타깃의 평균값으로만 예측하는 수준임을 뜻
    - 보조 지표로 MAE(Mean Absolute Error)를 사용해 
      "예측이 평균적으로 약 몇 g 정도 벗어나는지" 직관적인 오차 크기를 확인

4. 장단점 및 치명적인 한계점
    - 장점
        - 개념이 단순하고 직관적
        - 데이터의 수학적 분포(선형성 등)를 미리 가정하지 않으므로 
          복잡한 비선형 관계도 잘 포착

    - 치명적인 한계점 (외삽 문제, Extrapolation)
        - 훈련 세트 범위 밖 예측 불가 (가장 중요한 한계):
            새로운 데이터가 훈련 세트의 최대값보다 훨씬 크거나 최소값보다 훨씬 작아도, 
            가장 가까운 훈련 데이터 이웃들의 평균값만을 출력합니다.
            예를 들어, (100cm) 크기의 거대한 농어가 들어와도 훈련 세트에서 
            가장 큰 (44cm) 근처 이웃들의 평균 무게(약 1000g)로만 예측해 버림
            이 한계를 극복하기 위해 선형 회귀(Linear Regression)나 다항 회귀를 사용
    - 스케일 민감성:
        - 거리 기반 알고리즘이므로, 특성 간의 단위(스케일)가 다르면 반드시 
          표준화/정규화 전처리가 필요함
    - 데이터 크기에 따른 계산 비용:
        - 학습 단계에서는 데이터를 저장만 해두고, 
          예측 시점에 모든 데이터와의 거리를 계산하므로 
          데이터가 많아질수록 메모리와 예측 시간이 급증
"""

#%%
# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/03-1.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

#%%
# ## 데이터 준비

# In[1]:


import numpy as np


# In[2]:


# 훈련 데이터: 56개
perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )

# 타겟(정답): 56개
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[5]:


from sklearn.model_selection import train_test_split


# In[6]:

# 데이터 분할: 훈련, 테스트
train_input, test_input, train_target, test_target = train_test_split(
    perch_length, # 훈련 데이터
    perch_weight, # 정답 데이터
    random_state=42)


# In[7]:

# 총 56개 데이터
# 훈련 데이터: 42(75%)
# 평가 데이터: 14(25%)
print(train_input.shape, test_input.shape) # (42,) (14,)


# In[8]:

test_array = np.array([1,2,3,4])
print(test_array.shape) # (4,)


# In[9]:

# 1차원(4개) -> 2차원(2 * 2)
test_array = test_array.reshape(2, 2)
print(test_array.shape) # (2, 2)
print(test_array) # (2, 2)

#%%

"""
원본: [1,2,3,4]
변환:
[[1 2]
 [3 4]]
"""

# In[10]:

# 아래 코드의 주석을 제거하고 실행하면 에러가 발생합니다
# ValueError: cannot reshape array of size 4 into shape (2,3)
# test_array = test_array.reshape(2, 3)


# In[11]:

# 훈련 데이터는 2차원이야 한다.
# reshape()를 하지 않으면 오류 발생    
# ValueError: Expected 2D array, got 1D array instead
# reshape(-1, 1): -1은 열에 맞춰서 행을 자동으로 지정
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)


# In[12]:

print(train_input.shape, test_input.shape) # (42, 1) (14, 1)

#%%

# ## 결정 계수 ($ R^2$)

# In[13]:

# k-최근접 이웃 회귀 모델
from sklearn.neighbors import KNeighborsRegressor


# In[14]:

# 모델 객체 생성
knr = KNeighborsRegressor()

#%%

# k-최근접 이웃 회귀 모델을 훈련합니다
knr.fit(train_input, train_target)

#%%

# 훈련점수: 0.9698823289099254
knr_train_score = knr.score(train_input, train_target)
print("# 훈련점수:", knr_train_score);

# In[15]:

# 과소적합: 테스트 점수가 훈련 점수보다 높음
# 평가점수: 0.992809406101064
knr_test_score = knr.score(test_input, test_target)
print("# 평가점수:", knr_test_score);


# In[16]:

# 평균 절댓값 오차
from sklearn.metrics import mean_absolute_error


# In[17]:

# 테스트 세트에 대한 예측을 만듭니다
test_prediction = knr.predict(test_input)

# 테스트 세트에 대한 평균 절댓값 오차를 계산합니다
mae = mean_absolute_error(test_target, test_prediction)
print(mae) # 19.157142857142862

#%%

"""
결과: 19.157142857142862
단위: 약 19.16g
해석: 모델이 예측한 농어의 무게는 실제 농어 무게와
      평균적으로 약 19g 정도 차이가 난다.
"""

#%%

# ## 과대적합 vs 과소적합

# In[18]:

# 결과분석: 과소적합    
# 훈련점수: 0.9698823289099254
# 평가점수: 0.992809406101064
print("# 훈련점수:", knr.score(train_input, train_target))
print("# 평가점수:", knr.score(test_input, test_target))


# In[19]:

# 이웃의 갯수를 5에서 3으로 줄여서 민감도를 올려 복잡도 증가
# 훈련점수는 증가하고 평가점수는 하락하는 효과를 얻을 수 있다.
# 그 결과 훈련점수가 평가점수 보다 좀금 높게 나오도록 유도

# 이웃의 갯수를 3으로 설정합니다
knr.n_neighbors = 3

# 모델을 다시 훈련합니다
knr.fit(train_input, train_target)

# 변경전
# 훈련점수: 0.9698823289099254
# 평가점수: 0.992809406101064

# 변경후
# 훈련점수: 0.9804899950518966
# 평가점수: 0.9746459963987609
print("# 훈련점수:", knr.score(train_input, train_target))
print("# 평가점수:", knr.score(test_input, test_target))


#%%
# ## 확인문제

# In[21]:


# k-최근접 이웃 회귀 객체를 만듭니다
# n_neighbors : 5, 기본값
knr = KNeighborsRegressor(n_neighbors = 5)

# 농어의 길이: 5에서 45까지 x 좌표를 만듭니다
x = np.arange(5, 45).reshape(-1, 1)

# 하이퍼파리미터: 이웃의 갯수
# n = 1, 5, 10일 때 예측 결과를 그래프로 그립니다.
for n in [1, 5, 10]:
    # 모델 훈련
    knr.n_neighbors = n  # 이웃의 갯수
    knr.fit(train_input, train_target)
    
    # 농어의 무게 예측
    # 지정한 범위 x에 대한 예측 구하기
    prediction = knr.predict(x) 
    
    # 훈련 세트와 예측 결과 그래프 그리기
    plt.scatter(train_input, train_target)
    
    # 예측된 농어의 무게를 y축으로 지정하여 선을 그림
    plt.plot(x, prediction)
    
    plt.title('n_neighbors = {}'.format(n))
    plt.xlabel('length')
    plt.ylabel('weight')
    plt.show()

