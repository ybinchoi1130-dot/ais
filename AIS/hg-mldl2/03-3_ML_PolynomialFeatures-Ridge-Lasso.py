#!/usr/bin/env python
# coding: utf-8

# # 특성 공학과 규제(PolynomialFeatures, Ridge, Lasso)
# PolynomialFeatures: 특성 공학. 주어진 특성을 조합하여 새로운 특성을 만드는 일련의 작업 과정

# Ridge: 규제(L2). 규제의 강도(alpha)를 조절하여 계수를 제한
#        규제가 있는 선형 회귀 모델 중 하나이며 선형 모델의 계수를 작게 만들어 과대적합을 완화
#        릿지는 비교적 효과가 좋아 널리 사용하는 규제 방법
# Lasso: 규제(L1). 계수를 0으로 만들어 특성을 선택하는 효과도 있음
#        또 다른 규제가 있는 선형 회귀 모델
#        릿지와 달리 계수 값을 아예 0으로 만들 수 있음

# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/03-3.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# ## 데이터 준비

# In[1]:


import pandas as pd


# In[2]:


perch_full = pd.read_csv('https://bit.ly/perch_csv_data')
perch_full.head()


# In[3]:


import numpy as np

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )


# In[4]:


from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state=42)


# ## 사이킷런의 변환기

# In[5]:


from sklearn.preprocessing import PolynomialFeatures


# In[6]:


poly = PolynomialFeatures()
poly.fit([[2, 3]])
print(poly.transform([[2, 3]]))


# In[7]:


poly = PolynomialFeatures(include_bias=False)
poly.fit([[2, 3]])
print(poly.transform([[2, 3]]))


# In[8]:


poly = PolynomialFeatures(include_bias=False)

poly.fit(train_input)
train_poly = poly.transform(train_input)


# In[9]:


print(train_poly.shape)


# In[10]:


poly.get_feature_names_out()


# In[11]:


test_poly = poly.transform(test_input)


# ## 다중 회귀 모델 훈련하기

# In[12]:


from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(train_poly, train_target)
print(lr.score(train_poly, train_target))


# In[13]:


print(lr.score(test_poly, test_target))


# In[14]:


poly = PolynomialFeatures(degree=5, include_bias=False)

poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)


# In[15]:


print(train_poly.shape)


# In[16]:


lr.fit(train_poly, train_target)
print(lr.score(train_poly, train_target))


# In[17]:


print(lr.score(test_poly, test_target))


# ## 규제

# In[18]:


from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_poly)

train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)


# ## 릿지

# In[19]:


from sklearn.linear_model import Ridge

ridge = Ridge()
ridge.fit(train_scaled, train_target)
print(ridge.score(train_scaled, train_target))


# In[20]:


print(ridge.score(test_scaled, test_target))


# In[21]:


import matplotlib.pyplot as plt

train_score = []
test_score = []


# In[22]:


alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
    # 릿지 모델을 만듭니다
    ridge = Ridge(alpha=alpha)
    # 릿지 모델을 훈련합니다
    ridge.fit(train_scaled, train_target)
    # 훈련 점수와 테스트 점수를 저장합니다
    train_score.append(ridge.score(train_scaled, train_target))
    test_score.append(ridge.score(test_scaled, test_target))


# In[23]:


plt.plot(alpha_list, train_score)
plt.plot(alpha_list, test_score)
plt.xscale('log')
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()


# In[24]:


ridge = Ridge(alpha=0.1)
ridge.fit(train_scaled, train_target)

print(ridge.score(train_scaled, train_target))
print(ridge.score(test_scaled, test_target))


# ## 라쏘

# In[25]:


from sklearn.linear_model import Lasso

lasso = Lasso()
lasso.fit(train_scaled, train_target)
print(lasso.score(train_scaled, train_target))


# In[26]:


print(lasso.score(test_scaled, test_target))


# In[27]:


train_score = []
test_score = []

alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
    # 라쏘 모델을 만듭니다
    lasso = Lasso(alpha=alpha, max_iter=10000)
    # 라쏘 모델을 훈련합니다
    lasso.fit(train_scaled, train_target)
    # 훈련 점수와 테스트 점수를 저장합니다
    train_score.append(lasso.score(train_scaled, train_target))
    test_score.append(lasso.score(test_scaled, test_target))


# In[28]:


plt.plot(alpha_list, train_score)
plt.plot(alpha_list, test_score)
plt.xscale('log')
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()


# In[29]:


lasso = Lasso(alpha=10)
lasso.fit(train_scaled, train_target)

print(lasso.score(train_scaled, train_target))
print(lasso.score(test_scaled, test_target))


# In[30]:


print(np.sum(lasso.coef_ == 0))

