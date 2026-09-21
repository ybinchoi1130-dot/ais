
(PACKAGE)
pip install openai==1.57.4
pip install -q -U google-generativeai==0.8.3

pip install langchain_openai==0.2.6
pip install langchain_community==0.3.5



(OPENAI_API_KEY)
import getpass
import os

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

