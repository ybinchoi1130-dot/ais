#!/usr/bin/env python
# coding: utf-8

# # 심층 신경망

# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/07-2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# In[1]:


# 실행마다 동일한 결과를 얻기 위해 케라스에 랜덤 시드를 사용하고 
# 텐서플로 연산을 결정적으로 만듭니다.
import keras
import tensorflow as tf

keras.utils.set_random_seed(42)
tf.config.experimental.enable_op_determinism()


# ## 2개의 층

# In[2]:


import keras

(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()


# In[3]:


# 스케일
from sklearn.model_selection import train_test_split

train_scaled = train_input / 255.0
train_scaled = train_scaled.reshape(-1, 28*28)

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)


# In[4]:

# 입력축, 은닉층, 출력층
inputs = keras.layers.Input(shape=(784,))
dense1 = keras.layers.Dense(100, activation='sigmoid')
dense2 = keras.layers.Dense(10, activation='softmax')


# ## 심층 신경망 만들기

# In[5]:


model = keras.Sequential([inputs, dense1, dense2])


# In[6]:


model.summary()


#%%
# ## 층을 추가하는 다른 방법

# In[7]:


model = keras.Sequential([
    keras.layers.Input(shape=(784,)),
    keras.layers.Dense(100, activation='sigmoid', name='은닉층'),
    keras.layers.Dense(10, activation='softmax', name='출력층')
], name='패션 MNIST 모델')


# In[8]:


model.summary()


# In[9]:

# 모델의 메서드를 이용해서 하나씩 레이어를 추가
model = keras.Sequential()
model.add(keras.layers.Input(shape=(784,)))
model.add(keras.layers.Dense(100, activation='sigmoid'))
model.add(keras.layers.Dense(10, activation='softmax'))


# In[10]:


model.summary()


# In[11]:


model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_scaled, train_target, epochs=5)


# ## 렐루 활성화 함수

# In[12]:


model = keras.Sequential()
model.add(keras.layers.Input(shape=(28,28)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))


# In[13]:


model.summary()


# In[14]:


(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()
train_scaled = train_input / 255.0
train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)


# In[15]:


model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_scaled, train_target, epochs=5)


# In[16]:


model.evaluate(val_scaled, val_target)
# [0.3841075897216797, 0.8658333420753479]

#%%

# ## 옵티마이저

# In[17]:


model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# In[18]:


sgd = keras.optimizers.SGD()
model.compile(optimizer=sgd, loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# In[19]:


sgd = keras.optimizers.SGD(learning_rate=0.1)


# In[20]:


sgd = keras.optimizers.SGD(momentum=0.9, nesterov=True)


# In[21]:


adagrad = keras.optimizers.Adagrad()
model.compile(optimizer=adagrad, loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# In[22]:


rmsprop = keras.optimizers.RMSprop()
model.compile(optimizer=rmsprop, loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# In[23]:


model = keras.Sequential()
model.add(keras.layers.Input(shape=(28,28)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))


# In[24]:


model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_scaled, train_target, epochs=5)


# In[25]:


model.evaluate(val_scaled, val_target)
# [0.35866573452949524, 0.8689166903495789]
