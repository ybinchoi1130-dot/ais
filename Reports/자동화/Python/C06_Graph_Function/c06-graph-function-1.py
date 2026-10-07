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


#%%

# THE END

