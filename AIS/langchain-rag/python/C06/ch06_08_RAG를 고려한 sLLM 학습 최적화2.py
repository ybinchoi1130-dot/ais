#!/usr/bin/env python
# coding: utf-8

import os
import sys
import json
import pickle
import random
from pprint import pprint
from tqdm import tqdm

import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from datasets import Dataset
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

# 이전 단계에서 생성한 'qa_data.pkl' 데이터를 불러옵니다.
pk_path = os.path.join(script_dir, 'qa_data.pkl')
if os.path.exists(pk_path) and os.path.getsize(pk_path) > 0:
    with open(pk_path, 'rb') as f:
        data_list = pickle.load(f)
else:
    data_list = []

# 기존 데이터 폴더(python/data/qa_data.pkl)가 있는 경우 병합하여 다양한 네거티브 샘플 확보
alt_pk = os.path.join(script_dir, '..', 'data', 'qa_data.pkl')
if os.path.exists(alt_pk):
    with open(alt_pk, 'rb') as f:
        data_list.extend(pickle.load(f))

print(f"로드된 총 QA 데이터 수: {len(data_list)}개")

# 사용할 사전 학습된 모델의 ID를 지정합니다.
# (로컬 CPU/RAM 환경을 위해 Qwen2.5-0.5B-Instruct 사용, GPU 16GB+ 환경에서는 교재 원본 모델 사용 가능)
model_id = "Qwen/Qwen2.5-0.5B-Instruct"
print(f"모델 로드 중: {model_id}...")

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float32
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map="auto"
)
model.gradient_checkpointing_enable()
model = prepare_model_for_kbit_training(model)

# 학습 스크립트 형식을 정의 (Qwen ChatML 포맷 적용)
# 각 질문에 대해 두 개의 문서(정답 문서 1개 + 오답/네거티브 문서 1개)를 제시하고,
# 모델이 참조한 문서 번호([1] 또는 [2])를 답변 뒤에 인용하도록 훈련
script_format = """<|im_start|>system
너는 제공된 문서를 참조하여 답변을 하는 사람이야.
답변을 위해 참조한 문서의 번호를 답변 마지막에 번호를 붙여줘
1번 문서를 참조한 경우 답변 마지막에 "[1]"을 추가해줘<|im_end|>
<|im_start|>user
- 문서 1
{doc_1}
- 문서 2
{doc_2}

질문 : {q}
<|im_end|>
<|im_start|>assistant
답변 : {a}[{number}]<|im_end|>
"""

# 네거티브 샘플링을 적용한 RAG 데이터 생성 함수
def create_rag_data_with_negative_sampling(data_list):
    rag_data = []
    all_chunks = list(set(d['chunk'] for d in data_list))

    for data in data_list:
        q = data['question']
        a = data['answer']
        correct_doc = data['chunk']

        # 정답 문서를 제외한 네거티브 샘플링 문서를 1개 선택
        other_chunks = [c for c in all_chunks if c != correct_doc]
        if not other_chunks:
            continue
        negative_samples = random.sample(other_chunks, 1)

        # 문서를 무작위로 배치 (1번 또는 2번 문서)
        documents = [correct_doc] + negative_samples
        random.shuffle(documents)

        # 정답 문서의 위치 (1 또는 2)
        correct_doc_position = documents.index(correct_doc) + 1

        # 프롬프트 스크립트 생성
        script = script_format.format(
            doc_1=documents[0],
            doc_2=documents[1],
            q=q,
            a=a,
            number=correct_doc_position
        )

        rag_data.append({
            'script': script,
            'correct_doc_position': correct_doc_position
        })

    return rag_data

# RAG 학습 데이터를 생성합니다.
rag_data_with_negatives = create_rag_data_with_negative_sampling(data_list)
print(f"네거티브 샘플링 적용 RAG 학습 샘플 생성 완료: {len(rag_data_with_negatives)}개")

# Dataset 객체 생성 및 토큰화
data = Dataset.from_list([{"text": i['script']} for i in rag_data_with_negatives], split="train")
data = data.map(lambda samples: tokenizer(samples["text"], truncation=True, max_length=512), batched=True)

# LoRA 설정 구성 및 모델 적용
config = LoraConfig(
    r=8,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, config)
print("\n[LoRA 학습 파라미터]")
model.print_trainable_parameters()

# 학습 전 테스트용 프롬프트 준비
test_idx = min(5, len(rag_data_with_negatives) - 1)
full_script = rag_data_with_negatives[test_idx]['script']
test_script = full_script.split('답변 : ')[0] + '답변 : '
test_script_answer = '답변 : ' + full_script.split('답변 : ')[1]

print("\n--- [학습 전 모델 추론 테스트] ---")
inputs = tokenizer(test_script, return_tensors='pt').to(model.device)
gened = model.generate(
    **inputs,
    max_new_tokens=64,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    eos_token_id=tokenizer.eos_token_id,
)
print(test_script)
print(' -- 모델 답변:')
decoded = tokenizer.decode(gened[0], skip_special_tokens=True)
print(decoded[len(test_script):].strip() if test_script in decoded else decoded)
print('\n -- 정답 답변:')
print(test_script_answer.replace('<|im_end|>', '').strip())
print("-" * 50)

# Trainer 클래스를 사용하여 모델 학습 설정
output_dir = os.path.join(script_dir, "rag_opt_output")
save_dir = os.path.join(script_dir, "rag_opt_outputs")

training_args = transformers.TrainingArguments(
    per_device_train_batch_size=1,
    gradient_accumulation_steps=2,
    max_steps=5,             # 로컬 실습을 위해 5스텝 진행 (조정 가능)
    warmup_steps=2,
    learning_rate=2e-4,
    fp16=False,              # CPU 환경에서는 fp16 미지원
    use_cpu=True,            # CPU 명시 사용
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

model.config.use_cache = False

print("\nRAG 최적화 sLLM 학습을 시작합니다...")
trainer.train()

# 모델 저장
model_to_save = trainer.model.module if hasattr(trainer.model, 'module') else trainer.model
model_to_save.save_pretrained(save_dir)
tokenizer.save_pretrained(save_dir)
print(f"\nRAG 최적화 모델 가중치가 '{save_dir}' 디렉터리에 저장되었습니다.")

# 학습 후 동일한 프롬프트로 생성 결과 확인
print("\n--- [학습 후 모델 추론 테스트] ---")
model.config.use_cache = True
gened = model.generate(
    **inputs,
    max_new_tokens=64,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    eos_token_id=tokenizer.eos_token_id,
)
print(' -- 학습 후 모델 답변:')
decoded_after = tokenizer.decode(gened[0], skip_special_tokens=True)
print(decoded_after[len(test_script):].strip() if test_script in decoded_after else decoded_after)
print('\n -- 원본 정답:')
print(test_script_answer.replace('<|im_end|>', '').strip())
print("-" * 50)
print("\n모든 RAG 고려 sLLM 학습 최적화 실습 과정이 성공적으로 완료되었습니다!")
