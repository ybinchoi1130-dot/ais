#!/usr/bin/env python
# coding: utf-8

# # 예제 4.11
# 

# In[ ]:


get_ipython().system('pip install langchain_openai==0.3.0 langchain_core==0.3.29 langchain-community==0.3.14 langchain_experimental==0.3.4')
get_ipython().system('pip install neo4j==5.27.0 #그래프 데이터베이스')
get_ipython().system('pip install tiktoken==0.8.0 #OpenAI의 토크나이저로, 텍스트를 토큰 단위로 분할하는 데 사용')
get_ipython().system('pip install --upgrade --quiet yfiles_jupyter_graphs # 노트북에서 그래프 데이터를 시각화하기 위한 라이브러리')
get_ipython().system('pip install --upgrade -- python-dotenv==1.0.1 # .env 파일에 저장된 환경 변수를 쉽게 불러와 사용')
get_ipython().system('pip install transformers_stream_generator==0.0.5 # Hugging Face의 Transformers 라이브러리를 스트림 형태로 활용할 수 있게 해주는 라이브러리')
get_ipython().system('pip install PyPDF2 # PDF 파일을 파싱하고 조작')


# # 예제 4.12

# In[ ]:


import os
from langchain_core.runnables import  RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import StrOutputParser
from langchain_community.graphs import Neo4jGraph
from langchain_community.vectorstores import Neo4jVector
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores.neo4j_vector import remove_lucene_chars
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_experimental.graph_transformers import LLMGraphTransformer
from neo4j import GraphDatabase
from yfiles_jupyter_graphs import GraphWidget
from PyPDF2 import PdfReader


# ## NEO4J 연결

# # 예제 4.13

# In[ ]:


from neo4j import GraphDatabase
#neo4j aura   : https://workspace-preview.neo4j.io/workspace/query?code=v1kkRwBrrKaMQfEQDTN96KNVX7UVqqQTonY8uKc9tE8Rm&state=f2416a49214041fc89f73ce3f58d30cf

# 연결 정보 설정  #예시 
uri ="neo4j+s://03003836.databases.neo4j.io"
user = "neo4j"  # 기본 사용자 이름은 'neo4j'입니다
password = ""  # AuraDB에서 제공한 비밀번호를 입력하세요

# 드라이버 생성
driver = GraphDatabase.driver(uri, auth=(user, password))
# 연결 테스트
def test_connection(tx):
    result = tx.run("RETURN 1 AS num")
    return result.single()["num"]

with driver.session() as session:
    try:
        result = session.read_transaction(test_connection)
        print(f"neo4j 연결 성공: {result}")
    except Exception as e:
        print(f"neo4j 연결 실패: {e}")


# In[ ]:


from google.colab import drive
drive.mount('/content/drive')


# # 예제 4.14

# ## pdf 파싱 처리
# - 활용 pdf : [24.5월 중장기 심층연구] 혁신과 경제성장 - 우리나라 기업의 혁신활동 분석 및 평가.pdf (49p)
# - https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11934062
# 

# In[ ]:


from langchain.schema import Document

# PDF 파일 경로
pdf_path = "/content/drive/MyDrive/wikibooks/마스터파일/코드/4장_코드/[24.5월 중장기 심층연구] 혁신과 경제성장 - 우리나라 기업의 혁신활동 분석 및 평가.pdf"

# PDF에서 텍스트 추출
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() #페이지별로 순회하며 text 문자열 추가
    return text

# PDF에서 텍스트 추출
pdf_text = extract_text_from_pdf(pdf_path)

# 텍스트 분할
text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=24)
chunks = text_splitter.split_text(pdf_text)

documents = [Document(page_content=chunk) for chunk in chunks]

# 결과 확인
print(f"총 {len(chunks)}개의 청크로 분할되었습니다.")
print("첫 번째 청크의 내용:")
print(chunks[0],'\n')


# # 예제 4.15

# ## 랭체인 graphtransformer로 지식그래프 생성
# 
# - 약 50p 문서를 을 자동 그래프화

# In[ ]:


#약 18분 소요 (gpt-4o)되기때문에 주석처리! (한번 생성해두면 그래프 언제든 불러다 쓸 수 있음.)
os.environ['OPENAI_API_KEY'] ="" # API 키를 입력하세요.

llm = ChatOpenAI(temperature=0, model="gpt-4o")
llm_transformer = LLMGraphTransformer(llm=llm)
graph_documents = llm_transformer.convert_to_graph_documents(documents) #약 20분 소요 (gpt-4o 기준)
graph_documents[0]


# # 예제 4.16

# In[ ]:


graph = Neo4jGraph(uri,user,password)

graph.add_graph_documents(
    graph_documents,
    baseEntityLabel=True,
    include_source=True
)

# 노드의 총 개수 쿼리
node_count_query = """
MATCH (n)
RETURN count(n) AS TotalNodes """
node_result = graph.query(node_count_query)
print("전체 노드의 수:", node_result)

# 관계의 총 개수 쿼리
relationship_count_query = """
MATCH ()-[r]->()
RETURN count(r) AS TotalRelationships
"""
relationship_result = graph.query(relationship_count_query)
print("전체 관계의 수:", relationship_result)


# # 예제 4.17

# In[ ]:


from google.colab import output
output.enable_custom_widget_manager()

def showGraph():
    driver = GraphDatabase.driver(
        uri = uri,
        auth = (user,password))
    session = driver.session()
    widget = GraphWidget(graph = session.run("MATCH (s)-[r]->(t)  RETURN s,r,t LIMIT 500").graph())
    widget.node_label_mapping = 'id'
    return widget

showGraph()


# In[ ]:


from google.colab import output
output.enable_custom_widget_manager()

def showGraph():
    driver = GraphDatabase.driver(
        uri = uri,
        auth = (user,password))
    session = driver.session()
    widget = GraphWidget(graph = session.run("MATCH (s)-[r]->(t)  RETURN s,r,t LIMIT 500").graph())
    widget.node_label_mapping = 'id'
    return widget

showGraph()


# In[ ]:


from google.colab import output
output.enable_custom_widget_manager()

def showGraph():
    driver = GraphDatabase.driver(
        uri = uri,
        auth = (user,
                password))
    session = driver.session()
    widget = GraphWidget(graph = session.run("MATCH (s)-[r:!MENTIONS]->(t) RETURN s,r,t").graph())
    widget.node_label_mapping = 'id'
    return widget

showGraph()


# # 예제 4.18

# ## 하이브리드 리트리버 -그래프 리트리버

# In[ ]:


class Entities(BaseModel):
    """텍스트에서 명명된 개체와 주요 개념을 추출하는 모델"""
    people: list[str] = Field(
        ...,
        description="텍스트에서 언급된 사람 이름 리스트"
)
    organizations: list[str] = Field(
        default_factory=list,
        description="텍스트에서 언급된 조직 리스트"
)
    keywords: list[str] = Field(
        default_factory=list,
        description="텍스트에서 언급된 주요 개념이나 키워드 리스트"
)
llm= ChatOpenAI(temperature=0, model="gpt-4o")
prompt = ChatPromptTemplate.from_messages(
[
        ("system",
         "당신은 자연어 처리 어시스턴트입니다. 제공된 텍스트에서 사람, 조직, 주요 개념과 같은 "
         "명명된 개체를 식별하고 추출해주세요"),
        ("human",
         "다음 텍스트에서 관련 개체들을 추출해 주세요. "
         "다음 카테고리에 맞춰 개체들을 제공해 주세요: "
         "1. 사람, 2. 조직, 3. 주요 키워드 \n\n"
         "텍스트: {question}"),
    ]
)
entity_chain = prompt | llm.with_structured_output(Entities)


# In[ ]:


entity_chain.invoke("한국은행에서 발표한 2024년에 발표된 최근 중소 벤처 투자 관련 동향을 알려줘.")


# In[ ]:





# # 예제 4.19

# In[ ]:


def graph_retriever(question: str) -> str:
    """
    Collects the neighborhood of entities mentioned
    in the question
    """
    result = ""
    entities = entity_chain.invoke({"question": question})

    # names, organizations, keywords 모두를 검색에 사용
    all_entities = entities.people + entities.organizations + entities.keywords

    for entity in all_entities:
        response = graph.query(
            """
            MATCH (node)
            WHERE toLower(node.id) CONTAINS toLower($query) OR toLower(node.text) CONTAINS toLower($query)
            MATCH (node)-[r]-(neighbor)
            WHERE type(r) <> 'MENTIONS'
            RETURN CASE
                WHEN startNode(r) = node
                THEN node.id + ' - ' + type(r) + ' -> ' + neighbor.id
                ELSE neighbor.id + ' - ' + type(r) + ' -> ' + node.id
            END AS output
            LIMIT 50
            """,
            {"query": entity.lower()},
        )
        result += "\n".join([el['output'] for el in response])
        if result:
            result += "\n"  # 각 엔티티의 결과 사이에 빈 줄 추가

    return result.strip()  # 마지막 빈 줄 제거

# 사용 예
question = "저업력 중소기업이 겪는 어려움에 대해 말해줘"
print(graph_retriever(question))


# # 예제 4.20

# ## 하이브리드 리트리버 - 벡터 리트리버

# In[ ]:


# Neo4jVector를 이용해 벡터 인덱스 구성
vector_index = Neo4jVector.from_existing_graph(
    OpenAIEmbeddings(),          # OpenAI 임베딩 모델 사용
    search_type="hybrid",        # 키워드 + 벡터 검색 방식 사용
    node_label="Document",       # 검색 대상 노드 레이블
    text_node_properties=["text"], # 벡터화할 텍스트 속성
    embedding_node_property="embedding", # 임베딩 저장 속성
    url=uri,
    username=user,
    password=password
)
vector_retriever = vector_index.as_retriever()


# # 예제 4.21

# In[ ]:


# Cypher 쿼리 실행
query = """
MATCH (n:Document)
RETURN n.embedding AS embedding, properties(n) AS all_properties
LIMIT 1;
"""
result = graph.query(query)
print(result)


# In[ ]:


vector_retriever.invoke("저업력 중소기업이 겪는 어려움에 대해 말해줘")


# # 예제 4.22

# ## 하이브리드 리트리버 - (그래프 + 벡터)

# In[ ]:


def full_retriever(question: str):
    # 그래프 리트리버를 통해 연관 노드, 관계 Rag 데이터 수집
    graph_data = graph_retriever(question)

    # 벡터 리트리버를 통해 의미적으로 유사한 Rag 데이터 수집
    vector_data = [doc.page_content for doc in vector_retriever.invoke(question)]

    # 최종 출력 형식을 개선하여 가독성을 높임
    final_data = f"""
--- 검색 결과 ---

[Graph Data]
{graph_data if graph_data else "관련된 그래프 데이터가 없습니다."}

[Vector Data]
{("# Document ".join(vector_data) if vector_data else "관련된 벡터 데이터가 없습니다.")}
"""
    return final_data.strip()


# # 예제 4.23

# In[ ]:


template = """ Use the following context as a primary reference to answer the question:
{context}

Question: {question}
Use natural language and be concise.
Answer:"""

# 프롬프트 템플릿 설정
prompt = ChatPromptTemplate.from_template(template)

# 체인 구성
chain = (
    {
        "context": lambda question: full_retriever(question),  # `full_retriever` 결과를 context로 사용
        "question": RunnablePassthrough()  # 질문 그대로 전달
    }
    | prompt
    | llm  # LLM을 사용하여 최종 응답 생성
    | StrOutputParser()  # 출력 파싱
)


# In[ ]:


chain.invoke(input="저업력 중소기업이 겪는 어려움에 대해 말해줘")


# In[ ]:




