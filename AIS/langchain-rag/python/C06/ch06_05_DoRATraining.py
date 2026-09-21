#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install trl==0.13.0')
get_ipython().system('pip install datasets==3.2.0')
get_ipython().system('pip install -U bitsandbytes==0.45.0')
get_ipython().system('pip install git+https://github.com/huggingface/peft.git -q')


# In[ ]:


from datasets import load_dataset
from datasets import Dataset
from pprint import pprint
import transformers
from peft import prepare_model_for_kbit_training
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from tqdm import tqdm
import json
import pickle
import os
os.environ["WANDB_DISABLED"] = "true"


# In[ ]:


data_list = pickle.load(open('전자금융거래.pk', 'rb'))


# In[ ]:


model_id = "MLP-KTLim/llama-3-Korean-Bllossom-8B"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map={"":0})
model.gradient_checkpointing_enable()
model = prepare_model_for_kbit_training(model)


# In[ ]:


data = Dataset.from_list([{"text" : i} for i in data_list], split="train")

data = data.map(lambda samples: tokenizer(samples["text"]), batched=True)
data


# In[ ]:


from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=8,
    lora_alpha=32,  # LoRA 스케일링 계수로, 모델 학습 중 LoRA의 영향력을 조절
    lora_dropout=0.05,  # 드롭아웃 확률 설정
    bias="none",  # 바이어스 사용 설정 (여기서는 비활성화)
    use_dora=True,  # DoRA 학습을 활성화하는 옵션
    task_type="CAUSAL_LM"  # 생성 모델 학습을 지정
)

model = get_peft_model(model, config)


# In[ ]:


input_text = "전자지급수단이 뭐야?"
gened = model.generate(
      **tokenizer(
          input_text,
          return_tensors='pt',
          return_token_type_ids=False
      ).to(model.device),
      max_new_tokens=256,
      early_stopping=True,
      do_sample=True,
      eos_token_id=128001,
)


# In[ ]:


print(tokenizer.decode(gened[0]))


# In[ ]:


tokenizer.pad_token = tokenizer.eos_token
data_len = data.num_rows

trainer = transformers.Trainer(
    model=model,
    train_dataset=data,
    args=transformers.TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=1,
        warmup_steps=200,
        num_train_epochs = 3,
        # max_steps= int(data_len/batch_size) , # 1 epoch 만 학습
        learning_rate=1e-4,
        fp16=True,
        logging_steps=10,
        output_dir="qlora_output",
        optim="paged_adamw_8bit"
    ),
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False),
)
model.config.use_cache = False  # silence the warnings. Please re-enable for inference!
trainer.train()

model_to_save = trainer.model.module if hasattr(trainer.model, 'module') else trainer.model  # Take care of distributed/parallel training
model_to_save.save_pretrained("outputs")


# In[ ]:


input_text = "전자지급수단이 뭐야?"
gened = model.generate(
      **tokenizer(
          input_text,
          return_tensors='pt',
          return_token_type_ids=False
      ).to(model.device),
      max_new_tokens=256,
      early_stopping=True,
      do_sample=True,
      eos_token_id=128001,
)


# In[ ]:


print(tokenizer.decode(gened[0]))


# 
