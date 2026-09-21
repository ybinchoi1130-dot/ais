"""
https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ko
문서 처리 및 요약: 
    - PDF를 파싱하고 간결한 요약을 반환합니다. 
    - 문서 처리 파이프라인을 빌드하거나 수신 파일을 빠르게 분류하는 데 유용합니다.
"""

#%%

from google import genai
from google.genai import types
import httpx

client = genai.Client()

# Download a sample PDF document
doc_url = "https://storage.googleapis.com/generativeai-downloads/data/med_gemini.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=[
        types.Part.from_bytes(
            data=doc_data,
            mime_type='application/pdf',
        ),
        prompt
    ]
)

print(response.text)