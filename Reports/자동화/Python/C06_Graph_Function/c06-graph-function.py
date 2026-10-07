#!/usr/bin/env python
# coding: utf-8

# # 06 그래프 함수로 시각화하기

# ## 6.1 matplotlib으로 그래프 그리기 

# ### matplotlib 그래프 종류

#%%

# 그래프 모듈 설치
# pip install matplotlib

# In[1]:


import matplotlib.pyplot as plt					# matplotlib을 plt라는 이름으로 불러오기
plt.rcParams["font.family"] = "Malgun Gothic"	# 그래프에서 한글 폰트 깨짐 방지


# ### 선 그래프

# In[2]:


plt.plot([1,10], [1,1], linestyle = "solid")	# 실선(line)
plt.plot([1,10], [2,2], linestyle = "dashed")	# 파선(dash)
plt.plot([1,10], [3,3], linestyle = "dashdot")	# 쇄선(dashdot)
plt.plot([1,10], [4,4], linestyle = "dotted")	# 점선(dot)


# In[3]:


# 선 그래프 그리기
height = [155, 160, 163, 167, 170, 174, 178, 182, 186, 190]		# 키 데이터
weight = [44, 46, 48, 50, 57, 62, 70, 74, 79, 82]				# 몸무게 데이터
plt.title("선 그래프")											# 제목
plt.xlabel("몸무게")											# x축 제목
plt.ylabel("키")												# y축 제목
plt.plot(weight, height, color = "red", lw = 3)				# 선 그래프 그리기, 컬러 적색, 선 두께 3
plt.show()													# 그래프 출력


# In[4]:


height = [155, 160, 163, 167, 170, 174, 178, 182, 186, 190]		# 키 데이터
weight = [44, 46, 48, 50, 57, 62, 70, 74, 79, 82]				# 몸무게 데이터
plt.title("스캐터 플랏")											# 제목
plt.xlabel("몸무게")											# x축 제목
plt.ylabel("키")												# y축 제목
plt.scatter(weight, height)									# 스캐터 플랏 그리기
plt.show()													# 그래프 출력


# ### 막대 그래프

# In[5]:


# 막대 그래프 그리기
x = ["사과", "포도", "딸기"]			# 항목 데이터
y = [12, 31, 24]				# 빈도(크기) 데이터
plt.title("과일 생산량")			# 그래프 제목
plt.bar(x, y, color = "lightblue", width = 0.5)	# 색상은 밝은 파랑, 그래프 폭은 0.5로 지정
plt.xlabel("과일 종류")			# x축 제목
plt.ylabel("판매량")			# y축 제목
plt.ylim(0, 40)				# y축 범위 지정
plt.show()					# 그래프 출력


# ### 원 그래프

# In[6]:


# 원 그래프 그리기
x = ["사과", "포도", "딸기", "참외"]				# 항목 데이터
y = [12, 31, 24, 46]							# 비율 데이터
colors = ["coral", "cornsilk", "pink", "aqua"]	# 항목별 컬러 지정
plt.title("원 그래프")							# 파이 차트 제목
plt.pie(y, labels = x, autopct = "%1.1f%%", colors = colors, shadow = True) # 그래프 설정
plt.show()									# 그래프 출력


# In[7]:


x = ["사과", "포도", "딸기", "참외"]		# 항목 데이터
y = [12, 31, 24, 46]					# 비율 데이터
colors = ["coral", "cornsilk", "pink", "aqua"]	# 항목별 컬러 지정
plt.title("원 그래프")					# 파이 차트 제목
plt.pie(y, labels = x, autopct = "%1.1f%%", colors = colors, explode = (0.1, 0, 0, 0), shadow = True) 
plt.show()							# 그래프 출력


# ### 히스토그램

# In[8]:


# 히스토그램 그리기
x = [18, 4, 10, 22, 19, -10, 10, -2, -1, 4, 1, 15, 8, 1, 4, 3, 15, -2, 3,- 9, -26, 7, 9, -7, 23, -15, 0, -2, 15, 15]
plt.title("Histogram")			# 그래프 제목 지정
plt.grid(True)					# 격자 출력
plt.hist(x, bins = 10, color = "lightgreen")	# 히스토그램 설정, 계급 구간을 10으로 지정
plt.show()				# 그래프 출력


# ### 상자 수염 그래프

# In[9]:


# 상자 수염 그래프 그리기
x = [55, 60, 63, 67, 70, 74, 78, 66, 64, 73, 106]
plt.boxplot(x, sym = "bo", vert = 1)
plt.show()		# 그래프 출력


# In[10]:


# 산점도와 선 그래프 함께 그리기
height = [155, 160, 163, 167, 170, 174, 178, 182, 186, 190]		# 키 데이터
weight= [44, 46, 48, 50, 57, 62, 70, 74, 79, 82]				# 몸무게 데이터
plt.title("선 그래프")											# 제목
plt.xlabel("몸무게")											# x축 제목
plt.ylabel("키")												# y축 제목
plt.plot(weight, height, color = "blue", lw = 1)			# 선 그래프, 청색, 선 두께 1
plt.scatter(weight, height, color = "red", s = 100)			# 산점도, 적색, 크기 100
plt.show()


# ## 6.2 pandas로 그래프 그리기

# ###  실습 데이터 불러오기

# In[11]:


import pandas as pd					   # pandas 불러오기
import matplotlib.pyplot as plt		   # matplotlib 불러오기

plt.rcParams["font.family"] = "Malgun Gothic" # 그래프에서 한글 폰트 깨짐 방지 
graph = pd.read_excel(r"./그래프 실습2.xlsx", sheet_name = "Sheet1")
graph.head(10)		# 총 30행으로 구성, 상위 10행만 출력


# ### 선 그래프

# In[12]:


# 국어, 영어 열을 선택하여 선 그래프 그리기
graph.plot(y = ["국어", "영어"], grid = True, title = "선 그래프", color = ["green", "red"])
plt.show()


# In[13]:


# 반별 영어 점수 산점도 그리기
graph.plot.scatter(x = "반", y = "영어", color = "red", title = "영어 점수 산점도")
plt.show()


# ### 막대 그래프

# In[14]:


# 과목별 점수 데이터의 평균값으로 막대 그래프 그리기
graph.iloc[:, 2:7].mean().plot.bar(grid = True, title = "과목별 평균 점수", color = "orange", ylabel = "평균")
plt.show()


# In[15]:


# 과목별 점수 데이터의 평균값으로 수평 막대 그래프 그리기
a = graph.iloc[:, 2:7].mean().plot.barh(grid = True, color = "blue")
a.set_xlabel("평균")
a.set_title("과목별 평균 점수")
plt.show()


# ### 원 그래프

# In[16]:


# 반별 인원수로 원 그래프 그리기
class_c = graph.groupby("반").size()			# 반별 인원수를 카운트해서 class_c에 저장
class_c.plot.pie(title = "반별 인원수 분포", ylabel = "반", autopct = "%1.1f%%", explode = (0.1, 0, 0)
, shadow = True)
plt.show()


# In[17]:


# 과일 판매량으로 원 그래프 그리기
fruit = ["사과", "포도", "딸기", "참외"] 		# 과일 종류 데이터
sales = [12, 31, 24, 46] 					# 판매량 데이터
df = pd.Series(sales, index = fruit)		# pd.Series 자료형 생성

df.plot.pie(title="과일 판매량", ylabel = "과일", autopct = "%1.1f%%", explode = (0.1, 0, 0, 0)
, shadow = True)
plt.show()


# ### 히스토그램

# In[18]:


# 영어 점수 히스토그램 그리기
a = graph["영어"].plot.hist(bins = 20, color = "lightblue", edgecolor = "red", grid = True, title = "히스토그램")
a.set_xlabel("영어 점수"), a.set_ylabel("빈도 수")
plt.show()


# In[19]:


# 사회, 과학 점수 분포 시각화
graph["사회"].plot.hist(bins = 20, color = "blue", edgecolor = "blue", alpha = 0.5, title = "히스토그램")
graph["과학"].plot.hist(bins = 20, color = "red", edgecolor = "red", alpha = 0.5, grid = True)
plt.show()


# ### 상자 수염 그래프

# In[20]:


# 상자 수염 그래프 그리기
graph.boxplot(column = ["국어"], by = "반")
plt.show()

#%%

# THE END