#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Google Generative AI 패키지를 설치하여 API에 접근할 수 있도록 합니다.
get_ipython().system('pip install -q -U google-generativeai==0.8.3')


# In[ ]:


# 필요한 모듈을 임포트합니다.
import google.generativeai as genai
import pickle
from tqdm import tqdm
import re
# Generative AI 모델을 설정합니다. "gemini-1.5-flash" 모델을 사용하여 질문과 답변을 생성
genai.configure(api_key="GOOGLE_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")


# In[ ]:


# 청킹된 데이터 파일인 '전자금융거래.pk' 파일에서 데이터를 불러옴
data_list = pickle.load(open('전자금융거래.pk', 'rb'))


# In[ ]:


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

# 각 텍스트 청크에 대해 질문과 답변을 생성하고, qa_data에 저장
for i, chunk in enumerate(tqdm(data_list)):
    try:
        # 각 청크를 프롬프트에 삽입하여 질문과 답변을 생성
        model_output = model.generate_content(prompt.format(chunk=chunk)).text
    except Exception as e:
        print(e)
        continue

    # 정규표현식을 사용하여 생성된 텍스트에서 질문과 답변을 추출
    questions = re.findall(r"질문\d+:\s*(.*?)\s*답변\d+:", model_output, re.DOTALL)
    answers = re.findall(r"답변\d+:\s*(.*?)(?:\n질문|$)", model_output, re.DOTALL)

    # 질문과 답변을 쌍으로 묶어 qa_data에 추가
    for question, answer in zip(questions, answers):
        question, answer = question.strip(), answer.strip()
        qa_data.append({
            "index": i,
            "chunk": chunk,
            "question": question,
            "answer": answer
        })
        print(f"Q: {question}\nA: {answer}")

# 생성된 QA 데이터를 pickle 모듈을 사용하여 바이너리 파일로 저장
with open('qa_data.pkl', 'wb') as f:
    pickle.dump(qa_data, f)

