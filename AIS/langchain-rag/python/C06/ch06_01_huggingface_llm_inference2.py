#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# transformers와 torch 라이브러리를 임포트
# transformers는 Hugging Face에서 제공하는 다양한 사전 학습된 모델과 도구를 제공하며,
# torch는 딥러닝을 위한 PyTorch 라이브러리
# import transformers==4.47.1
# import torch==2.5.1+cu121

import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import transformers
import torch


# In[ ]:


# 사용할 모델의 ID를 설정
# 로컬 CPU/저사양 환경에서도 원활하게 실행되도록 
# 경량 모델(Qwen2.5-0.5B-Instruct)로 설정
# (Google Colab 등 VRAM 16GB 이상 환경에서는 
# 원래 교재 모델인 "MLP-KTLim/llama-3-Korean-Bllossom-8B" 사용 가능)
model_id = "Qwen/Qwen2.5-0.5B-Instruct"


# In[ ]:


# 텍스트 생성 파이프라인을 설정
pipeline = transformers.pipeline(
    "text-generation",          # 작업 유형을 'text-generation'으로 설정하여 텍스트 생성 기능을 사용
    model=model_id,             # 지정한 모델 ID로 모델을 로드
    torch_dtype=torch.float32,  # 로컬 CPU 환경 호환성을 위해 float32 사용
    device_map="auto",          # 사용 가능한 장치를 자동으로 할당하여 실행
)


# In[ ]:


# 모델을 평가 모드로 전환
# 평가 모드에서는 훈련 기능이 비활성화되며, 
# 모델이 추론(예측)에 최적화된 상태로 변경
pipeline.model.eval()


# In[ ]:


# AI 어시스턴트가 사용자 질문에 대해 친절하게 답변할 수 있도록
# 대화 형식의 프롬프트를 설정하고, 필요한 종료 조건을 정의하는 과정
#
# PROMPT와 instruction을 통해 AI의 역할과 사용자 요청을 설정하고,
# messages 리스트로 대화 흐름을 정의하여 최종적으로 prompt를 생성
# terminators 리스트는 대화 종료에 사용될 토큰 ID를 지정하여,
# AI가 적절한 시점에 대화를 마칠 수 있도록 함

# AI 어시스턴트의 역할을 정의하는 문구를 PROMPT 변수에 저장
PROMPT = '''당신은 유능한 AI 어시스턴트 입니다. 사용자의 질문에 대해 친절하게 답변해주세요.'''

# 사용자가 AI에게 요청하는 작업 내용을 instruction 변수에 저장
instruction = "서울의 유명한 관광 코스를 만들어줄래?"

# messages 리스트를 생성하여 대화의 흐름을 정의
messages = [
    {"role": "system", "content": f"{PROMPT}"},    # "system" 역할로 AI의 기본 역할을 정의하는 PROMPT를 포함
    {"role": "user", "content": f"{instruction}"}  # "user" 역할로 사용자가 요청한 instruction을 포함
]


# In[ ]:


# 메시지 리스트를 기반으로 대화용 prompt를 생성
# pipeline.tokenizer.apply_chat_template 함수를 사용하여 
# messages 리스트를 템플릿 형식에 맞게 변환하고,
# tokenize=False로 설정해 텍스트 그대로 생성에 활용할 수 있도록 함
prompt = pipeline.tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True  # 텍스트 생성을 위한 추가 정보를 포함해 prompt를 구성
)


# In[ ]:


print(prompt)


# In[ ]:


# 대화를 종료하는 데 사용될 토큰 ID들이 포함된 terminators 리스트를 정의
# 이 리스트는 종료 조건으로 사용되는 
# 특별 토큰(eos_token_id와 <|im_end|>, <|eot_id|>)을 
# 포함하여 대화가 적절히 종료될 수 있도록 함
terminators = [pipeline.tokenizer.eos_token_id]
for token_str in ["<|im_end|>", "<|eot_id|>"]:
    tok_id = pipeline.tokenizer.convert_tokens_to_ids(token_str)
    if tok_id is not None and tok_id != pipeline.tokenizer.unk_token_id:
        terminators.append(tok_id)

# outputs 변수에 텍스트 생성 결과를 저장
# pipeline 함수는 생성된 텍스트를 반환
outputs = pipeline(
    prompt,              # 앞서 생성된 prompt를 사용하여 모델이 텍스트를 생성
    max_new_tokens=512,  # 로컬 CPU 환경을 고려하여 512개의 새로운 토큰을 생성
    eos_token_id=terminators,  # terminators 리스트에 포함된 종료 토큰을 만나면 생성을 중단
    do_sample=True,  # 샘플링 방식으로 텍스트를 생성하여 결과가 다양하게 나올 수 있게 함
    temperature=0.6,  # 샘플링 확률 분포를 조절하여 모델이 결정적으로 또는 창의적으로 행동하도록 설정
    top_p=0.9  # 상위 90%에 해당하는 누적 확률의 토큰만을 고려하여 샘플링을 진행
)

# 생성된 텍스트 출력. prompt 길이 이후의 텍스트만 출력하여 사용자 요청에 대한 응답을 표시
print(outputs[0]["generated_text"][len(prompt):])


# # 프롬프트 직접 만들어서 바로 쓰기

# In[ ]:


prompt = "서울에서 갈만한 곳 추천해줘"

outputs = pipeline(
    prompt,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9
)

print(outputs[0]["generated_text"][len(prompt):])


# In[ ]:




