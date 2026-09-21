#!/usr/bin/env python
# coding: utf-8

# In[1]:


# get_ipython().system('pip install openai==1.57.4')
# pip install openai==1.57.4


# In[2]:

from openai import OpenAI

# import os
# OpenAI API 키를 환경 변수에 설정합니다.
# os.environ['OPENAI_API_KEY'] = 'OPENAI API KEY'

# OpenAI 클라이언트를 생성합니다.
client = OpenAI()

#%%

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", 
            "content": "너는 상담원이야" # 페르소나
        },
        {
            "role": "user",
            "content": "서울 명소는?"
        }
    ]
)
# 모델의 응답을 출력합니다.
print(completion.choices[0].message.content)


#%%

"""
서울에는 많은 명소가 있습니다. 몇 가지를 소개해 드릴게요:

1. **경복궁**: 한국의 역사적인 왕궁으로, 아름다운 건축물과 정원이 있는 곳입니다. 근처에 있는 국립민속박물관도 추천합니다.

2. **N서울타워**: 서울의 랜드마크 중 하나로, 정상에서 서울 전경을 감상할 수 있는 곳입니다. 야경이 아름다워서 데이트 코스로도 인기가 많습니다.

3. **명동**: 쇼핑과 다양한 먹거리를 즐길 수 있는 인기 있는 거리입니다. 특히 거리 음식과 화장품 가게들이 많습니다.

4. **홍대**: 젊은이들의 문화가 살아 있는 지역으로, 다양한 카페, 음식점, 예술 공연을 경험할 수 있습니다.

5. **북촌 한옥마을**: 전통 한옥이 잘 보존된 곳으로, 옛 서울의 분위기를 느낄 수 있습니다.

6. **청계천**: 도심 속의 아름다운 하천으로, 산책하기 좋은 장소입니다.

7. **롯데월드타워**: 서울에서 가장 높은 빌딩으로, 전망대에서 멋진 경치를 감상할 수 있습니다.

이 외에도 더 많은 장소가 있으니, 여행 계획에 맞춰 찾아보시면 좋을 것 같습니다!
"""

#%%

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", 
            "content": "너는 관광 가이드야" # 페르소나
        },
        {
            "role": "user",
            "content": "수원 전통 명소는?"
        }
    ]
)
# 모델의 응답을 출력합니다.
print(completion.choices[0].message.content)

#%%

"""
수원은 한국의 전통과 현대가 잘 어우러진 도시로, 
여러 가지 전통 명소가 있습니다. 
다음은 수원에서 꼭 방문해야 할 몇 가지 전통 명소입니다:

1. **수원화성** 
    - 유네스코 세계문화유산으로 지정된 수원화성은 조선 시대의 성곽으로, 
    군사적인 목적과 함께 방어와 행정의 중심지로 세워졌습니다. 
    성곽을 따라 산책하거나 성 내부의 건축물을 구경할 수 있습니다.

2. **화성행궁** 
    - 수원화성과 함께 지어진 행궁으로, 
    왕이 수원에 방문할 때 머물던 곳입니다. 
    아름다운 정원과 함께 역사적인 건물들이 잘 보존되어 있어 많은 관광객들이 찾습니다.
"""



