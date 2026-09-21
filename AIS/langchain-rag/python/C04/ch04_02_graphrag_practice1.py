#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# langchain, openAI, neo4j
get_ipython().system('pip install langchain==0.3.14')
get_ipython().system('pip install langchain_openai==0.3.0')
get_ipython().system('pip install neo4j==5.27.0')
get_ipython().system('pip install langchain-community==0.3.14')


# In[ ]:


from langchain_community.graphs import Neo4jGraph
import os
os.environ['OPENAI_API_KEY'] = "" # API 키를 입력하세요.


# In[ ]:


import matplotlib.pyplot as plt
import networkx as nx

# Neo4jGraph 객체 사용
# neo4j Bolt URL, Username, Password를 입력하세요 #예시 
graph = Neo4jGraph(url= "bolt://44.202.189.21:7687" , username="neo4j", password="figures-ability-miner")

# 스키마 가져오기
query = """
CALL db.schema.visualization;
"""
results = graph.query(query)

# 결과 구조 확인
print("Results structure:", results)

# NetworkX 그래프 생성
G = nx.Graph()

# 결과가 리스트의 딕셔너리 형태로 반환됨
for result in results:
    # 노드 추가
    for node in result['nodes']:
        G.add_node(node['name'], name=node['name'])

    # 엣지 추가
    for rel in result['relationships']:
        start_node = rel[0]['name']
        end_node = rel[2]['name']
        rel_type = rel[1]
        G.add_edge(start_node, end_node, name=rel_type)

# 그래프 레이아웃 설정
pos = nx.spring_layout(G)

# 그래프 그리기
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')

# 엣지 레이블 추가
edge_labels = nx.get_edge_attributes(G, 'name')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# 노드 레이블 추가
node_labels = nx.get_node_attributes(G, 'name')
nx.draw_networkx_labels(G, pos, node_labels, font_size=12)

plt.title("Neo4j Stackoverflow Schema Visualization")
plt.axis('off')
plt.tight_layout()
plt.show()


# # 예제 4.8

# In[ ]:


from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI
from langchain_community.graphs import Neo4jGraph
import os
# os.environ['OPENAI_API_KEY'] = "" # API 키를 입력

chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(temperature=0), model="gpt-4o-mini", graph=graph, verbose=True, allow_dangerous_requests=True
)
chain.invoke("누가 가장 많이 답변을 달았어? 답변 횟수도 같이 알려줘.")


# 

# # 예제 4.9

# In[ ]:


chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(temperature=0.5, model="gpt-4"), # gpt-4 모델 설정
    graph=graph,
    verbose=True,
    return_intermediate_steps=True,
    allow_dangerous_requests=True
)

chain.invoke("유저간의 상호작용을 분석하여 서로의 질문에 가장 자주 답변한 사용자 쌍을 찾아줘. 그리고 그 둘의 질문과 답변의 평균 점수도 출력해줘")


# # 예제 4.10

# In[ ]:


result = chain.invoke("GraphRAG 단어가 포함된 질문을 남긴 유저는 누구야?")

