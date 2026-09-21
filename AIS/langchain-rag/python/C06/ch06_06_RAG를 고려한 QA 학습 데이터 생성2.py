#!/usr/bin/env python
# coding: utf-8

import os
import sys
import time
import pickle
import re
from tqdm import tqdm
import google.generativeai as genai

# Windows 콘솔 한글 인코딩 설정
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 현재 스크립트 디렉터리 경로
script_dir = os.path.dirname(os.path.abspath(__file__))

# Google API 키 설정 (환경 변수 GOOGLE_API_KEY 또는 GEMINI_API_KEY 확인)
api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY 또는 GEMINI_API_KEY 환경 변수가 설정되어 있지 않습니다.")

genai.configure(api_key=api_key)

# Generative AI 모델을 설정합니다. 최신 Gemini 모델인 "gemini-2.5-flash" 사용
# (이전 gemini-1.5-flash는 서비스 만료 또는 v1beta 지원 종료로 gemini-2.5-flash 권장)
model_name = "gemini-2.5-flash"
print(f"Gemini 모델 초기화 중: {model_name}...")
model = genai.GenerativeModel(model_name)

# 청킹된 데이터 파일인 '전자금융거래.pk' 파일에서 데이터를 불러옴
pk_path = os.path.join(script_dir, '전자금융거래.pk') if os.path.exists(os.path.join(script_dir, '전자금융거래.pk')) else '전자금융거래.pk'
print(f"청킹 데이터 로드: {pk_path}")
with open(pk_path, 'rb') as f:
    data_list = pickle.load(f)

print(f"총 로드된 청크 수: {len(data_list)}개")

# 질문과 답변을 저장할 리스트를 생성
qa_data = []

# AI 모델에 전달할 프롬프트를 정의
prompt = """
너는 지문을 보고 사용자가 궁금해할만한 질문과 답변을 만드는 사람이야.
- 질문과 답변을 5개씩 만들어줘.
질문1:
답변1:
형식으로 답변해줘야해
- 각 질문과 답변의 내용은 다양한 주제를 포함하도록 만들어줘
- 각 질문과 답변은 아래 예시 형식으로 작성해줘.
   그 외에 텍스트는 사용하지 마.

   - 예시
질문1: ~~~
답변1: ~~~
... 생략 ...
질문5: ~~~
답변5: ~~~

    - 지문
{chunk}
"""

# Gemini API 무료 티어(분당 15회 호출 제한) 및 실습 속도를 고려하여 청크 수 지정
# 전체 청크(89개) 생성을 원하시면 MAX_CHUNKS = len(data_list)로 변경하시면 됩니다.
MAX_CHUNKS = 3
target_chunks = data_list[:MAX_CHUNKS]

print(f"\n총 {len(target_chunks)}개 청크에 대해 QA 데이터 생성을 시작합니다...\n")

# 각 텍스트 청크에 대해 질문과 답변을 생성하고, qa_data에 저장
for i, chunk in enumerate(tqdm(target_chunks, desc="QA 생성 진행")):
    try:
        # 각 청크를 프롬프트에 삽입하여 질문과 답변을 생성
        response = model.generate_content(prompt.format(chunk=chunk))
        model_output = response.text
    except Exception as e:
        print(f"\n[오류 발생 - 청크 {i}]: {e}")
        continue

    # 정규표현식을 사용하여 생성된 텍스트에서 질문과 답변을 추출
    questions = re.findall(r"질문\d+:\s*(.*?)\s*(?=답변\d+:)", model_output, re.DOTALL)
    answers = re.findall(r"답변\d+:\s*(.*?)(?=(?:\n\s*질문\d+:|\Z))", model_output, re.DOTALL)

    print(f"\n--- [청크 {i+1}에서 추출된 질문/답변 쌍 ({len(questions)}개)] ---")
    # 질문과 답변을 쌍으로 묶어 qa_data에 추가
    for question, answer in zip(questions, answers):
        question, answer = question.strip(), answer.strip()
        qa_data.append({
            "index": i,
            "chunk": chunk,
            "question": question,
            "answer": answer
        })
        print(f"Q: {question}")
        print(f"A: {answer}\n")

    # API Rate Limit (분당 요청 수) 보호를 위한 짧은 대기
    time.sleep(1)

# 생성된 QA 데이터를 pickle 모듈을 사용하여 바이너리 파일로 저장
output_path = os.path.join(script_dir, 'qa_data.pkl')
with open(output_path, 'wb') as f:
    pickle.dump(qa_data, f)

print(f"\n총 {len(qa_data)}개의 QA 데이터가 '{output_path}'에 성공적으로 저장되었습니다.")
