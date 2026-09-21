#!/usr/bin/env python
# coding: utf-8

# # 교차 검증과 그리드 서치 (Cross Validation & Grid/Randomized Search)
"""
본 스크립트는 모델 평가의 신뢰도를 높이기 위한 '교차 검증(Cross Validation)'과
최적의 하이퍼파라미터를 자동으로 탐색하는 '그리드 서치(GridSearchCV)',
'랜덤 서치(RandomizedSearchCV)'의 동작 원리 및 실습 과정을 다룸.

##################################################################
1. 검증 세트(Validation Set)의 필요성
- 테스트 세트를 사용하여 하이퍼파라미터를 반복 튜닝하면 모델이 테스트 세트에 과대적합됨.
- 이로 인해 실전 데이터 투입 시 일반화 성능이 저하되는 문제가 발생함.
- 따라서 테스트 세트는 최종 평가 직전까지 완전히 숨겨두고,
  모델 튜닝을 위한 평가용 데이터로 훈련 세트에서 '검증 세트'를 별도로 떼어내어 활용함.

##################################################################
2. 교차 검증 (Cross Validation)
- 훈련 세트에서 검증 세트를 분리하면 모델 훈련에 가용한 데이터양이 줄어드는 단점이 생김.
- 이를 해결하기 위해 훈련 세트를 K개 구간(폴드)으로 나누고,
  각 폴드를 한 번씩 검증 세트로 번갈아 사용하며 K번 평가한 후 평균 점수를 내는 K-폴드 교차 검증을 적용함.
- StratifiedKFold: 분류 모델의 경우 타깃 클래스 비율이 불균형할 수 있으므로,
  각 폴드마다 레이블 비율이 균등하게 배분되도록 계층적으로 분할해 주는 분할기(Splitter)임.

##################################################################
3. 그리드 서치 (GridSearchCV)
- 사람이 지정한 여러 하이퍼파라미터 후보들의 모든 조합(격자망)을 전수 조사함.
- 하이퍼파라미터 탐색과 교차 검증 과정을 단 한 번의 호출로 자동 수행함.
- 최적의 조합을 찾으면 전체 훈련 데이터로 모델을 자동 재학습하여 best_estimator_에 저장함.

##################################################################
4. 랜덤 서치 (RandomizedSearchCV)
- 탐색할 매개변수의 범위가 넓거나 조합 수가 매우 많을 때 그리드 서치의 연산 비용 문제를 해결함.
- 매개변수 후보 값을 직접 나열하는 대신, 확률 분포 객체(scipy.stats의 uniform, randint)를 전달함.
- 지정된 반복 횟수(n_iter)만큼 무작위로 매개변수 값을 샘플링하여 효율적으로 최적점을 탐색함.
"""

#%%
# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/05-2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

#%%
# ## 검증 세트 (Validation Set)

# In[1]:
# 판다스 라이브러리 임포트 및 원격 CSV 파일에서 와인 데이터 로드함
import pandas as pd

# 총 6,497개의 와인 샘플 데이터셋임
# wine = pd.read_csv('https://bit.ly/wine_csv_data')
wine = pd.read_csv('./wine.csv')


# In[2]:
# 입력 특성(알코올, 당도, pH)과 타깃 레이블(class: 0=레드와인, 1=화이트와인) 분리함
data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']


# In[3]:
# 전체 데이터를 훈련 세트(80%)와 테스트 세트(20%)로 분할함
# test_size=0.2로 설정하고 random_state=42로 시드를 고정함
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)


# In[4]:
# 훈련 세트(train_input)에서 다시 20%를 검증 세트(val_input)로 분할함
# 모델 튜닝 시 테스트 세트가 오염되는 것을 방지하기 위해 별도의 검증 세트를 확보함
sub_input, val_input, sub_target, val_target = train_test_split(
    train_input, train_target, test_size=0.2, random_state=42)


# In[5]:
# 실제 훈련에 사용할 훈련 세트(sub_input)와 검증 세트(val_input)의 크기(shape) 확인 및 출력함
# sub_input: 4,157개 샘플, val_input: 1,040개 샘플로 구성됨
print(sub_input.shape, val_input.shape)


# In[6]:
# 기본 결정 트리 모델을 생성하고 서브 훈련 세트로 학습을 진행함
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input, sub_target)

# 훈련 점수(약 99.7%)와 검증 점수(약 86.4%)를 각각 출력함
# 훈련 세트 점수에 비해 검증 세트 점수가 크게 낮아 과대적합이 발생함을 확인함
print(dt.score(sub_input, sub_target))
print(dt.score(val_input, val_target))


#%%
# ## 교차 검증 (Cross Validation)

# In[7]:
# cross_validate() 함수를 사용하여 전체 훈련 세트(5,197개)에 대해 기본 5-폴드 교차 검증을 수행함
from sklearn.model_selection import cross_validate

# 모델 훈련 시간(fit_time), 검증 시간(score_time), 각 폴드별 검증 점수(test_score)가 반환됨
scores = cross_validate(dt, train_input, train_target)
print(scores)


# In[8]:
# 넘파이 라이브러리를 임포트하고 5개 폴드의 검증 점수 평균을 계산하여 출력함
# 단순 1회 검증 점수(86.4%)보다 안정적인 평균 성능(약 85.5%)을 얻음
import numpy as np

print(np.mean(scores['test_score']))


# In[9]:
# 분류 모델에서 클래스 비율을 균등하게 유지하며 폴드를 나누기 위해 StratifiedKFold 분할기를 적용함
# cross_validate()의 기본 분할기 동작과 동일함을 확인함
from sklearn.model_selection import StratifiedKFold

scores = cross_validate(dt, train_input, train_target, cv=StratifiedKFold())
print(np.mean(scores['test_score']))


# In[10]:
# 10-폴드 교차 검증(n_splits=10)을 적용하고 데이터를 섞도록(shuffle=True) 설정하여 교차 검증을 수행함
# 폴드 수를 늘려 데이터 분할의 편향을 줄이고 평균 점수(약 85.7%)를 산출함
splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)
print(np.mean(scores['test_score']))


#%%
# ## 하이퍼파라미터 튜닝 (그리드 서치, GridSearchCV)

# In[11]:
# 탐색할 min_impurity_decrease(최소 불순도 감소량) 매개변수 후보 리스트를 딕셔너리로 정의함
from sklearn.model_selection import GridSearchCV

params = {'min_impurity_decrease': [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}


# In[12]:
# 결정 트리 모델과 매개변수 후보 딕셔너리를 전달하여 GridSearchCV 객체를 생성함
# n_jobs=-1로 지정하여 시스템의 모든 CPU 코어를 병렬로 투입함
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)


# In[13]:
# 그리드 서치를 실행하여 총 5개 후보 조합에 대해 5-폴드 교차 검증(총 25회 학습)을 자동으로 수행함
gs.fit(train_input, train_target)


# In[14]:
# 교차 검증에서 최고 점수를 낸 최적 모델 객체(best_estimator_)를 가져와 훈련 세트 성능을 측정함
# 그리드 서치는 최적의 하이퍼파라미터로 전체 훈련 세트에서 자동 재학습을 완료한 모델을 보관함
dt = gs.best_estimator_
print(dt.score(train_input, train_target))


# In[15]:
# 교차 검증에서 가장 높은 성능을 낸 최적의 하이퍼파라미터 값을 출력함 ({'min_impurity_decrease': 0.0001})
print(gs.best_params_)


# In[16]:
# 5가지 파라미터 조합 각각의 5-폴드 교차 검증 평균 점수 배열을 출력함
print(gs.cv_results_['mean_test_score'])


# In[17]:
# 가장 높은 검증 점수를 기록한 최적 조합 인덱스(best_index_)의 파라미터 정보를 직접 확인함
print(gs.cv_results_['params'][gs.best_index_])


# In[18]:
# 여러 하이퍼파라미터를 동시에 탐색하기 위한 복합 파라미터 딕셔너리를 구성함
# - min_impurity_decrease: 0.0001부터 0.001 직전까지 0.0001 단위로 9개 값
# - max_depth: 5부터 19까지 1 단위로 15개 값
# - min_samples_split: 2부터 92까지 10 단위로 10개 값
# 탐색할 총 파라미터 조합 수: 9 x 15 x 10 = 1,350개
params = {'min_impurity_decrease': np.arange(0.0001, 0.001, 0.0001),
          'max_depth': range(5, 20, 1),
          'min_samples_split': range(2, 100, 10)
          }


# In[19]:
# 1,350개 조합에 대해 5-폴드 교차 검증(총 6,750회 학습)을 병렬로 수행함
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
gs.fit(train_input, train_target)


# In[20]:
# 1,350개 조합 중 가장 우수한 검증 점수를 기록한 최적의 하이퍼파라미터 조합을 출력함
print(gs.best_params_)


# In[21]:
# 그리드 서치 결과 도출된 최고 교차 검증 평균 점수를 출력함 (약 86.9%)
print(np.max(gs.cv_results_['mean_test_score']))


#%%
# ### 랜덤 서치 (RandomizedSearchCV)

# In[22]:
# 수치형 매개변수 범위를 확률 분포로 정의하기 위해 scipy.stats의 uniform, randint 모듈을 임포트함
from scipy.stats import uniform, randint


# In[23]:
# randint: 0부터 9까지 정수를 균등한 확률로 추출하는 이산 확률 분포 객체를 생성하고 10개 샘플링을 테스트함
rgen = randint(0, 10)
rgen.rvs(10)


# In[24]:
# 1,000회 정수 무작위 추출을 수행한 후 각 숫자의 발생 빈도를 확인하여 균등 분포를 검증함
np.unique(rgen.rvs(1000), return_counts=True)


# In[25]:
# uniform: 0부터 1까지의 실수 구간에서 균등하게 추출하는 연속 확률 분포 객체를 생성하고 10개 샘플링을 테스트함
ugen = uniform(0, 1)
ugen.rvs(10)


# In[26]:
# 랜덤 서치를 위한 하이퍼파라미터 탐색 공간을 확률 분포 객체로 정의함
# - min_impurity_decrease: 0.0001 ~ 0.001 구간의 연속형 실수
# - max_depth: 20 ~ 49 범위의 이산형 정수
# - min_samples_split: 2 ~ 24 범위의 이산형 정수
# - min_samples_leaf: 1 ~ 24 범위의 이산형 정수
params = {'min_impurity_decrease': uniform(0.0001, 0.001),
          'max_depth': randint(20, 50),
          'min_samples_split': randint(2, 25),
          'min_samples_leaf': randint(1, 25),
          }


# In[27]:
# RandomizedSearchCV 객체를 생성하고 훈련 세트에 대해 랜덤 서치를 실행함
# n_iter=100 : 정의된 매개변수 분포에서 총 100회 무작위 샘플링하여 5-폴드 교차 검증(총 500회)을 수행함
from sklearn.model_selection import RandomizedSearchCV

rs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42), params,
                        n_iter=100, n_jobs=-1, random_state=42)
rs.fit(train_input, train_target)


# In[28]:
# 100회 샘플링 탐색 결과 가장 성능이 뛰어난 최적의 하이퍼파라미터 조합을 출력함
print(rs.best_params_)


# In[29]:
# 랜덤 서치 탐색을 통해 달성한 최고 교차 검증 평균 점수를 출력함 (약 86.9%)
print(np.max(rs.cv_results_['mean_test_score']))


# In[30]:
# 최적 모델(best_estimator_)을 추출하여 최종 테스트 세트(test_input)에 대한 일반화 정확도를 평가함
# 모델 튜닝 및 탐색 과정에 전혀 관여하지 않은 테스트 데이터로 최종 성능(약 86.0%)을 확인함
dt = rs.best_estimator_

print(dt.score(test_input, test_target))


#%%
# ## 확인문제 (splitter='random' 무작위 분할 트리 적용)

# In[31]:
# splitter='random' 옵션을 지정하여 노드 분할 시 무작위 분할을 수행하는 결정 트리를 대상으로 랜덤 서치를 실행함
# 동일한 매개변수 공간에서 100회 무작위 샘플링을 진행함
gs = RandomizedSearchCV(DecisionTreeClassifier(splitter='random', random_state=42), params,
                        n_iter=100, n_jobs=-1, random_state=42)
gs.fit(train_input, train_target)


# In[32]:
# splitter='random' 모델의 최적 하이퍼파라미터 조합 및 최고 교차 검증 평균 점수를 출력함
print(gs.best_params_)
print(np.max(gs.cv_results_['mean_test_score']))

# 도출된 최적 모델로 최종 테스트 세트 정확도를 평가하여 일반화 성능을 확인함
dt = gs.best_estimator_
print(dt.score(test_input, test_target))
