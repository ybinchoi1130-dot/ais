#!/usr/bin/env python
# coding: utf-8

# # 훈련 세트와 테스트 세트

# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/02-1.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# ## 훈련 세트와 테스트 세트

# In[1]:


fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 
               29.7, 29.7, 30.0, 30.0, 30.7, 
               31.0, 31.0, 31.5, 32.0, 32.0, 
               32.0, 33.0, 33.0, 33.5, 33.5, 
               34.0, 34.0, 34.5, 35.0, 35.0, 
               35.0, 35.0, 36.0, 36.0, 37.0, 
               38.5, 38.5, 39.5, 41.0, 41.0, # 도미(35개)
                9.8, 10.5, 10.6, 11.0, 11.2, # 빙어(14개)
                11.3, 11.8, 11.8, 12.0, 12.2, 
                12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 
               450.0, 500.0, 390.0, 450.0, 500.0, 
               475.0, 500.0, 500.0, 340.0, 600.0, 
               600.0, 700.0, 700.0, 610.0, 650.0, 
               575.0, 685.0, 620.0, 680.0, 700.0, 
               725.0, 720.0, 714.0, 850.0, 1000.0, 
               920.0, 955.0, 925.0, 975.0, 950.0, # 도미(35개)
                 6.7, 7.5,  7.0, 9.7, 9.8,        # 빙어(14개)
                 8.7, 10.0, 9.9, 9.8, 12.2, 
                 13.4, 12.2, 19.7, 19.9]


# In[2]:


fish_data = [[l, w] for l, w in zip(fish_length, fish_weight)]
fish_target = [1]*35 + [0]*14  # 도미(1) * 35, 빙어(0) * 14


# In[3]:


from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()


# In[4]:


print(fish_data[4])


# In[5]:


print(fish_data[0:5])


# In[6]:


print(fish_data[:5])


# In[7]:


print(fish_data[44:])


# In[8]:

# 훈련 데이터와 정답
train_input = fish_data[:35]
train_target = fish_target[:35]

# 테스트 데이터와 정답
test_input = fish_data[35:]
test_target = fish_target[35:]


# In[9]:


kn.fit(train_input, train_target)
train_score = kn.score(train_input, train_target)
test_score = kn.score(test_input, test_target)

# 테스트 데이터 점수가 0.0이 나온 이유?
# 훈련은 '도미' 데이터로 테스트는 '빙어'로 했기 때문에
print("훈련 데이터 점수:", train_score)  # 1.0
print("테스트 데이터 점수:", test_score) # 0.0


#%%
# ## 넘파이

# In[10]:


import numpy as np


# In[11]:

# 리스트 -> 넘파이 배열
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)


# In[12]:


print(input_arr)


# In[13]:


print(input_arr.shape) # (49, 2)


# In[14]:

# 0~48까지 49개의 숫자를 무작위로 섞음
np.random.seed(42)       # 난수 씨드 고정
index = np.arange(49)    # 1차원 배열 49개
np.random.shuffle(index) # 무작위로 섞음


# In[15]:


print(index)


# In[16]:

# 넘파이 배열에서 인덱스 1번째와 3번째에 해당하는 값을 2개를 출력
print(input_arr[[1,3]]) # [[ 26.3 290. ] [ 29.  363. ]]

# 개별 요소를 1개를 출력
print(input_arr[1])     # [ 26.3 290. ]
print(input_arr[3])     # [ 29.  363. ]
print(input_arr[[1]])   # [[ 26.3 290. ]] 2차원


# In[17]:

# 훈련 데이터 슬라이싱: 0~34
train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]


# In[18]:

# index의 0번째의 값 13에 의해서 
# train_input의 0번째로 이동
print(input_arr[13], train_input[0])


# In[19]:

# 테스트 데이터를 index를 기준으로 구성: 35~48 
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]


# In[20]:

import matplotlib.pyplot as plt

plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(test_input[:, 0], test_input[:, 1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


#%%

# ## 두 번째 머신러닝 프로그램

# In[21]:

# 새로 구성된 데이터로 훈련 수행
kn.fit(train_input, train_target)


# In[22]:

# 평가
new_score = kn.score(test_input, test_target)
print("새로 훈련한 모델로 평가:", new_score) # 1.0


# In[23]:

# 테스트 데이터로 예측
test_predict = kn.predict(test_input)
print(test_predict)

# In[24]:

# 테스트 데이터 정답
print(test_target)

#%%

# [문제]
# 테스트 예측(test_predict)과 
# 테스트 정답(test_target)을 zip으로 묶어서
# 같은지(True) 틀린지(False) 출력하라.
test_predict_target = list(zip(test_input, test_predict, test_target))
for n, val in enumerate(test_predict_target):
    print(f"[{n:2}] 정답({val[2]}): {val[1] == val[2]}, {val[0]}")

#%%

"""
[ 0] 정답(0): True, [10.6  7. ]
[ 1] 정답(0): True, [9.8 6.7]
[ 2] 정답(1): True, [ 35. 680.]
[ 3] 정답(0): True, [11.2  9.8]
[ 4] 정답(1): True, [ 31. 475.]
[ 5] 정답(1): True, [ 34.5 620. ]
[ 6] 정답(1): True, [ 33.5 610. ]
[ 7] 정답(0): True, [15.  19.9]
[ 8] 정답(1): True, [ 34. 575.]
[ 9] 정답(1): True, [ 30. 390.]
[10] 정답(0): True, [11.8  9.9]
[11] 정답(1): True, [ 32. 600.]
[12] 정답(1): True, [ 36. 850.]
[13] 정답(0): True, [11.   9.7]
"""

#%%

# 넘파이
import numpy as np

n03 = np.arange(3)    
n10 = np.arange(10)   
n05 = np.arange(5,10) 

print(type(n03), n03) # <class 'numpy.ndarray'> [0 1 2]
print(type(n10), n10) # <class 'numpy.ndarray'> [0 1 2 3 4 5 6 7 8 9]
print(type(n05), n05) # <class 'numpy.ndarray'> [5 6 7 8 9]

#%%

# 1부터 3까지 0.2씩 증가
# 값이 하나라도 실수(float)가 있으면 타입이 실수가 된다.
nf = np.arange(1, 3, 0.2)
print(type(nf)) # <class 'numpy.ndarray'>, float64
print(nf) # [1.  1.2 1.4 1.6 1.8 2.  2.2 2.4 2.6 2.8]

#%%

# 무작위로 섞기
lst = [[1,2], [3,4], [4,5]]
n2r = np.array(lst)
np.random.seed(44)     # 씨드 고정
np.random.shuffle(n2r) # 섞기
print(n2r) # [[4 5] [3 4] [1 2]]





