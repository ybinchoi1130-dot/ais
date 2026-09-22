"""
https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ko
문서 처리 및 요약: 
    - PDF를 파싱하고 간결한 요약을 반환합니다. 
    - 문서 처리 파이프라인을 빌드하거나 수신 파일을 빠르게 분류하는 데 유용합니다.
"""

#%%

from google import genai
from google.genai import types
# import httpx

client = genai.Client()

# Download a sample PDF document
# doc_url = "https://storage.googleapis.com/generativeai-downloads/data/med_gemini.pdf"
# doc_data = httpx.get(doc_url).content
uploaded_file = client.files.upload(file='med_gemini.pdf')

prompt = "Summarize this document and translate to Korean"

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=[uploaded_file, prompt]
)

print(response.text)

#%%

"""
제공해주신 문서 "Capabilities of Gemini Models in Medicine"에 대한 요약과 한국어 번역입니다.

---

### **문서 요약 (Summary)**

이 논문은 구글의 Gemini 모델을 의료 분야에 특화하여 발전시킨 **Med-Gemini** 모델 제품군을 소개합니다. Med-Gemini는 고도화된 임상 추론, 다중 모달(multimodal) 이해, 긴 문맥(long-context) 처리 능력을 갖추고 있으며, 다음과 같은 핵심 기여를 제시합니다:

1.  **임상 추론 강화:** 웹 검색 기능의 자가 학습(self-training)과 불확실성 기반 검색 전략을 통해 MedQA(USMLE) 벤치마크에서 91.1%라는 최고 성능(SoTA)을 달성했습니다.
2.  **다중 모달 전문성:** 전문 인코더와 미세 조정을 통해 영상(의료 영상, 피부 병변 등) 및 파형(ECG) 데이터 분석 능력을 크게 향상했습니다.
3.  **긴 문맥 처리 능력:** 대규모 전자 건강 기록(EHR) 및 긴 의료 영상을 분석하여 정보 검색 및 질의응답에서 획기적인 성능을 보였습니다.
4.  **실제 활용 가능성:** 의료 요약, 진료 의뢰서 작성, 복잡한 의료 정보 대화 등 실제 임상 현장에서의 잠재적 유용성을 시연했습니다.
5.  **책임 있는 AI:** 성능 향상과 더불어 AI 모델의 편향성, 데이터 품질, 안전성 확보의 중요성을 강조하며, 실제 의료 현장 도입을 위해 엄격한 평가와 추가적인 연구가 필수적임을 역설합니다.

---

### **한국어 번역 요약 (번역)**

**의료 분야에서의 Gemini 모델 역량**

본 논문은 구글의 Gemini 모델을 기반으로 의료 분야에 
특화된 다중 모달 모델 제품군인 'Med-Gemini'를 소개합니다. 
Med-Gemini는 임상 추론, 다중 모달 이해, 
긴 문맥 처리라는 Gemini의 핵심 강점을 바탕으로 구축되었습니다.

**주요 성과:**
*   **임상 추론:** 자가 학습 및 웹 검색 통합을 통해 MedQA(USMLE) 벤치마크에서 91.1%의 정확도를 기록하며 최첨단(SoTA) 성능을 달성했습니다.
*   **다중 모달 및 긴 문맥:** 전자 건강 기록(EHR) 내 '니들 인 어 헤이스택(needle-in-a-haystack)' 검색 및 의료 영상 분석 등 14개 의료 벤치마크 중 10개에서 기존 SoTA 성능을 넘어섰습니다. 특히 GPT-4V와의 직접 비교 가능한 모든 벤치마크에서 우수한 성과를 보였습니다.
*   **실제 활용:** 의학적 요약, 진료 의뢰서 작성 및 대화형 의료 상담 등에서 인간 전문가를 상회하거나 견줄 만한 성능을 입증했습니다.

**결론:**
Med-Gemini는 의료 AI의 새로운 가능성을 보여주지만, 
실제 의료 현장에서 안전하게 배포되기 위해서는 추가적인 엄격한 평가와 규제 준수, 
그리고 편향성 및 안전성에 대한 지속적인 연구가 필요합니다. 
본 연구는 AI가 의사의 보조 도구로서 과학적 발전과 
의료 서비스 질 향상을 가속화할 수 있는 미래를 제시합니다.
"""


