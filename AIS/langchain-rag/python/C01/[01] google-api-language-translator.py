
# pip install google-genai
# 환경변수에 GEMINI_API_KEY 등록

from google import genai

client = genai.Client()

language = "Korean"
text = "Hey, are you down to grab some pizza later? I'm starving!"

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    config={
        "system_instruction": "Only output the translated text"
    },
    contents=f"Translate the following text to {language}: {text}"
)

print(response.text)

#%%

"""
야, 이따가 피자 먹으러 갈래? 배고파 죽겠어!
"""