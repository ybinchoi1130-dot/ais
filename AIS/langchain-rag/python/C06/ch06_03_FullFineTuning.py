#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('nviida-smi')


# In[ ]:


# datasets 라이브러리를 설치합니다. 다양한 데이터셋을 쉽게 로드하고 처리할 수 있는 도구를 제공합니다.
get_ipython().system('pip install datasets==3.2.0')
# 트랜스포머 모델에 강화 학습 기법을 적용하는 trl(Transformers Reinforcement Learning) 라이브러리를 설치합니다.
get_ipython().system('pip install trl==0.13.0')


# In[ ]:


import os
# nvidia-smi 명령어를 통해 확인한 GPU 중 학습에 필요한 GPU를 선택합니다.
os.environ["CUDA_VISIBLE_DEVICES"]="0,1,2,3,4"


# In[ ]:


from datasets import load_dataset
from datasets import Dataset
import transformers
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import json
import pickle
from trl import SFTTrainer
from accelerate import FullyShardedDataParallelPlugin as FSDP, Accelerator
from torch.distributed.fsdp.fully_sharded_data_parallel import FullOptimStateDictConfig, FullStateDictConfig


# In[ ]:


# 텍스트 청크로 저장된 데이터 파일인 전자금융거래.pk 파일에서 데이터를 로드합니다.
data_list = pickle.load(open('전자금융거래.pk', 'rb'))


# In[ ]:


# 학습에 사용할 모델 ID를 지정하여 언어 모델을 불러옵니다.
# device_map="auto"를 사용해 모델이 자동으로 여러 GPU에 분산되어 로드되도록 합니다.
model_id = "MLP-KTLim/llama-3-Korean-Bllossom-8B"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)


# In[ ]:


# 로드된 데이터 리스트를 기반으로 데이터셋 객체를 생성합니다.
# 각 텍스트 청크는 딕셔너리 형태로 변환되며, "train" 데이터셋으로 지정됩니다.
data = Dataset.from_list([{"text": i} for i in data_list], split="train")

# 텍스트 데이터를 토큰화하여 모델 입력에 맞는 형식으로 변환합니다. 이 과정은 배치 단위로 처리됩니다.
data = data.map(lambda samples: tokenizer(samples["text"]), batched=True)


# In[ ]:


# FSDP(Fully Sharded Data Parallel) 플러그인을 설정하여 혼합 정밀도 정책(fp16)과 CPU 오프로딩을 활성화합니다.
# 모델 학습 시 메모리 사용량을 최적화합니다.
fsdp_plugin = FSDP(
    mixed_precision_policy='fp16',
    cpu_offload=True
)


# In[ ]:


# 패딩 토큰을 시퀀스 종료(end-of-sequence) 토큰으로 설정합니다.
# 이는 패딩이 필요할 때 시퀀스 종료 토큰을 사용하게 합니다.
tokenizer.pad_token = tokenizer.eos_token

# 데이터셋의 총 행(row) 수를 계산하여 data_len 변수에 저장합니다.
# 이는 데이터의 크기를 추적하는 데 사용됩니다.
data_len = data.num_rows

# 배치 크기를 4로 설정합니다. 배치 크기는 한 번에 학습에 사용할 데이터 샘플의 수를 의미합니다.
batch_size = 4

# 학습 결과를 저장할 디렉토리 경로를 설정합니다.
output_path = "fft_model_save"

# SFTTrainer 클래스를 초기화합니다. 이 클래스는 사전학습된 모델에 맞춤 학습을 수행하는 데 사용됩니다.
trainer = SFTTrainer(
    model=model,
    train_dataset=data,
    args=transformers.TrainingArguments(
        # 학습을 제어하는 다양한 인자를 설정합니다.
        per_device_train_batch_size=batch_size,  # 각 GPU에서의 배치 크기
        gradient_accumulation_steps=4,  # 경사 하강법을 수행하기 전에 쌓을 기울기의 수를 4로 설정
        warmup_steps=100,  # 학습 초기 단계에서 학습률을 서서히 증가시키는 워밍업 스텝 수
        num_train_epochs=1,  # 학습할 총 에폭 수를 1로 설정
        learning_rate=2e-4,  # 학습률을 0.0002로 설정
        fp16=True,  # 혼합 정밀도(FP16) 학습을 활성화하여 학습 속도를 높이고 메모리 사용량을 줄임
        logging_steps=10,  # 로그를 기록할 간격을 10 스텝으로 설정
        output_dir=output_path,  # 학습된 모델과 관련 파일들이 저장될 디렉토리를 설정
    )
)

# 설정된 인자와 함께 학습을 시작합니다.
trainer.train()

