#!/usr/bin/env python
# coding: utf-8

# # 신경망 모델 훈련

# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/07-3.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# In[1]:


# 실행마다 동일한 결과를 얻기 위해 케라스에 랜덤 시드를 사용하고 텐서플로 연산을 결정적으로 만듭니다.
import keras
import tensorflow as tf

keras.utils.set_random_seed(42)
tf.random.set_seed(42)
tf.config.experimental.enable_op_determinism()


# ## 손실 곡선

# In[2]:


import keras
from sklearn.model_selection import train_test_split

(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

train_scaled = train_input / 255.0

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)


# In[3]:


def model_fn(a_layer=None):
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=(28,28))) # 입력층
    model.add(keras.layers.Flatten())            # 평탄화
    model.add(keras.layers.Dense(100, activation='relu'))
    if a_layer: # 레이어 추가
        model.add(a_layer)
    model.add(keras.layers.Dense(10, activation='softmax')) # 출력층
    return model


# In[4]:


model = model_fn()
model.summary()


# In[5]:

# verbose=0: 진행상황이 보이지 않음
model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_scaled, train_target, epochs=5, verbose=0)


# In[6]:

print(history.history.keys()) # dict_keys(['accuracy', 'loss'])


# In[7]:


import matplotlib.pyplot as plt

plt.plot(history.history['loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()


# In[8]:


plt.plot(history.history['accuracy'])
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()


# In[9]:


model = model_fn()
model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_scaled, train_target, epochs=20, verbose=0)


# In[10]:


plt.plot(history.history['loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()


# ## 검증 손실

# In[11]:


model = model_fn()
model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_scaled, train_target, epochs=20, verbose=0,
                    validation_data=(val_scaled, val_target))


# In[12]:


print(history.history.keys())


# In[13]:


plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()


# In[14]:


model = model_fn()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(train_scaled, train_target, epochs=20, verbose=0,
                    validation_data=(val_scaled, val_target))


# In[15]:


plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()


# ## 드롭아웃

# In[16]:


model = model_fn(keras.layers.Dropout(0.3))
model.summary()


# In[17]:


model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(train_scaled, train_target, epochs=20, verbose=0,
                    validation_data=(val_scaled, val_target))


# In[18]:


plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()


# ## 모델 저장과 복원

# In[19]:


model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(train_scaled, train_target, epochs=11, verbose=0,
                    validation_data=(val_scaled, val_target))


# In[20]:


model.save('model-whole.keras')


# In[21]:


model.save_weights('model.weights.h5')


# In[22]:


get_ipython().system('ls -al model*')


# In[23]:


model = model_fn(keras.layers.Dropout(0.3))
model.load_weights('model.weights.h5')


# In[24]:


import numpy as np

val_labels = np.argmax(model.predict(val_scaled), axis=-1)
print(np.mean(val_labels == val_target))


# In[25]:


model = keras.models.load_model('model-whole.keras')
model.evaluate(val_scaled, val_target)


# ## 콜백

# In[26]:


model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.keras',
                                                save_best_only=True)
model.fit(train_scaled, train_target, epochs=20, verbose=0,
          validation_data=(val_scaled, val_target),
          callbacks=[checkpoint_cb])


# In[27]:

# 저장된 모델 로딩
model = keras.models.load_model('best-model.keras')
model.evaluate(val_scaled, val_target) # [0.32417261600494385, 0.8845000267028809]


# In[28]:

# 최적의 에포크 횟수를 찾아서 훈련된 모델을 저장('best-model.keras')
model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.keras',
                                                save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
                                                  restore_best_weights=True)
history = model.fit(train_scaled, train_target, epochs=20, verbose=1,
                    validation_data=(val_scaled, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])


# In[29]:


print(early_stopping_cb.stopped_epoch) # 14회


# In[30]:


plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()


# In[31]:


model.evaluate(val_scaled, val_target) # [0.32121017575263977, 0.8803333044052124]

#%%

# 예측?
test_scaled = test_input / 255.0
test_loss, test_acc = model.evaluate(test_scaled, test_target)
print(f"테스트 세트 손실: {test_loss:.4f}, 정확도: {test_acc:.4f}")
# 테스트 세트 손실: 0.3542, 정확도: 0.8754

#%%
preds = model.predict(test_scaled)

# 예측한 결과 데이터에서 가장 높은 확률값을 가진 위치를 인덱스(0~9)를 반환
pred_labels = np.argmax(preds, axis=-1)
print("테스트 세트 정확도:", np.mean(pred_labels == test_target))
# 테스트 세트 정확도: 0.8754

#%%

print("처음 10개 샘플 예측값:", pred_labels[:10])
print("처음 10개 샘플 실제값:", test_target[:10])

# 처음 10개 샘플 예측값: [9 2 1 1 6 1 4 6 5 7]
# 처음 10개 샘플 실제값: [9 2 1 1 6 1 4 6 5 7]

#%%




