#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pickle
import torch
import transformers
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import SFTTrainer, SFTConfig

# Windows 콘솔 한글 인코딩 설정
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 텍스트 청크로 저장된 데이터 파일인 전자금융거래.pk 파일에서 데이터를 로드합니다.
script_dir = os.path.dirname(os.path.abspath(__file__))
pk_path = os.path.join(script_dir, '전자금융거래.pk') if os.path.exists(os.path.join(script_dir, '전자금융거래.pk')) else '전자금융거래.pk'

print(f"데이터 파일 경로: {pk_path}")
with open(pk_path, 'rb') as f:
    data_list = pickle.load(f)

print(f"로드된 청크 데이터 수: {len(data_list)}개")

# 학습에 사용할 모델 ID를 지정하여 언어 모델을 불러옵니다.
# 로컬 CPU/저사양 환경에서도 원활하게 학습 실습을 완료할 수 있도록 경량 모델(Qwen2.5-0.5B-Instruct)을 사용합니다.
# (VRAM 80GB 이상 고사양 멀티 GPU 서버/Colab 환경에서는 원래 모델인 "MLP-KTLim/llama-3-Korean-Bllossom-8B" 사용 가능)
model_id = "Qwen/Qwen2.5-0.5B-Instruct"
print(f"모델 로드 중: {model_id}...")

tokenizer = AutoTokenizer.from_pretrained(model_id)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    device_map="auto"
)

# 로드된 데이터 리스트를 기반으로 데이터셋 객체를 생성합니다.
data = Dataset.from_list([{"text": i} for i in data_list], split="train")

# 학습 결과를 저장할 디렉토리 경로를 설정합니다.
output_path = os.path.join(script_dir, "fft_model_save")

# SFTConfig 설정 (최신 TRL 규격)
# 로컬 CPU 환경을 고려하여 과도한 대기시간 없이 전체 학습 파이프라인(Loss 계산, 역전파, 가중치 업데이트, 모델 저장)을
# 성공적으로 검증할 수 있도록 max_steps를 3으로 설정합니다.
# (전체 에폭 학습을 원하실 경우 max_steps 대신 num_train_epochs=1 등으로 설정 가능합니다)
training_args = SFTConfig(
    output_dir=output_path,
    per_device_train_batch_size=1,  # CPU 환경에 맞게 배치 크기 설정
    gradient_accumulation_steps=2,  # 기울기 누적 스텝
    learning_rate=2e-4,             # 학습률
    max_steps=3,                    # 로컬 실습을 위한 스텝 수 (조정 가능)
    logging_steps=1,                # 매 스텝마다 로그 기록
    dataset_text_field="text",
    max_length=256,                 # 시퀀스 길이 제한 (메모리 절약)
    fp16=False,                     # CPU 환경에서는 fp16 미지원
    use_cpu=True,                   # CPU 명시 사용
    report_to="none",               # 외부 로깅 비활성화
    save_strategy="steps",
    save_steps=3,
)

# SFTTrainer 클래스 초기화
trainer = SFTTrainer(
    model=model,
    train_dataset=data,
    processing_class=tokenizer,
    args=training_args,
)

# 설정된 인자와 함께 학습을 시작합니다.
print("\nFull Fine-Tuning 학습을 시작합니다...")
trainer.train()

# 학습된 모델과 토크나이저를 저장합니다.
trainer.save_model(output_path)
tokenizer.save_pretrained(output_path)

print(f"\n학습 완료! 파인튜닝된 모델과 토크나이저가 다음 경로에 저장되었습니다:\n'{output_path}'")
