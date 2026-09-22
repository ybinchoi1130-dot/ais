#!/usr/bin/env python
# coding: utf-8

import os
import sys
import json
import pickle
from pprint import pprint
from tqdm import tqdm

import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from datasets import load_dataset, Dataset
from peft import prepare_model_for_kbit_training, LoraConfig, get_peft_model

# Windows 콘솔 한글 출력 인코딩 설정
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

os.environ["WANDB_DISABLED"] = "true"

# 현재 스크립트 디렉터리 경로
script_dir = os.path.dirname(os.path.abspath(__file__))

# pickle 모듈을 사용하여 청킹한 “전자금융거래.pk” 바이너리 파일 데이터를 불러옵니다.
pk_path = os.path.join(script_dir, '전자금융거래.pk') if os.path.exists(os.path.join(script_dir, '전자금융거래.pk')) else '전자금융거래.pk'
print(f"데이터 파일 로드: {pk_path}")
with open(pk_path, 'rb') as f:
    data_list = pickle.load(f)

print(f"로드된 청크 데이터 수: {len(data_list)}개")

# 사용할 사전 학습된 모델의 ID를 지정합니다.
# (로컬 CPU/RAM 환경을 위해 Qwen2.5-0.5B-Instruct 사용, 고사양 GPU 16GB+ 환경에서는 "MLP-KTLim/llama-3-Korean-Bllossom-8B" 사용 가능)
model_id = "Qwen/Qwen2.5-0.5B-Instruct"
print(f"모델 로드 중: {model_id}...")

# BitsAndBytesConfig를 사용하여 4-bit 양자화 설정을 구성합니다.
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float32  # 로컬 CPU 환경 호환성을 위해 float32 사용
)

# 토크나이저와 모델을 불러옵니다.
tokenizer = AutoTokenizer.from_pretrained(model_id)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map="auto"
)

# 모델의 기울기 체크포인팅을 활성화하여 메모리 사용을 줄입니다.
model.gradient_checkpointing_enable()

# 모델을 K-bit 양자화 훈련에 적합하도록 준비합니다.
model = prepare_model_for_kbit_training(model)

# 불러온 데이터 리스트를 기반으로 데이터셋 객체를 생성하고 텍스트 데이터를 토큰화합니다.
data = Dataset.from_list([{"text": i} for i in data_list], split="train")
data = data.map(lambda samples: tokenizer(samples["text"], truncation=True, max_length=256), batched=True)

# LoraConfig를 사용하여 DoRA 설정을 구성합니다.
# use_dora=True 옵션을 활성화하여 방향(Direction)과 크기(Magnitude)를 분해하여 학습합니다.
config = LoraConfig(
    r=8,
    lora_alpha=32,       # LoRA 스케일링 계수로, 모델 학습 중 LoRA 영향력 조절
    lora_dropout=0.05,   # 드롭아웃 확률 설정
    bias="none",         # 바이어스 비활성화
    use_dora=True,       # DoRA(Weight-Decomposed Low-Rank Adaptation) 활성화
    task_type="CAUSAL_LM" # 생성 모델 학습 유형 지정
)

# 설정된 DoRA 구성을 사용하여 모델을 PEFT 모델로 변환합니다.
model = get_peft_model(model, config)
print("\n[DoRA 학습 가능 파라미터 확인]")
model.print_trainable_parameters()

# 학습 전 모델 테스트를 위해 입력 텍스트를 생성해 결과를 확인합니다.
print("\n--- [학습 전 추론 테스트] ---")
input_text = "전자지급수단이 뭐야?"
inputs = tokenizer(input_text, return_tensors='pt').to(model.device)
gened = model.generate(
    **inputs,
    max_new_tokens=64,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    eos_token_id=tokenizer.eos_token_id,
)
print("입력 질문:", input_text)
print("학습 전 답변:", tokenizer.decode(gened[0], skip_special_tokens=True))
print("-" * 40)

# Trainer 클래스를 사용하여 모델 학습을 설정
output_dir = os.path.join(script_dir, "dora_output")
save_dir = os.path.join(script_dir, "dora_outputs")

# 로컬 CPU 환경에서 쾌적하게 전체 학습 루프를 검증할 수 있도록 max_steps=5로 설정
training_args = transformers.TrainingArguments(
    per_device_train_batch_size=1,
    gradient_accumulation_steps=2,
    max_steps=5,             # 로컬 실습을 위해 5 스텝 설정 (조정 가능)
    warmup_steps=2,
    learning_rate=2e-4,
    fp16=False,              # CPU 환경에서는 fp16 미지원
    use_cpu=True,            # CPU 명시
    logging_steps=1,
    output_dir=output_dir,
    report_to="none",
)

trainer = transformers.Trainer(
    model=model,
    train_dataset=data,
    args=training_args,
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False),
)

# 학습 중 메모리 사용량을 최적화하기 위해 캐시 기능을 비활성화
model.config.use_cache = False

print("\nDoRA 학습을 시작합니다...")
trainer.train()

# 학습된 DoRA 어댑터 가중치 저장
model_to_save = trainer.model.module if hasattr(trainer.model, 'module') else trainer.model
model_to_save.save_pretrained(save_dir)
tokenizer.save_pretrained(save_dir)
print(f"\nDoRA 어댑터 가중치가 '{save_dir}' 디렉터리에 저장되었습니다.")

# 학습 후 입력 텍스트로 다시 텍스트 생성을 수행하여 결과를 확인
print("\n--- [학습 후 추론 테스트] ---")
model.config.use_cache = True
gened = model.generate(
    **inputs,
    max_new_tokens=64,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    eos_token_id=tokenizer.eos_token_id,
)
print("입력 질문:", input_text)
print("학습 후 답변:", tokenizer.decode(gened[0], skip_special_tokens=True))
print("-" * 40)
print("\n모든 DoRA 실습 과정이 성공적으로 완료되었습니다!")
