#!/usr/bin/env python
# coding: utf-8

# # 트리의 앙상블 (Tree Ensemble)
"""
본 스크립트는 정형 데이터(Tabular Data) 분석에서 가장 뛰어난 성능을 발휘하는
다양한 '트리 기반 앙상블 학습(Ensemble Learning)' 기법의 원리와 실습을 다룸.

##################################################################
1. 앙상블 학습(Ensemble Learning)의 개념
- 단일 결정 트리는 해석이 쉽지만 과대적합되기 쉽고 일반화 성능이 불안정한 한계가 있음.
- 앙상블 학습은 여러 개의 약한 학습기(결정 트리)를 결합하여 단일 모델의 높은 분산을 낮추고,
  훨씬 더 강력하고 안정적인 예측 성능을 도출하는 기법임.

##################################################################
2. 주요 앙상블 모델 비교
(1) 랜덤 포레스트 (Random Forest)
    - 배깅(Bagging: Bootstrap Aggregating)의 대표적인 알고리즘임.
    - 부트스트랩 샘플(훈련 데이터에서 중복을 허용하여 무작위 복원 추출한 샘플)을 기반으로 각 트리를 훈련함.
    - 노드 분할 시 전체 특성이 아닌 무작위로 선택된 일부 특성(전체 특성의 제곱근 개)만을 검토하여 트리 간의 상관관계를 낮춤.
    - OOB(Out-of-Bag) 평가: 부트스트랩 샘플링에 포함되지 않고 남은 약 37%의 샘플을 자체 검증 세트로 활용할 수 있음.

(2) 엑스트라 트리 (Extra Trees)
    - 랜덤 포레스트와 유사하나, 부트스트랩 샘플링을 쓰지 않고 전체 훈련 세트를 사용함.
    - 노드 분할 시 최적의 분할 임계값을 찾는 대신 '무작위 임계값'을 선택하여 분할함.
    - 계산 속도가 매우 빠르고, 트리의 분산을 낮추어 과대적합을 강력히 억제함.

(3) 그레이디언트 부스팅 (Gradient Boosting)
    - 부스팅(Boosting)의 대표적인 기법으로, 깊이가 얕은(기본 max_depth=3) 약한 결정 트리를 순차적으로 추가함.
    - 이전 트리가 예측하고 남은 잔여 오차(경사하강법의 손실 함수 기울기)를 다음 트리가 맞추도록 순차 학습을 진행함.
    - 과대적합에 매우 강하고 높은 정확도를 보이나, 순차 학습 특성상 훈련 속도가 다소 느림.

(4) 히스토그램 기반 그레이디언트 부스팅 (HistGradientBoostingClassifier)
    - 대규모 데이터에서 훈련 속도를 획기적으로 개선한 사이킷런의 최신 부스팅 알고리즘임.
    - 입력 특성을 256개의 구간(bin)으로 변환(양자화)하여 최적의 분할을 매우 빠르게 찾아냄.
    - 256개 구간 중 1개를 결측치 전용 구간으로 배정하여 누락된 결측값을 자동 처리함.
    - 모델 해석 시 특성 중요도 대신 치환 중요도(permutation_importance)를 주로 활용함.

(5) 대표적 외부 부스팅 라이브러리
    - XGBoost: 캐글 등 머신러닝 경진대회에서 널리 검증된 고성능 부스팅 라이브러리임 (tree_method='hist' 지원).
    - LightGBM: 리프 중심(Leaf-wise) 분할 방식을 적용하여 대규모 데이터에서 학습 속도가 매우 빠르고 메모리 효율이 뛰어남.
"""

#%%
# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/05-3.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

#%%
# ## 랜덤 포레스트 (Random Forest)

# In[1]:
# 필요한 라이브러리 임포트 및 원격 CSV 파일에서 와인 데이터셋 로드함
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

wine = pd.read_csv('https://bit.ly/wine_csv_data')

# 독립변수 특성(알코올, 당도, pH)과 종속변수 타깃(class: 0=레드와인, 1=화이트와인) 분리함
data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']

# 전체 데이터를 훈련 세트(80%)와 테스트 세트(20%)로 분할함 (시드 42 고정)
train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)


# In[2]:
# RandomForestClassifier 모델을 생성하고 5-폴드 교차 검증을 수행함
# return_train_score=True로 지정하여 검증 점수뿐 아니라 훈련 점수도 함께 수집함
# n_jobs=-1로 지정하여 모든 CPU 코어를 병렬로 활용함
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(rf, train_input, train_target, return_train_score=True, n_jobs=-1)

# 5-폴드 교차 검증 훈련 점수 평균(약 99.7%)과 검증 점수 평균(약 89.1%)을 출력함
# 단일 결정 트리(85.5%)에 비해 검증 점수가 대폭 향상됨을 확인함
print(np.mean(scores['train_score']), np.mean(scores['test_score']))


# In[3]:
# 전체 훈련 세트로 랜덤 포레스트 모델을 훈련하고 각 특성의 중요도를 확인함
rf.fit(train_input, train_target)

# 특성 순서: ['alcohol', 'sugar', 'pH']
# 단일 결정 트리는 당도(sugar) 중요도가 87%로 극단적이었으나,
# 랜덤 포레스트는 무작위 특성 선택 효과로 인해 당도(약 68%), 알코올(약 23%), pH(약 9%)로 더 균형 있게 분산됨
print(rf.feature_importances_)


# In[4]:
# oob_score=True 설정으로 부트스트랩 샘플에 포함되지 않은 OOB(Out-of-Bag) 샘플을 이용한 자체 평가를 활성화함
# 별도의 검증 세트를 분리하지 않고도 모델의 일반화 성능을 신뢰성 있게 평가할 수 있음
rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)

rf.fit(train_input, train_target)

# OOB 평가 점수(약 89.3%)를 출력함 (교차 검증 점수 89.1%와 매우 유사하게 측정됨)
print(rf.oob_score_)


#%%
# ## 엑스트라 트리 (Extra Trees)

# In[5]:
# ExtraTreesClassifier 모델을 생성하고 교차 검증을 수행함
# 부트스트랩 샘플링 없이 전체 훈련 데이터를 사용하고, 노드 분할 시 무작위 임계값을 적용함
from sklearn.ensemble import ExtraTreesClassifier

et = ExtraTreesClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(et, train_input, train_target,
                        return_train_score=True, n_jobs=-1)

# 엑스트라 트리의 훈련 점수 평균(약 99.7%)과 검증 점수 평균(약 88.9%)을 출력함
# 랜덤 분할로 인해 개별 트리의 성능은 낮아질 수 있으나 앙상블을 통해 과대적합을 방지하고 빠른 연산 속도를 제공함
print(np.mean(scores['train_score']), np.mean(scores['test_score']))


# In[6]:
# 전체 훈련 세트로 엑스트라 트리를 학습한 후 특성 중요도를 출력함
# 랜덤 포레스트와 유사하게 여러 특성에 고르게 분산된 특성 중요도를 나타냄
et.fit(train_input, train_target)
print(et.feature_importances_)


#%%
# ## 그레이디언트 부스팅 (Gradient Boosting)

# In[7]:
# GradientBoostingClassifier 모델을 생성하고 교차 검증을 수행함
# 기본적으로 깊이가 얕은 결정 트리(max_depth=3) 100개를 순차적으로 배치하여 오차를 줄여나감
from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier(random_state=42)
scores = cross_validate(gb, train_input, train_target,
                        return_train_score=True, n_jobs=-1)

# 훈련 점수 평균(약 88.8%)과 검증 점수 평균(약 87.2%)을 출력함
# 훈련 점수와 검증 점수 간의 격차가 매우 작아 과대적합이 거의 발생하지 않음을 확인함
print(np.mean(scores['train_score']), np.mean(scores['test_score']))


# In[8]:
# 트리 개수를 500개(n_estimators=500)로 늘리고 학습률을 0.2(learning_rate=0.2)로 높여 모델 성능을 강화함
gb = GradientBoostingClassifier(n_estimators=500, learning_rate=0.2,
                                random_state=42)
scores = cross_validate(gb, train_input, train_target,
                        return_train_score=True, n_jobs=-1)

# 하이퍼파라미터 변경 후 훈련 점수(약 94.6%)와 검증 점수(약 87.8%)를 확인함
# 과대적합을 억제하면서도 검증 점수가 소폭 상승함을 확인함
print(np.mean(scores['train_score']), np.mean(scores['test_score']))


# In[9]:
# 전체 훈련 세트로 그레이디언트 부스팅 모델을 학습하고 특성 중요도를 확인함
# 그레이디언트 부스팅은 오차 보정에 결정적인 당도(sugar) 특성에 높은 비중을 둠을 확인함
gb.fit(train_input, train_target)
print(gb.feature_importances_)


#%%
# ## 히스토그램 기반 그레이디언트 부스팅 (HistGradientBoostingClassifier)

# In[10]:
# 특성을 256개 구간으로 이산화하여 최적의 분할을 초고속으로 찾는 HistGradientBoostingClassifier 적용함
from sklearn.ensemble import HistGradientBoostingClassifier

hgb = HistGradientBoostingClassifier(random_state=42)
scores = cross_validate(hgb, train_input, train_target,
                        return_train_score=True, n_jobs=-1)

# 훈련 점수 평균(약 93.2%)과 검증 점수 평균(약 88.0%)을 출력함
# 정형 데이터에서 매우 안정적이고 강력한 성능과 빠른 속도를 보여줌
print(np.mean(scores['train_score']), np.mean(scores['test_score']))


# In[11]:
# 치환 중요도(permutation_importance)를 사용하여 훈련 세트 기준 특성 중요도를 계산함
# 특정 특성의 값을 무작위로 섞었을 때 모델 성능이 얼마나 감소하는지를 측정하여 중요도를 산출함 (10회 반복 측정)
from sklearn.inspection import permutation_importance

hgb.fit(train_input, train_target)
result = permutation_importance(hgb, train_input, train_target, n_repeats=10,
                                random_state=42, n_jobs=-1)

# 훈련 세트 기준 3개 특성의 평균 중요도(importances_mean)를 출력함
# 값이 클수록 모델 예측에 필수적인 특성임을 의미함 (당도가 가장 높음)
print(result.importances_mean)


# In[12]:
# 테스트 세트에 대해서도 치환 중요도를 동일하게 측정함
# 실전 테스트 데이터에서도 각 특성이 실제 예측에 미치는 기여도를 객관적으로 검증함
result = permutation_importance(hgb, test_input, test_target, n_repeats=10,
                                random_state=42, n_jobs=-1)
print(result.importances_mean)


# In[13]:
# 최종 테스트 세트에서 히스토그램 기반 그레이디언트 부스팅 모델의 최종 정확도를 평가함 (약 87.2%)
hgb.score(test_input, test_target)


#%%
# #### 외부 부스팅 라이브러리: XGBoost

# In[14]:
# 데이터 재로드 및 훈련/테스트 세트 분할을 다시 실행함
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate

wine = pd.read_csv('https://bit.ly/wine_csv_data')

data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']

train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)


# In[15]:
# XGBoost 라이브러리의 XGBClassifier 모델을 생성하고 교차 검증을 수행함
# tree_method='hist'를 지정하여 히스토그램 기반 고속 트리 알고리즘을 사용함
from xgboost import XGBClassifier

xgb = XGBClassifier(tree_method='hist', random_state=42)
xgb._estimator_type = "classifier"
scores = cross_validate(xgb, train_input, train_target,
                        return_train_score=True, n_jobs=-1)

# XGBoost 모델의 훈련 점수 평균(약 95.5%)과 검증 점수 평균(약 87.8%)을 출력함
print(np.mean(scores['train_score']), np.mean(scores['test_score']))


#%%
# #### 외부 부스팅 라이브러리: LightGBM

# In[16]:
# LightGBM 라이브러리의 LGBMClassifier 모델을 생성하고 교차 검증을 수행함
# 리프 중심 트리 분할 방식으로 대용량 데이터에서 속도가 매우 빠르고 성능이 우수함
from lightgbm import LGBMClassifier

lgb = LGBMClassifier(random_state=42)
scores = cross_validate(lgb, train_input, train_target,
                        return_train_score=True, n_jobs=-1)

# LightGBM 모델의 훈련 점수 평균(약 93.6%)과 검증 점수 평균(약 87.9%)을 출력함
print(np.mean(scores['train_score']), np.mean(scores['test_score']))
