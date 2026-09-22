#!/usr/bin/env python
# coding: utf-8

# #예제 4.1

# In[ ]:


# langchain, openAI, neo4j
get_ipython().system('pip install langchain==0.3.14')
get_ipython().system('pip install langchain_openai==0.3.0')
get_ipython().system('pip install neo4j==5.27.0')
get_ipython().system('pip install langchain-community==0.3.14')


# # 예제 4.2
# 

# In[ ]:


from langchain_community.graphs import Neo4jGraph
import os

os.environ['OPENAI_API_KEY'] = "" # API 키를 입력하세요.


# # 예제 4.3

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


# # 예제 4.4

# In[ ]:


result = graph.query("""
MATCH (u:User)
WHERE  u.display_name CONTAINS 'ch'
RETURN
    u.display_name AS DisplayName
ORDER BY u.display_name DESC
LIMIT 3""")

print(result)


# #예제4.5

# In[ ]:


# 그래프 내부 고유 노드 레이블(DISTINCT) 조회
result = graph.query("""
MATCH (n)
RETURN
    DISTINCT labels(n) AS Labels
LIMIT 100""")
print(result)


# #예제 4.6

# In[ ]:


# ‘User’ 노드ID 카운트
result = graph.query("""
MATCH (n:User)
WITH
    count(DISTINCT elementId(n)) AS Node_Unique_Count
RETURN
    Node_Unique_Count """)
print(result)


# #예제 4.7

# In[ ]:


# ‘User’ 노드 1개 살펴보기
result = graph.query("""
MATCH (n:User)
RETURN
    elementId(n) AS NodeID,
    labels(n) AS Labels,
    keys(n) AS key,
    properties(n) AS Properties,
    size(keys(n)) AS PropertyCount
LIMIT 1 """)
print(result)

