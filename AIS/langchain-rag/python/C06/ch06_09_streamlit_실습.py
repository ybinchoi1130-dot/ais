#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install -q streamlit==1.41.1')
get_ipython().system('npm install localtunnel')


# In[ ]:


get_ipython().run_cell_magic('writefile', 'app.py', "\nimport streamlit as st\n\n\nst.write('Streamlit 실습 페이지')\n")


# In[ ]:


import urllib
print("Password/Enpoint IP :",urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n"))


# In[ ]:


get_ipython().system('streamlit run app.py &>/content/logs.txt &')


# In[ ]:


get_ipython().system('npx localtunnel --port 8501')


# In[ ]:




