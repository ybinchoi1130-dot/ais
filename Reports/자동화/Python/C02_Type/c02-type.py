#!/usr/bin/env python
# coding: utf-8

# # 02 자료형

# ## 2.1 변수와 상수

# ### 변수 선언하기

# In[1]:


a1 = 2048			# 변수 a1은 숫자를 저장
a2 = "안녕하세요." # 변수 a2는 문자열을 저장


# In[2]:


a = 1024		# 변수 a에 1024를 저장
print (a)		# a를 화면에 출력


# ### 변수명 규칙

# In[3]:


100원 = "백원"					# 변수명을 숫자 100으로 시작하여 에러 발생
email@ = "test@naver.com"	# 변수명에 특수문자 @를 사용하여 에러 발생
my age = 30					# 변수명에 공백을 사용하여 에러 발생
break = 100					# 변수명에 예약어를 사용하여 에러 발생


# ### 상수 사용하기

# In[ ]:


print(20)		# 숫자 상수 20을 화면에 출력
print('A')		# 문자 상수 ‘A’를 화면에 출력
print("선생님")	# 문자열 상수 "선생님"을 화면에 출력


# In[ ]:


x = 3					# 변수 x에 3을 저장
y = x + 2				# 변수 x에 2를 더하여 y에 저장
print(y)				# 변수 y를 화면에 출력

s= "선생님"				# 변수 s에 “선생님” 저장
s = s + ", " + "안녕하세요!"	# 변수 s에 “, “ 와 "안녕하세요!"를 더하여 s에 다시 저장
print(s)				# 변수 s를 화면에 출력


# ## 2.2 기본 자료형

# ### 숫자

# In[ ]:


a = 359  		# 변수 a에 359를 저장
print(type(a))	# a의 자료형을 출력


# In[ ]:


a = 359 		# 변수 a에 359를 저장
a 				# print() 함수를 사용하지 않아도 저장된 값 확인 가능


# In[ ]:


a = -3.619  	# 변수 a에 -3.619를 저장
print(type(a))	# a의 자료형을 출력


# In[ ]:


a = 27  		# 변수 a에 27을 저장
b = 9			# 변수 b에 9를 저장
a + b			# a와 b 더하기, 연산자 + 사용


# In[ ]:


a - b		# a에서 b 빼기, 연산자 - 사용


# In[ ]:


a * b		# a와 b 곱하기, 연산자 * 사용


# In[ ]:


print(a / b)  		# a를 b로 나누었을 때 값 구하기, 연산자 / 사용
print(a // b)		# a를 b로 나누었을 때 몫 구하기, 연산자 // 사용
print(a % b)		# a를 b로 나누었을 때 나머지 구하기, 연산자 % 사용


# In[ ]:


4 ** 3		# 4의 세제곱, 연산자 ** 사용


# In[ ]:


3 + 2 ** 3 / (5-3)


# In[ ]:


abs(-3)			# -3의 절대값을 구함


# In[ ]:


round(3.14159, 3)	# 실수 3.14159를 소수점 넷째 자리에서 반올림하여 셋째 자리까지 출력


# In[ ]:


a = 0o467  		# 8진수 표현
b = 0x7fc		# 16진수 표현
print(a)
print(b)


# ### 문자열

# In[ ]:


a = "Hello Python!"
a


# In[ ]:


type(a)


# In[ ]:


sen = "It's mine." 		# 작은따옴표를 문자열 안에 포함할 때
print(sen)


# In[ ]:


sen2 = '“It is impossible.” He says.' 		# 큰따옴표를 문자열 안에 포함할 때
print(sen2)


# In[ ]:


sen3 = 'It\'s mine.'						# 작은따옴표를 문자열 앞뒤와 안에 사용
sen4 = "\"It is impossible.\" He says." 	# 큰따옴표를 문자열 앞뒤와 안에 사용
print(sen3)
print(sen4)


# In[ ]:


a = """Hello!
Python!"""
print(a)


# In[ ]:


a = "Hello!\nPython!"
print(a)


# In[ ]:


a = "Hello! "
b = "Python!"
print(a + b)		# 문자열 변수인 a와 b를 연결


# In[ ]:


a * 3			# 문자열 변수 a를 3번 반복


# In[ ]:


a = "26"
b = "3"
a + b			# 문자열 변수 a와 b를 연결


# In[ ]:


a * 3			# 문자열 변수 a를 3번 반복


# In[ ]:


a = 26 			# 변수 a에 숫자 자료형(정수) 26을 저장
b ="8" 		# 변수 b에 문자열 자료형 8을 저장
a + b


# In[ ]:


a = "Hello! Python!"


# In[ ]:


a[-1]			# 뒤에서부터 인덱스를 계산, 인덱스 -1의 위치는 ! 


# In[4]:


a[3]			# 뒤에서부터 인덱스를 계산, 인덱스 3의 위치는 l


# In[ ]:


a[3:9]			# 인덱스 3부터 8까지 추출


# In[ ]:


a[3:-4]			# 인덱스 3부터 -5까지 추출


# In[ ]:


a[:8]			# 문자열 처음부터 인덱스 7까지 추출


# In[ ]:


a[3:]			# 인덱스 3부터 문자열 끝까지 추출


# In[ ]:


a = "Life" 					# 변수 a에 문자열 자료형 "Life"를 저장
b = a[0:2] + "v" + a[-1] 	# 슬라이싱 활용
print(b)


# In[ ]:


"I eat %s bananas." %3  # %s 대신 3을 입력해서 값을 출력


# In[ ]:


"I eat %s bananas." %"three" # %s 대신 “three”를 입력해서 값을 출력


# In[ ]:


color = "blue"					# color 변수를 생성
"I like %s color."  %color		# %s 대신 변수 color에 저장된 “blue” 값을 출력


# In[ ]:


ar = "%15s"  %"hello"		# 문자열 길이 15, hello 오른쪽 정렬 
ar


# In[ ]:


ar = "%-15s" % "hello"		# 문자열 길이 15, hello 왼쪽 정렬
ar


# In[ ]:


ar = "John%10s" % "hello"	# John 다음에 공백 10개 추가, hello 오른쪽 정렬
print(ar)


# In[ ]:


a = "%4d"%34				# 공백을 4개 만들고 정수를 오른쪽 정렬 출력
print(a)


# In[ ]:


b = "%10.2f" %5.6182359		# 공백을 10개 만들고 실수를 소수점 둘째 자리까지 오른쪽 정렬 
print(b)


# In[ ]:


test = "I need {} eggs.".format(5)		# format 함수에 있는 값 “5”가 {} 위치에 들어감
print(test)


# In[ ]:


color = "white"
num = 5
test = "I like {} egg. I need {} eggs.".format(color, num)		# 여러 개의 값을 변수로 입력
print(test)


# In[ ]:


a = "{:.2f}".format(5.6182359)	# 소수점 둘째 자리까지 표현(소수점 셋째 자리에서 반올림)
print(a)


# In[ ]:


x = 5.6182359
a = "{:15.2f}".format(x)		# 숫자 길이 15, 오른쪽 정렬, 소수점 둘째 자리까지 표현
print(a)


# In[ ]:


a = "I eat banana."
a.count("n")		# 문자열에서 “n”의 개수 구하기


# In[ ]:


a = "I eat banana."
print(a.find("n"))		# find() 함수 활용, 문자열에서 “n”이 처음 나오는 인덱스 값 구하기
print(a.index("n"))		# index() 함수 활용, 문자열에서 “n”이 처음 나오는 인덱스 값 구하기


# In[ ]:


print(a.find("d"))		# 문자열에서 “d”가 처음 나오는 인덱스 값 구하기
print(a.index("d"))		# 문자열에서 “d”가 처음 나오는 인덱스 값 구하기


# In[ ]:


b = ",".join("fruit")		# join() 함수 안에 있는 문자열의 문자 사이에 “,” 삽입하기
print(b)


# In[ ]:


a = "Hello"
print(a.upper())		# 문자를 전부 대문자로 변경
print(a.lower())		# 문자를 전부 소문자로 변경


# In[ ]:


a = "  Hello  "
print(a.strip()) ; print(a.lstrip()) ; print(a.rstrip()) 


# In[ ]:


a = "I eat banana."
a.split()			# 공백을 기준으로 문자열 나누기


# In[ ]:


a = "a:b:c:d:e"
a.split(':')		# ':'을 기준으로 문자열 나누기


# In[ ]:


a = "I eat banana."
print(a.replace("a", "b", 1))	# 문자열에서 “a”를 “b”로 1회 변경
print(a.replace("a", "b"))		# 문자열에서 “a”를 “b”로 모두 변경


# ### 불

# In[ ]:


print(1 == 1)		# 1과 1이 같은지 판단,  True 출력
print(10 < 8 )		# 10이 8보다 작은지 판단,  False 출력


# In[ ]:


print(bool("python"))		# “python”이라는 문자열이 있으므로 True
print(bool(None))			# None 또는 ““인 경우 False


# ## 2.3 복합 자료형

# ### 리스트

# In[ ]:


a = [ ]									# 공백(띄어쓰기)을 데이터로 갖는 리스트
b = [1, 2, 3, 4, 5]						# 숫자를 데이터로 갖는 리스트
c = ["I", "like", "python"]				# 문자열을 데이터로 갖는 리스트
d = [1, 2, "Python"]					# 숫자와 문자열을 데이터로 갖는 리스트
e = [1, 2, ["Python", "C", "Java"]]		# 숫자와 리스트를 데이터로 갖는 리스트


# In[ ]:


a = [3, 7, 9]
b = [4, 6, 10]
print(a + b)		# 리스트 자료형을 가진 변수 a에 변수 b의 데이터를 추가
print(a * 3)		# 리스트 자료형을 가진 변수 a의 데이터를 세 번 반복


# In[ ]:


test = [75, 69, 95, 84, 89]
food = ["milk", "juice", "rice", "soup", "cookie"]
print(test[2])			# 인덱스가 0부터 시작하기 때문에 3번째 데이터인 95를 출력
print(food[3:5])		# 인덱스 3~4에 있는 데이터인 ‘soup’, ‘cookie’를 출력


# In[ ]:


a = [1, 2, ["Python", "C", "Java"]]		# 숫자와 리스트를 데이터로 갖는 리스트(중첩 리스트)
print(a[2])			# 변수 a에 저장된 데이터 중 3번째 데이터를 출력
print(a[2][:2])		# 출력된 3번째 데이터에서 처음부터 인덱스 1까지 슬라이싱 


# In[ ]:


a = [1, 3, 5, 7, 6, 2, 4]
a[3] = 8			# 변수 a의 인덱스 3 데이터를 8로 변경
print(a)


# In[ ]:


a = [1, 3, 5, 7, 6, 2, 4]
del a[3]			# 변수 a의 인덱스 3 데이터 삭제
print(a)


# In[ ]:


a = [1, 2, 3, 4]
a.append(3)			# 변수 a의 마지막 위치에 3을 추가
print(a)


# In[ ]:


a.append([3, 5, 9])		# 변수 a에 리스트를 추가
print(a)


# In[ ]:


a = [1, 2, 3, 4]
a.insert(0, 7)		# 변수 a의 인덱스 0 위치에 7을 추가
print(a)


# In[ ]:


a = [1, 2, 3, 4, 5, 4, 3, 2, 1]
a.remove(4)			# remove(x)는 리스트에서 첫 번째로 일치하는 x를 삭제
print(a)


# In[ ]:


a = [1, 3, 5, 7, 6, 2, 4]
a.sort()					# 변수 a의 데이터를 오름차순 정렬
print(a)


# In[ ]:


a = [1, 3, 5, 7, 6, 2, 4]
a.sort(reverse=True)		# 변수 a의 데이터를 내림차순 정렬
print(a)


# In[ ]:


a = [1, 3, 5, 7, 6, 2, 4]
a.reverse()					# 변수 a의 데이터 순서 뒤집기
print(a)


# In[ ]:


a = [1, 3, 5, 7, 6, 2, 4]
print(a.pop())		# 변수 a의 마지막 데이터를 보여준 다음 삭제
print(a)


# In[ ]:


a = [1, 3, 5, 7, 6, 2, 4]
print(a.pop(3))		# 변수 a의 인덱스 3 데이터를 보여준 다음 삭제
print(a)


# In[ ]:


a = [1, 3, 5, 7, 6, 2, 4]
a.extend([3, 5, 7])		# 변수 a에 3, 5, 7을 추가함
print(a)


# In[ ]:


a = [1, 3, 5, 7, 6, 2, 4]
b = [3, 5, 7]
a.extend(b)		# 변수 a에 변수 b 데이터를 추가함
print(a)


# ### 튜플

# In[ ]:


tp1 = ( )
tp2 = (1, )				# 데이터가 하나만 있는 튜플을 만들 경우 데이터 뒤에 ,(쉼표) 필수 입력
tp3 = (1, 2, 3)
tp4 = 1, 2, 3 			# 괄호 () 생략 가능
tp5 = ("a", "b", ("ab", "cd"))


# In[ ]:


tp1 = (1, 2, 3, "a", "b", "c")
tp2 = (4, 5, 6)
print(tp1 + tp2)		# 튜플 자료형을 가진 변수 tp1과 tp2의 데이터를 합치기
print(tp2 * 2)			# 튜플 자료형을 가진 변수 tp2의 데이터를 두 번 반복하기


# In[ ]:


tp = (1, 2, ("ab", "cd", "ef"), 3, "a", "b", "c")	# 숫자, 문자열, 튜플을 데이터로 갖는 튜플
print(tp[2])			# 변수 tp에 저장된 데이터 중 3번째 데이터를 출력 
print(tp[2][:2])		# 변수 tp의 3번째 데이터에서 처음부터 인덱스 1까지 슬라이싱 


# ### 딕셔너리

# In[ ]:


dict1 = {"name" : "Lee", "age" : 29, "birth" : "0320"}	# 예시
dict2 = {1 : "ab"}					# Key에 정수형, Value에 문자열 자료형을 입력한 예
dict3 = {"test" : [1, 3, 5, 7]}		# Value에 리스트 자료형을 입력한 예


# In[ ]:


dict4 = {"a" : [1, 2], "b" : [3, 4], "c" : [5, 6]}
print(dict4["a"])


# In[ ]:


dict5 = {"a" : [1, 2]}
dict5["b"] = [3, 4]		# 변수 dict5에 Key:Value가 "b" : [3, 4]인 딕셔너리 쌍 추가
print(dict5)


# In[ ]:


dict6 = {"a" : [1, 2], "b" : [3, 4], "c" : [5, 6]}
del dict6["c"]			# Key "c"에 해당하는 Value [5, 6]을 삭제하면 Key : Value 쌍이 삭제됨
print(dict6)


# In[ ]:


del dict
list1 = [["a", 2], ["b", 4], ["c", 6]]
dict(list1)				# 중첩 리스트로 구성된 자료형을 딕셔너리로 변경


# In[ ]:


list2 = [("a", 2), ("b", 4), ("c", 6)]
dict(list2)				# 리스트 내 튜플로 구성된 자료형을 딕셔너리로 변경


# In[ ]:


tp1 = (["a", 2], ["b", 4], ["c", 6])
dict(tp1)				# 튜플 내 리스트로 구성된 자료형을 딕셔너리로 변경


# In[ ]:


tp2 = (("a", 2), ("b", 4), ("c", 6))
dict(tp2)				# 중첩 튜플로 구성된 자료형을 딕셔너리로 변경


# In[ ]:


a = 3 		# 변수 a에 정수형 자료 저장
float(a) 	# 변수 a를 실수형으로 변환


# In[ ]:


a = 3.619	# 변수 a에 실수형 자료 저장
int(a)		# 변수 a를 정수형으로 변환(소수점 자리는 버림)


# In[ ]:


b = [1, 2, 3, 4, 5]		# 변수 b에 리스트 자료 저장
tuple(b)				# 변수 b를 튜플형으로 변환


# In[ ]:


dict(b)	 	    # 변수 b가 쌍으로 구성되지 않았기 때문에 딕셔너리로 변경 시 에러 발생


# In[ ]:


a = 5									# 정수
b = 3.14								# 실수
c = "love"								# 문자열
d = True								# 불
e = [1, 2, 3, 4, 5]						# 리스트
f = (6, 7, 8, 9, 10)					# 튜플
g = {"name":"park","number":"505"} 		# 딕셔너리
print(type(a),type(b))
print(type(c),type(d))
print(type(e),type(f),type(g))


# In[ ]:


dict1 = {"name" : "Lee", "age" : 29, "birth" : "0320"}
print(dict1.keys())			# 변수 dict1의 Key만 모아서 출력
print(list(dict1.keys()))	# 변수 dict1의 Key만 모인 객체를 리스트로 출력


# In[ ]:


list(dict1.values())		# 변수 dict1의 Value만 모인 객체를 리스트로 출력


# In[ ]:


dict2 = {"name" : "Lee", "age" : 29, "birth" : "0320"}
dict2.items()		# 변수 dict2의 Key와 Value 쌍을 튜플로 출력


# In[ ]:


dict3 = {"name" : "Lee", "age" : 29, "birth" : "0320"}
dict3.clear()		# 변수 dict3 안의 모든 쌍을 삭제
print(dict3)


# In[ ]:


dict3 = {"name" : "Lee", "age" : 29, "birth" : "0320"}
print("name" in dict3)		# 변수 dict3 안에 "name" Key가 있으면 True, 없으면 False


# ### 집합

# In[ ]:


set1 = set([1, 2, 5, 3, 7, 4])
print(set1)						# 숫자로 된 리스트의 집합 자료형은 분해되면서 오름차순으로 출력됨


# In[ ]:


set2 = set("school bus")		# 문자열의 경우 문자로 분해되고 중복 문자는 제거됨
print(set2)						# 집합 자료형은 순서를 가지지 않으므로 랜덤으로 출력됨


# In[ ]:


set1 = set([1, 2, 3, 4, 5, 6, 7])
set2 = set([5, 6, 7, 8, 9, 10, 11])
print(set1 & set2)				# 교집합(두 집합의 공통 데이터)
print(set1.intersection(set2))	# 교집합(set2.intersection(set1)과 결과는 동일)


# In[ ]:


print(set1 | set2)			# 합집합(두 집합의 전체 데이터), |은 [shift] + [\]
print(set1.union(set2))		# 합집합(set2.union(set1)과 결과는 동일)


# In[ ]:


print(set1 - set2)				# 차집합(set1에 포함되나 set2에 포함되지 않는 집합)
print(set1.difference(set2))	# 차집합(set2.difference(set1)과 결과는 다름)


# In[ ]:


print(set2 - set1)		# 차집합(set2에 포함되나 set1에 포함되지 않는 집합)
print(set2.difference(set1))	# 차집합(set1.difference(set2)과 결과는 다름)


# In[ ]:


set1 = set([1, 2, 3, 5])
set1.add(4)
set1


# In[ ]:


set2 = set([1, 2, 3, 4, 5])
set2.update([6, 7, 8])
set2


# In[ ]:


set3 = set([1, 2, 3, 4, 5])
set3.remove(3)
set3

