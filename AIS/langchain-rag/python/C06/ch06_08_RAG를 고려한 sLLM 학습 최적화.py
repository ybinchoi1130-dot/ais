#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install trl==0.13.0')
get_ipython().system('pip install datasets==3.2.0')
get_ipython().system('pip install -U bitsandbytes==0.45.0')
get_ipython().system('pip install peft==1.26.4')


# In[ ]:


from datasets import Dataset
import transformers
from peft import prepare_model_for_kbit_training
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import pickle
import random
import os
os.environ["WANDB_DISABLED"] = "true"


# In[ ]:


data_list = pickle.load(open('qa_data.pkl', 'rb'))


# In[ ]:


model_id = "aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored"

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


# 학습 스크립트 형식을 정의
# 각 질문에 대해 두 개의 문서와 답변 형식을 포함
script_format = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

너는 제공된 문서를 참조하여 답변을 하는 사람이야.
답변을 위해 참조한 문서의 번호를 답변 마지막에 번호를 붙여줘
1번 문서를 참조한 경우 답변 마지막에 "[1]"을 추가해줘 <|eot_id|><|start_header_id|>user<|end_header_id|>
- 문서 1
{doc_1}
- 문서 2
{doc_2}

질문 : {q}[{number}]
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
답변 : {a} <|eot_id|>
"""


# In[ ]:


# 네거티브 샘플링을 적용한 데이터 생성 함수
def create_rag_data_with_negative_sampling(data_list):
    rag_data = []

    for data in data_list:
        q = data['question']
        a = data['answer']
        correct_doc = data['chunk']

        # 정답 문서를 제외한 네거티브 샘플링 문서를 1개 선택
        negative_samples = random.sample([d['chunk'] for d in data_list if d['chunk'] != correct_doc], 1)

        # 문서를 무작위로 배치
        documents = [correct_doc] + negative_samples
        random.shuffle(documents)

        # 정답 문서의 위치 (1, 2 중 하나)
        correct_doc_position = documents.index(correct_doc) + 1

        # script 생성
        script = script_format.format(
            doc_1=documents[0],
            doc_2=documents[1],
            q=q,
            a=a,
            number = correct_doc_position
        )

        # 각 데이터를 저장
        rag_data.append({
            'script': script,
            'correct_doc_position': correct_doc_position
        })

    return rag_data


# In[ ]:


# RAG 학습 데이터를 생성합니다.
rag_data_with_negatives = create_rag_data_with_negative_sampling(data_list)


# In[ ]:


data = Dataset.from_list([{"text" : i['script']} for i in rag_data_with_negatives], split="train")

data = data.map(lambda samples: tokenizer(samples["text"]), batched=True)
data


# In[ ]:


from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=8,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, config)


# In[ ]:


test_script = rag_data_with_negatives[5]['script'].split('답변 : ')[0]
test_script_answer = rag_data_with_negatives[5]['script'].split('ssistant<|end_header_id|>\n')[1]

gened = model.generate(
      **tokenizer(
          test_script,
          return_tensors='pt',
          return_token_type_ids=False
      ).to(model.device),
      max_new_tokens=256,
      early_stopping=True,
      do_sample=True,
      eos_token_id=[128001,128009],
)


# In[ ]:


print(test_script)


# In[ ]:


print(' -- 모델 답변')
print(tokenizer.decode(gened[0]).split('<|start_header_id|>assistant<|end_header_id|>\n')[1])
print(' -- 정답 답변')
print(test_script_answer)


# In[ ]:


tokenizer.pad_token = tokenizer.eos_token
data_len = data.num_rows

trainer = transformers.Trainer(
    model=model,
    train_dataset=data,
    args=transformers.TrainingArguments(
        per_device_train_batch_size=1,
        gradient_accumulation_steps=1,
        warmup_steps=200,
        num_train_epochs = 1,
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


gened = model.generate(
      **tokenizer(
          test_script,
          return_tensors='pt',
          return_token_type_ids=False
      ).to(model.device),
      max_new_tokens=256,
      early_stopping=True,
      do_sample=True,
      eos_token_id=128001,
)


# In[ ]:


print(' -- 모델 답변')
print(tokenizer.decode(gened[0]).split('<|start_header_id|>assistant<|end_header_id|>\n')[1])
print(' -- 정답 답변')
print(test_script_answer)

