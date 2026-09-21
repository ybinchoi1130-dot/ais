#!/usr/bin/env python
# coding: utf-8

# # 선형 회귀(LinearRegression)


# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/03-2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# ## k-최근접 이웃의 한계

# In[1]:


import numpy as np

# 농어의 길이: 훈련
perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )

# 농어의 무게: 타깃
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )


# In[2]:


from sklearn.model_selection import train_test_split

# 훈련 세트와 테스트 세트로 나눕니다
train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state=42)
# 훈련 세트와 테스트 세트를 2차원 배열로 바꿉니다
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)


# In[3]:


from sklearn.neighbors import KNeighborsRegressor

knr = KNeighborsRegressor(n_neighbors=3)
# k-최근접 이웃 회귀 모델을 훈련합니다
knr.fit(train_input, train_target)


# In[4]:


print(knr.predict([[50]]))


# In[5]:


import matplotlib.pyplot as plt


# In[6]:


# 50cm 농어의 이웃을 구합니다
distances, indexes = knr.kneighbors([[50]])

# 훈련 세트의 산점도를 그립니다
plt.scatter(train_input, train_target)
# 훈련 세트 중에서 이웃 샘플만 다시 그립니다
plt.scatter(train_input[indexes], train_target[indexes], marker='D')
# 50cm 농어 데이터
plt.scatter(50, 1033, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[7]:


print(np.mean(train_target[indexes]))


# In[8]:


print(knr.predict([[100]]))



# In[9]:


# 100cm 농어의 이웃을 구합니다
distances, indexes = knr.kneighbors([[100]])

# 훈련 세트의 산점도를 그립니다
plt.scatter(train_input, train_target)
# 훈련 세트 중에서 이웃 샘플만 다시 그립니다
plt.scatter(train_input[indexes], train_target[indexes], marker='D')
# 100cm 농어 데이터
plt.scatter(100, 1033, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# ## 선형 회귀

# In[10]:


from sklearn.linear_model import LinearRegression


# In[11]:


lr = LinearRegression()
# 선형 회귀 모델 훈련
lr.fit(train_input, train_target)


# In[12]:


# 50cm 농어에 대한 예측
print(lr.predict([[50]]))


# In[13]:


# 계수와 절편 확인
"""
LinearRegression 모델에서 lr.coef_와 lr.intercept_는 훈련 세트를 통해 모델이 학습해 찾아낸 1차 직선 방정식의 핵심 파라미터
1. lr.coef_ (계수, 기울기 / Slope, Weight)
    - 수학적 의미: 직선의 기울기(Slope)
    - 물리적 의미: 특성값(농어 길이)이 1단위(1cm) 증가할 때 타깃값(무게)이 평균적으로 몇 g 증가하는지를 나타냄
    - 특징: 특성(Feature)이 여러 개(다중 선형 회귀)일 경우 각 특성에 대응되는 계수들이 배열(ndarray) 형태로 담김
2. lr.intercept_ (절편 / Intercept)
    - 수학적 의미: 직선이 y축과 만나는 지점
    - 물리적 의미: 특성값(농어 길이)이 0일 때의 예측값(무게). 
        이론적으로 농어의 길이가 0이면 무게도 0이므로, 
        실제 농어 데이터에서는 이 값이 큰 의미가 없을 수 있음
    - NOTE: 실제 농어 길이가 0cm일 때 무게가 음수가 나올 수도 있는데, 
        이는 선형 모델이 데이터의 경향성을 직선으로 단순화했기 때문에 발생하는 통계적 절편값
3. 모델 파라미터 (Model Parameter)
    사용자가 직접 정해주는 k값 같은 값은 하이퍼파라미터(Hyperparameter)라고 부름
    반면 coef_와 intercept_처럼 데이터를 바탕으로 모델이 훈련(fit)을 통해 스스로 찾아낸 값을 모델 파라미터라고 부름
4. 이름 끝의 언더바(_)
    scikit-learn에서는 모델 훈련 전에는 없다가, 훈련(fit)이 완료된 후에 계산되어 생성된 속성 이름 뒤에 언더바(_)를 붙이는 명명 규칙이 있음
"""
print(lr.coef_, lr.intercept_)


# In[14]:


# 훈련 세트의 산점도를 그립니다
plt.scatter(train_input, train_target)
# 15에서 50까지 1차 방정식 그래프를 그립니다
plt.plot([15, 50], [15*lr.coef_+lr.intercept_, 50*lr.coef_+lr.intercept_])
# 50cm 농어 데이터
plt.scatter(50, 1241.8, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[15]:


print(lr.score(train_input, train_target))
print(lr.score(test_input, test_target))


# ## 다항 회귀

# In[16]:


train_poly = np.column_stack((train_input ** 2, train_input))
test_poly = np.column_stack((test_input ** 2, test_input))


# In[17]:


print(train_poly.shape, test_poly.shape)


# In[18]:


lr = LinearRegression()
lr.fit(train_poly, train_target)

print(lr.predict([[50**2, 50]]))


# In[19]:


print(lr.coef_, lr.intercept_)


# In[20]:


# 구간별 직선을 그리기 위해 15에서 49까지 정수 배열을 만듭니다
point = np.arange(15, 50)
# 훈련 세트의 산점도를 그립니다
plt.scatter(train_input, train_target)
# 15에서 49까지 2차 방정식 그래프를 그립니다
plt.plot(point, 1.01*point**2 - 21.6*point + 116.05)
# 50cm 농어 데이터
plt.scatter([50], [1574], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[21]:


print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))

