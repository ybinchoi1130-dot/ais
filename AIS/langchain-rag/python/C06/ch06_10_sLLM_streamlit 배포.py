#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install -q streamlit==1.41.1')
get_ipython().system('npm install localtunnel')
get_ipython().system('pip install vllm==0.6.6.post1')
get_ipython().system('pip install -U bitsandbytes==0.45.0')
get_ipython().system('pip install triton==3.1.0')


# In[ ]:


get_ipython().run_cell_magic('writefile', 'app.py', '\nimport streamlit as st\nimport torch\nfrom vllm import LLM, SamplingParams\n\n\n# 모델을 캐싱하여 최초 한 번만 로드\n@st.cache_resource\ndef load_model():\n    model_id = "PrunaAI/saltlux-Ko-Llama3-Luxia-8B-bnb-4bit-smashed"\n    # LLM 객체 생성\n    llm = LLM(\n        model=model_id,\n        dtype="float16",\n        quantization="bitsandbytes",  # bitsandbytes 양자화 사용\n        load_format="bitsandbytes",   # load_format을 명시적으로 설정\n        max_model_len=512,            # 최대 시퀀스 길이 감소\n        gpu_memory_utilization=0.7,   # GPU 메모리 활용도 제한\n        max_num_batched_tokens=512,   # 배치된 토큰 수 제한\n        max_num_seqs=1,               # 동시에 처리할 시퀀스 수 제한\n    )\n    return llm\n\n# 모델과 토크나이저 로드\nllm = load_model()\n\n# Streamlit 페이지에 모델 설명 출력\nst.write(\'sLLM을 활용한 Streamlit 배포 예제\')\n\n# 사용자 입력을 받기 위한 텍스트 입력 상자\nuser_input = st.text_input(\'질문을 입력하세요:\')\n\n# 모델이 입력에 대해 답변을 생성\nif user_input:\n    sampling_params = SamplingParams(max_tokens=256)\n    outputs = llm.generate([user_input], sampling_params)[0].outputs[0].text\n    st.write(\'모델의 답변:\', outputs)\n')


# In[ ]:


import urllib
print("Password/Enpoint IP :",urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n"))


# In[ ]:


get_ipython().system('streamlit run app.py &>/content/logs.txt &')


# In[ ]:


get_ipython().system('npx localtunnel --port 8501')

