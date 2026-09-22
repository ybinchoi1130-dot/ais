#!/usr/bin/env python
# coding: utf-8

# # 심층 신경망 (파이토치)

# <table align="left"><tr><td>
# <a href="https://colab.research.google.com/github/rickiepark/hg-mldl2/blob/main/07-2.pytorch.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="코랩에서 실행하기"/></a>
# </td></tr></table>

# In[1]:


# 실행마다 동일한 결과를 얻기 위해 파이토치에 랜덤 시드를 지정하고 GPU 연산을 결정적으로 만듭니다.
import torch

torch.manual_seed(42)
if torch.cuda.is_available():
    torch.cuda.manual_seed(42)
    torch.backends.cudnn.deterministic = True


# In[2]:


from torchvision.datasets import FashionMNIST

fm_train = FashionMNIST(root='.', train=True, download=True)
fm_test = FashionMNIST(root='.', train=False, download=True)


# In[3]:


type(fm_train.data)


# In[4]:


print(fm_train.data.shape, fm_test.data.shape)


# In[5]:


print(fm_train.targets.shape, fm_test.targets.shape)


# In[6]:


train_input = fm_train.data
train_target = fm_train.targets


# In[7]:


train_scaled = train_input / 255.0


# In[8]:


from sklearn.model_selection import train_test_split

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)


# In[9]:


print(train_scaled.shape, val_scaled.shape)


# In[10]:


import torch.nn as nn

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 100),
    nn.ReLU(),
    nn.Linear(100, 10)
)


# In[11]:


# get_ipython().system('pip install torchinfo')


# In[12]:


from torchinfo import summary

summary(model, input_size=(32, 28, 28))


# In[13]:


import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


# In[14]:


import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters())


# In[15]:


for params in model.parameters():
    print(params.shape)


# In[16]:


epochs = 5
batches = int(len(train_scaled)/32)
for epoch in range(epochs):
    model.train()
    train_loss = 0
    for i in range(batches):
        inputs = train_scaled[i*32:(i+1)*32].to(device)
        targets = train_target[i*32:(i+1)*32].to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
    print(f"에포크:{epoch + 1}, 손실:{train_loss/batches:.4f}")


# In[17]:


model.eval()
with torch.no_grad():
    val_scaled = val_scaled.to(device)
    val_target = val_target.to(device)
    outputs = model(val_scaled)
    predicts = torch.argmax(outputs, 1)
    corrects = (predicts == val_target).sum().item()

accuracy = corrects / len(val_target)
print(f"검증 정확도: {accuracy:.4f}")

