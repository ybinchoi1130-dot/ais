#!/usr/bin/env python
# coding: utf-8

# # 결정 트리 (Decision Tree, DecisionTreeClassifier)
"""
DecisionTreeClassifier(결정 트리 분류기):
scikit-learn에서 제공하는 규칙 기반의 대표적인 지도학습(Supervised Learning) 분류 알고리즘임.

데이터에 있는 특성들을 바탕으로 "예/아니오" 형태의 연속적인 질문(분기 조건)을 만들어가며 
데이터를 더 순수한(한 가지 클래스만 모여 있는) 부분 집합으로 분할해 나감.

##################################################################
1. 등장 배경 및 필요성 (로지스틱 회귀와의 비교)
- 로지스틱 회귀와 같은 선형 모델은 가중치(기울기, coef_)와 절편(intercept_)을 학습함.
- 하지만 "왜 당도가 4.3% 이상이고 알코올이 10% 이상일 때 화이트 와인인가?"와 같은
  직관적인 근거를 제시하기 어려움.
- 결정 트리는 사람이 생각하는 의사결정 방식(스무고개)과 매우 유사하여,
  모델의 예측 과정과 규칙을 시각화하고 설명하기 매우 쉽다는 
  강력한 장점(화이트박스 모델)을 가짐.

##################################################################
2. 핵심 개념 및 분기 기준 (불순도와 정보 이득)
(1) 노드(Node)의 구성
    - 루트 노드(Root Node): 맨 꼭대기에 위치한 첫 번째 질문 노드
    - 내부 노드(Internal Node): 중간에 위치한 조건 질문 노드
    - 리프/말단 노드(Leaf/Terminal Node): 더 이상 분기하지 않고 최종 클래스를 결정하는 노드

(2) 지니 불순도 (Gini Impurity, 기본 분기 기준)
    Gini = 1 - (음성 클래스 비율^2 + 양성 클래스 비율^2)
    - 0.5: 두 클래스가 5:5로 섞여 있어 가장 불순한 상태 (최악)
    - 0.0: 한 클래스만 100% 모여 있는 상태 (순수 노드, Pure Node, 최상)

(3) 정보 이득 (Information Gain, 불순도 차이)
    정보 이득 = 부모 노드의 불순도 - (왼쪽 자식 불순도 * 왼쪽 비율 + 오른쪽 자식 불순도 * 오른쪽 비율)
    - 결정 트리는 자식 노드로 갈수록 불순도가 가장 많이 줄어들도록(정보 이득이 최대가 되도록)
      최적의 특성과 분할 임계값을 찾음.

(4) 엔트로피 (Entropy, criterion='entropy')
    - 지니 불순도 대신 밑이 2인 로그를 사용하는 엔트로피 불순도를 사용할 수도 있음.

##################################################################
3. 주요 특징: 특성 스케일링(전처리) 불필요
- 결정 트리는 특성의 대소 비교(예: sugar <= 4.325)를 통해 노드를 분할함.
- 따라서 데이터에 표준화(StandardScaler)나 정규화(MinMaxScaler)를 적용해도
  분할 기준점의 상대적 순서가 바뀌지 않으므로 모델의 훈련 결과와 성능이 완전히 동일함.
- 오히려 원본 데이터를 그대로 사용하면 분할 조건이 실제 단위(예: 당도 %, 알코올 도수)로 표시되어
  해석하기 훨씬 편리함.

##################################################################
4. 결정 트리의 장단점 및 과대적합 해결 방안
- 장점:
    - 결과가 직관적이며 시각화(plot_tree)를 통해 설명하기 쉬움
    - 특성 스케일링(표준화 등) 전처리가 불필요함
    - 이상치(Outlier)에 덜 민감하고 비선형 관계를 자연스럽게 포착함
    - 특성 중요도(feature_importances_)를 제공하여 중요한 변수를 쉽게 파악 가능
- 단점:
    - 트리가 너무 깊게 자라면 훈련 데이터의 사소한 노이즈까지 완벽하게 외워버리는
      심각한 과대적합(Overfitting)이 발생하기 쉬움
    - 데이터가 조금만 바뀌어도 트리의 구조가 크게 달라지는 불안정성이 있음
- 극복 방안: 가지치기(Pruning)
    - 트리가 무한정 깊어지지 않도록 하이퍼파라미터로 제어함
    - max_depth: 트리의 최대 깊이 제한
    - min_samples_split: 노드를 분할하기 위한 최소 샘플 수
    - min_samples_leaf: 리프 노드가 되기 위한 최소 샘플 수
    - min_impurity_decrease: 분할로 인해 감소해야 하는 최소 불순도 기준
"""

#%%
# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/05-1.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

#%%
# ## 로지스틱 회귀로 와인 분류하기

# In[1]:
# 판다스(Pandas) 라이브러리 임포트 및 원격 CSV 파일에서 와인 데이터 로드
import pandas as pd

# 레드와인과 화이트와인 데이터셋 (총 6,497개 샘플)
# wine = pd.read_csv('https://bit.ly/wine_csv_data')
wine = pd.read_csv('wine.csv')


# In[2]:
    
# 데이터프레임 처음 5개 행 확인
# 컬럼 구성:
# - alcohol: 알코올 도수
# - sugar: 당도
# - pH: 산도(pH 값)
# - class: 타깃값 (0.0: 레드와인 / 1.0: 화이트와인)
wine.head()

#%%

"""
   alcohol  sugar    pH  class
0      9.4    1.9  3.51    0.0
1      9.8    2.6  3.20    0.0
2      9.8    2.3  3.26    0.0
3      9.8    1.9  3.16    0.0
4      9.4    1.9  3.51    0.0
"""


# In[3]:
# 데이터프레임 요약 정보 출력
# 각 컬럼의 결측치(Non-Null Count) 여부와 데이터 타입(Dtype: float64) 확인
# 총 6,497개 샘플 모두 결측치 없이 채워져 있음
wine.info()

#%%

"""
RangeIndex: 6497 entries, 0 to 6496
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   alcohol  6497 non-null   float64
 1   sugar    6497 non-null   float64
 2   pH       6497 non-null   float64
 3   class    6497 non-null   float64
dtypes: float64(4)
memory usage: 203.2 KB
"""

# In[4]:
# 각 수치형 컬럼의 기술 통계량(개수, 평균, 표준편차, 사분위수, 최솟값, 최댓값) 확인
# 특성의 최소~최대값
# 알코올(8~14), 
# 당도(0.6~65.8), 
# pH(2.7~4.0)
# 각 특성마다 단위와 스케일(범위)이 크게 다름
wine.describe()

#%%

"""
           alcohol        sugar           pH        class
count  6497.000000  6497.000000  6497.000000  6497.000000
mean     10.491801     5.443235     3.218501     0.753886
std       1.192712     4.757804     0.160787     0.430779
min       8.000000     0.600000     2.720000     0.000000
25%       9.500000     1.800000     3.110000     1.000000
50%      10.300000     3.000000     3.210000     1.000000
75%      11.300000     8.100000     3.320000     1.000000
max      14.900000    65.800000     4.010000     1.000000
"""


# In[5]:
    
# 입력 특성(data)과 타깃 레이블(target) 분리
# - data: 독립변수 (알코올, 당도, pH) 3개 특성
# - target: 종속변수 (와인의 종류 class: 0=레드와인, 1=화이트와인)
data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']


# In[6]:
    
# 데이터를 훈련 세트(80%)와 테스트 세트(20%)로 분할
# test_size=0.2 : 테스트 세트 비율 20% 지정 (기본값은 0.25)
# random_state=42 : 난수 시드 고정으로 동일한 분할 결과 재현
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)


# In[7]:
    
# 분할된 훈련 세트와 테스트 세트의 형태(크기) 확인
# 전체 6,497개 중 훈련 세트 5,197개(80%), 테스트 세트 1,300개(20%)로 분할
print(train_input.shape, test_input.shape) # (5197, 3) (1300, 3)


# In[8]:
    
# 로지스틱 회귀와 같은 거리/기울기 기반 선형 모델 학습을 위해 표준화 전처리 진행
# StandardScaler: 각 특성의 평균을 0, 표준편차를 1로 맞추는 표준점수(Z-Score) 변환
# 주의: 반드시 훈련 세트의 평균과 표준편차(fit) 기준으로 테스트 세트도 변환(transform)해야 함
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)


# In[9]:
    
# 표준화된 데이터를 사용하여 로지스틱 회귀(LogisticRegression) 모델 훈련 및 평가
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(train_scaled, train_target)

# 정확도(Accuracy) 출력:
# 훈련 점수 약 0.7808 (78.1%), 테스트 점수 약 0.7777 (77.8%)
# 점수가 다소 낮아 두 세트 모두 과소적합(Underfitting) 경향을 보임
print(lr.score(train_scaled, train_target)) # 0.7808350971714451
print(lr.score(test_scaled, test_target))   # 0.7776923076923077

#%%

# ### 설명하기 쉬운 모델과 어려운 모델

# In[10]:
    
# 로지스틱 회귀가 학습한 선형 방정식의 계수(가중치)와 절편(바이어스) 확인
# 선형 방정식 형태: z = w1 * alcohol + w2 * sugar + w3 * pH + b
# 출력된 계수만으로는 "왜 이 값이 나와야 화이트와인인가?"를 직관적으로 설명하기 어려움
# 결과: [[ 0.51268071  1.67335441 -0.68775646]] [1.81773456]
print(lr.coef_, lr.intercept_)


#%%
# ## 결정 트리 (Decision Tree)

# In[11]:

# 결정트리분류 모델
# 사이킷런의 DecisionTreeClassifier를 사용하여 결정 트리 모델 훈련
# 기본 설정은 리프 노드가 완전히 순수해지거나 
# 샘플 수가 기준 이하가 될 때까지 끝없이 분기함
from sklearn.tree import DecisionTreeClassifier

# max_depth: 기본값 None
# 트리의 깊이에 제한을 두지 않고 무한정 분할
# 1. 모든 리프 노드가 완전히 순수해질 대까지(지니 불순도가 0.0이 될 때까지)
# 2. 노드 안의 샘플 수가 분할 최소 기준(min_sample_split, 기본값 2개) 미만이 될 때까지
dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_scaled, train_target)

# 정확도 평가:
# 훈련 세트 점수: 약 0.9969 (99.7%) -> 훈련 데이터를 거의 완벽하게 암기
# 테스트 세트 점수: 약 0.8592 (85.9%) -> 훈련 세트와의 격차가 큼
# 전형적인 과대적합(Overfitting) 상태임
print(dt.score(train_scaled, train_target)) # 0.996921300750433
print(dt.score(test_scaled, test_target))   # 0.8592307692307692

# 과대적합 해결방안: 가지치기

# In[12]:
    
# 훈련된 결정 트리의 전체 구조 시각화
# plot_tree() 함수를 사용하여 트리 분기 과정을 그래프로 출력
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(10,7))
plot_tree(dt)
# 트리가 너무 깊고 복잡하게 분기되어 사람이 규칙을 읽기 어려운 형태임을 보여줌
plt.show()


# In[13]:
    
# 가독성을 높이기 위해 트리의 최대 깊이를 1로 제한
# (루트 노드 + 자식 노드 1단계)하여 시각화
# 매개변수 설명:
# - max_depth=1: 루트 노드 아래로 1단계 깊이까지만 표시
# - filled=True: 클래스 비율에 따라 노드의 색상을 채움 (비율이 높을수록 색상이 진해짐)
# - feature_names: 각 특성의 실제 이름 지정 (분기 조건 가독성 향상)
plt.figure(figsize=(10,7))
plot_tree(dt, max_depth=1, filled=True,
          feature_names=['alcohol', 'sugar', 'pH'])
plt.show()

#%%

"""
[노드 상자(Box)에 표기된 정보 읽는 법]
1. 분기 조건 (예: sugar <= -0.239)
   - 만족(True)하면 왼쪽 자식 노드로 이동
   - 불만족(False)하면 오른쪽 자식 노드로 이동
2. gini (지니 불순도)
   - 0.0이면 완벽히 한 클래스만 모인 순수 노드
3. samples
   - 해당 노드에 포함된 총 샘플 수
4. value = [레드와인 개수, 화이트와인 개수]
   - 각 클래스별 샘플 수
     (음성 클래스: 0=레드와인, 양성 클래스: 1=화이트와인)
"""


#%%

# ### 가지치기 (Pruning)
# 트리가 무제한으로 깊어지는 것을 막아 과대적합을 해소하고 
# 일반화 성능을 높임

# In[14]:
    
# max_depth=3 으로 트리의 최대 깊이를 3으로 제한하는 
# 사전 가지치기(Pre-pruning) 적용
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(train_scaled, train_target)

# 가지치기 후 정확도 평가:
# 훈련 세트: 약 0.8455 (84.6%)
# 테스트 세트: 약 0.8415 (84.2%)
# 훈련 점수는 낮아졌으나 테스트 점수와 근접하여 과대적합이 성공적으로 해소됨
print(dt.score(train_scaled, train_target)) # 0.8454877814123533
print(dt.score(test_scaled, test_target))   # 0.8415384615384616


# In[15]:
    
# max_depth=3으로 가지치기된 트리 시각화
plt.figure(figsize=(20,15))
plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
plt.show()


#%%

# ### 특성 스케일링이 필요 없는 결정 트리
# 결정 트리는 데이터의 대소 관계만을 기준으로 분할하므로 특성 스케일링(표준화 등)에 영향을 받지 않음

# In[16]:
    
# 표준화되지 않은 원본 데이터(train_input, test_input)로 동일한 모델 훈련
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(train_input, train_target)

# 정확도 출력:
# 표준화 데이터를 사용했을 때(0.8455, 0.8415)와 소수점 끝자리까지 완전히 동일함
# 즉, 결정 트리는 전처리(StandardScaler)가 불필요함을 증명함
print(dt.score(train_input, train_target)) # 0.8454877814123533
print(dt.score(test_input, test_target))   # 0.8415384615384616


# In[17]:
    
# 원본 특성값으로 학습한 트리 시각화
# 노드의 분기 조건이 'sugar <= -0.239' 같은 표준점수 대신
# 'sugar <= 4.325' 처럼 직관적인 실제 당도(%) 단위로 표기되어 모델 해석이 훨씬 쉬워짐
plt.figure(figsize=(20,15))
plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
plt.show()


# In[18]:
    
# 각 특성이 트리의 불순도 감소에 기여한 정도를 나타내는 특성 중요도(Feature Importances) 확인
# 특성 순서: ['alcohol', 'sugar', 'pH']
# 결과: [0.1234, 0.8686, 0.0079] 
#       -> 당도(sugar) 중요도가 약 87%로 와인 분류에 가장 결정적인 특성임
# 모든 특성 중요도의 합은 항상 1
print(dt.feature_importances_) # [0.12345626 0.86862934 0.0079144 ]


#%%

# ## 확인문제 (min_impurity_decrease 하이퍼파라미터 활용)

# In[19]:
    
# min_impurity_decrease: 노드 분할 시 얻어지는 불순도 감소량(정보 이득)의 최소 기준값 설정
# 불순도 감소량이 0.0005 미만이면 더 이상 자식 노드로 분할하지 않고 중단함
# max_depth 외에도 이 기준으로 효과적인 가지치기가 가능함
dt = DecisionTreeClassifier(min_impurity_decrease=0.0005, random_state=42)
dt.fit(train_input, train_target)

# 평가 결과:
# 훈련 점수: 약 0.8874 (89.0%)
# 테스트 점수: 약 0.8615 (86.2%)
# max_depth=3 일 때(84.2%)보다 조금 더 세밀하게 분기되어 일반화 성능이 향상됨
print(dt.score(train_input, train_target)) # 0.8874350586877044
print(dt.score(test_input, test_target))   # 0.8615384615384616


# In[20]:
    
# min_impurity_decrease=0.0005 기준으로 가지치기된 트리 시각화
# 깊이가 적절히 제어되면서도 의미 있는 규칙들이 잘 형성됨을 확인
plt.figure(figsize=(20,15))
plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
plt.show()
