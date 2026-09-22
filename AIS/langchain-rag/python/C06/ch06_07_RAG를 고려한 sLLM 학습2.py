#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# get_ipython().system('pip install trl==0.13.0')
# get_ipython().system('pip install datasets==3.2.0')
# get_ipython().system('pip install -U bitsandbytes==0.45.0')
# get_ipython().system('pip install git+https://github.com/huggingface/peft.git -q')


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


# 이전에 생성한 질문과 답변 데이터셋인 'qa_data.pkl' 파일을 불러옵니다.
data_list = pickle.load(open('qa_data.pkl', 'rb'))


# In[ ]:


# 사용할 사전 학습된 인스트럭션 모델 ID를 지정합니다.
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


# 학습 스크립트 형식을 정의합니다. 질문에 답변할 때 참고할 문서 두 개와 질문 및 답변 형식을 지정합니다.
script_format = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

너는 제공된 문서를 참조하여 답변을 하는 사람이야.<|eot_id|><|start_header_id|>user<|end_header_id|>
- 문서 1
{doc_1}
- 문서 2
{doc_2}

질문 : {q}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
답변 : {a} <|eot_id|>
"""


# In[ ]:


# 네거티브 샘플링을 적용하여 RAG 학습 데이터를 생성하는 함수
def create_rag_data_with_negative_sampling(data_list):
    rag_data = []

    for data in data_list:
        q = data['question']  # 질문
        a = data['answer']    # 정답 답변
        correct_doc = data['chunk']  # 정답 문서

        # 정답 문서를 제외한 다른 문서에서 네거티브 샘플을 하나 선택
        negative_samples = random.sample([d['chunk'] for d in data_list if d['chunk'] != correct_doc], 1)

        # 정답 문서와 네거티브 문서를 무작위로 배치
        documents = [correct_doc] + negative_samples
        random.shuffle(documents)

        # 정답 문서의 위치를 1 또는 2로 설정
        correct_doc_position = documents.index(correct_doc) + 1

        # script_format을 사용해 학습용 스크립트를 생성
        script = script_format.format(
            doc_1=documents[0],
            doc_2=documents[1],
            q=q,
            a=a
        )

        # 생성된 데이터를 리스트에 추가
        rag_data.append({
            'script': script,
            'correct_doc_position': correct_doc_position
        })

    return rag_data


# In[ ]:


# RAG 학습 데이터를 생성
# 생성된 데이터는 정답과 네거티브 샘플이 포함됨
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


# 학습된 모델을 사용하여 질문에 대한 답변을 생성하고, 생성된 답변과 정답을 비교
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

