#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 필요한 라이브러리를 설치합니다.
get_ipython().system('pip install datasets==3.2.0 # 데이터셋 로드 및 처리 라이브러리')
get_ipython().system('pip install trl==0.13.0  # Transformer 모델을 위한 강화 학습 라이브러리')
get_ipython().system('pip install peft==1.26.4  # 파라미터 효율적인 미세 조정을 위한 라이브러리')
get_ipython().system('pip install -U bitsandbytes==0.45.0  # 양자화 및 메모리 효율성을 위한 라이브러리')


# In[ ]:


# 필요한 모듈을 임포트합니다.
from datasets import load_dataset, Dataset
from pprint import pprint
import transformers
from peft import prepare_model_for_kbit_training
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from tqdm import tqdm
import json
import pickle
from peft import LoraConfig, get_peft_model
import os
os.environ["WANDB_DISABLED"] = "true"


# In[ ]:


# pickle 모듈을 사용하여 청킹한 “전자금융거래.pk” 바이너리 파일 데이터를 불러옵니다.
data_list = pickle.load(open('전자금융거래.pk', 'rb'))


# In[ ]:


# 사용할 사전 학습된 모델의 ID를 지정합니다.
model_id = "MLP-KTLim/llama-3-Korean-Bllossom-8B"

# BitsAndBytesConfig를 사용하여 4-bit 양자화 설정을 구성합니다.
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

# 토크나이저와 모델을 불러옵니다.
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map={"": 0})

# 모델의 기울기 체크포인팅을 활성화하여 메모리 사용을 줄입니다.
model.gradient_checkpointing_enable()

# 모델을 K-bit 양자화 훈련에 적합하도록 준비합니다.
model = prepare_model_for_kbit_training(model)


# In[ ]:


# 불러온 데이터 리스트를 기반으로 데이터셋 객체를 생성하고 텍스트 데이터를 토큰화 합니다.
data = Dataset.from_list([{"text": i} for i in data_list], split="train")
data = data.map(lambda samples: tokenizer(samples["text"]), batched=True)


# In[ ]:


# LoraConfig를 사용하여 LoRA 설정을 구성합니다.
config = LoraConfig(
    r=8,
    lora_alpha=32,  # LoRA 스케일링
    lora_dropout=0.05,  # 드롭아웃 비율
    bias="none",
    task_type="CAUSAL_LM"  # 생성 모델 학습 유형으로 지정
)

# 설정된 LoRA 구성을 사용하여 모델을 PEFT 모델로 변환합니다.
model = get_peft_model(model, config)


# In[ ]:


# 학습 전 모델 테스트를 위해 입력 텍스트를 생성해 결과를 확인합니다.
input_text = "전자지급수단이 뭐야?"
gened = model.generate(
      **tokenizer(input_text, return_tensors='pt', return_token_type_ids=False).to(model.device),
      max_new_tokens=128,
      early_stopping=True,
      do_sample=True,
      eos_token_id=2,
)
print(tokenizer.decode(gened[0]))


# In[ ]:


print(tokenizer.decode(gened[0]))


# In[ ]:


# 패딩 토큰을 엔드 오브 시퀀스(end-of-sequence) 토큰으로 설정
tokenizer.pad_token = tokenizer.eos_token

# 데이터셋의 총 행(row) 수를 계산하여 data_len 변수에 저장
data_len = data.num_rows

# Trainer 클래스를 사용하여 모델 학습을 설정
trainer = transformers.Trainer(
    model=model,
    train_dataset=data,
    args=transformers.TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=1,
        warmup_steps=200,
        num_train_epochs=3,
        learning_rate=1e-4,
        fp16=True,
        logging_steps=10,
        output_dir="qlora_output",
        optim="paged_adamw_8bit"
    ),
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False),
)

# 학습 중 메모리 사용량을 최적화하기 위해 캐시 기능을 비활성화
model.config.use_cache = False
trainer.train()  # 설정된 인자와 함께 학습을 시작


model_to_save = trainer.model.module if hasattr(trainer.model, 'module') else trainer.model  # Take care of distributed/parallel training
model_to_save.save_pretrained("outputs")


# In[ ]:


# 학습 후 입력 텍스트로 다시 텍스트 생성을 수행하여 결과를 확인
input_text = "전자지급수단이 뭐야?"
gened = model.generate(
      **tokenizer(input_text, return_tensors='pt', return_token_type_ids=False).to(model.device),
      max_new_tokens=256,
      early_stopping=True,
      do_sample=True,
      eos_token_id=128001,
)


# In[ ]:


print(tokenizer.decode(gened[0]))


# 
