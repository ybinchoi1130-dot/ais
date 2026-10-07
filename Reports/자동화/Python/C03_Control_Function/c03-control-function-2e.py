#!/usr/bin/env python
# coding: utf-8

# # 03 제어문과 함수

# ##  3.1 제어문

# ### if 문

# In[1]:


x = 10	# 변수 x에 10을 입력
y = 5	# 변수 y에 5를 입력
x > y	# x가 y보다 큰 값인지 비교


# In[2]:


x == y	# x와 y가 같은 값인지 비교 


# In[3]:


x != y	# x와 y가 다른 값인지 비교 


# In[4]:


x = True	# 변수 x에 True 입력
y = False	# 변수 y에 False 입력
x or y		# x와 y값 중 하나라도 참이면 True를 출력


# In[5]:


x and y		# x와 y값 모두가 참이 아니면 False를 출력


# In[6]:


10 in [10, 20, 30]		# 리스트 [10, 20, 30]에 10이 있으면 참 


# In[7]:


"x" not in ("x", "y", "z")		# 튜플 ("x", "y", "z")에 "x"가 없으면 참 


# In[8]:


x = 3				# 변수 x에 3을 대입
if x % 2 == 0:		# x를 2로 나눈 나머지 값과 0을 비교
    print("짝수")		# 조건문이 참일 때 실행
else:
    print("홀수")		# 조건문이 거짓일 때 실행 


# In[9]:


pass_list = ["이순신", "을지문덕", "연개소문", "강감찬"]  #리스트로 저장
name = "강감찬"
if name in pass_list :
    print (name + "님은 합격입니다.")
else :
    print (name + "님은 불합격입니다.")


# In[10]:


x = 55
if x >= 70:			# x가 70보다 작으므로 조건문의 값은 거짓
    print ("양호")
elif x >= 40:		# x가 40보다 크므로 조건문의 값은 참
    print ("보통")
else :
    print ("불량")


# In[11]:


if x >= 80:
    msg = "합격"
else:
    msg = "불합격"


# In[12]:


msg = "합격" if x >= 80 else "불합격"


# ### while 문

# In[13]:


i = 1
result = 0
while i < 101:      	# i가 101보다 작을 동안 계속해서 반복
    result = result + i
    i = i + 1
print("1 + 2 + ... + 99 + 100 =", result)


# In[14]:


egg = 2
while True:						# 무한 반복
    egg = egg -1
    print("남은 계란은 %d개입니다." % egg)
    if egg == 0:				# egg가 0일 때 print() 실행
        print("계란이 없습니다.")
        break


# In[15]:


i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0: continue		# i가 짝수일 경우 while 문의 처음 코드로 돌아감
    print(i)


# In[ ]:


while True:			# 조건문이 True이므로 항상 참
    print("Ctrl+C를 눌러야 빠져나갈 수 있습니다.")


# ### for 문

# In[ ]:


web_list = ["네이버", "구글", "다음"] 
for a in web_list: 		# 변수 a에 "네이버", "구글", "다음"이 차례로 대입됨
    print(a)


# In[ ]:


a = [(3, 6), (4, 5), (3, 8)]
for (x, y) in a:		# 변수(x, y)에 (3, 6), (4, 5), (3, 8)이 차례로 대입됨  
    print(x * y)		# x와 y를 곱하고 출력


# In[ ]:


a = list(range(1, 10))		# 1부터 9까지 숫자 리스트 생성
b = list(range(1, 10, 2))	# 1~9에서 2씩 증가하는 숫자 리스트 생성
c = list(range(10, 1, -1))	# 10~2에서 -1씩 감소하는 숫자 리스트 생성
print(a, b, c)


# In[ ]:


result = 0
for a in range(1, 100, 2):		# 1~99에서 2씩 증가, 홀수 리스트를 생성
    result = a + result				# 변수 result에 홀수를 차례로 더함
print(result) 


# In[ ]:


for x in range(2, 8):  				# x에 2부터 7까지 대입
    for y in range(2,7):			# y에 2부터 6까지 대입
        print("%d X %d = %d"%(x, y, x * y), "\t", end="")	# x, y, x * y 출력, tab으로 간격 조정
    print(" ")						# 줄 바꾸기


# In[ ]:


scores = [(1, 83),(2, 66),(3, 55),(4, 70), (5, 50)]
for num, score in scores:  			# num과 score에 튜플 데이터를 대입
    if score < 60:					# score가 60보다 작을 경우 continue 실행
        continue 
    print("%d번 학생 축하합니다." %num)	# score가 60보다 크거나 같을 경우 print() 실행


# ## 3.2 함수와 클래스

# ### 함수 만들기

# In[1]:


def summation(a, b):			# summation() 함수 정의, 매개변수 a, b
    result = a+b
    return result		# result를 결과값으로 전달

print(summation(10,20))		# summation() 함수 호출, 10과 20은 매개변수로 전달되는 인수


# In[ ]:


def mul(x, y):			# mul() 함수 정의, 매개변수 x, y
    res = x * y
    return res			# res를 결과값으로 전달

print(mul(100, 2))		# mul() 함수 호출, 100과 2는 매개변수로 전달되는 인수


# In[ ]:


def good( ):		# good() 함수 정의, 매개변수 없음
    return "안녕하세요! 반갑습니다."

print(good( ))		# good() 함수 호출


# In[ ]:


def test(a):		# test() 함수 정의
    if a >= 60:		# a가 60 이상이면  "합격을 축하드립니다." 출력
        print("합격을 축하드립니다.")
    else:			# a가 60 미만이면 "불합격입니다.ㅠㅠ" 출력
        print("불합격입니다.ㅠㅠ")
test(55)


# In[ ]:


def sayhello( ):		# sayhello() 함수 정의
   print("안녕하세요! 반갑습니다.")  

sayhello()				# 함수 호출


# In[ ]:


a = 1
def test(a):		# test() 함수 정의
    a = a + 1
    return a
test(a)				# test() 함수 호출
print(a)


# ### 입력과 출력 함수

# In[ ]:


test = input()


# In[ ]:


print(test)


# In[ ]:


type(test)


# In[ ]:


input("저장하고 싶은 값을 입력하세요:")


# In[ ]:


print("I" "eat" "5" "eggs.")	# 공백 사용했지만 출력값 사이에 공백 없이 출력됨


# In[ ]:


print("I", "eat", "5", "eggs.")	# 콤마(,) 사용 시 출력값에 공백 추가됨, 숫자 입력 가능


# In[ ]:


print("I"+"eat"+"5"+"eggs.")    # 더하기 기호(+)는 같은 자료형끼리만 사용 가능


# In[ ]:


print("I", end =" ")			# "" 사이에 공백 입력
print("eat", end =" ")
print(5, end =" ")
print("eggs.", end =" ")


# In[ ]:


num = input()


# In[ ]:


print(num)


# In[ ]:


type(num)


# In[ ]:


num2 = int(num)
type(num2)


# ### 외부 파일 읽고 쓰기

# In[ ]:


f = open("A lucky day.txt", "r")		# 현재 경로에서 “A lucky day.txt”를 읽기 모드로 열기
f.close()					# 파일 닫기


# In[ ]:


f = open("A lucky day.txt", "w")		# 현재 경로에서 “A lucky day.txt”를 쓰기 모드로 열기
f.close()					# 파일 닫기


# In[ ]:


f = open("A lucky day.txt", "w")		# 파일 열기
f.write("""새침하게 흐린 품이 눈이 올 듯하더니 눈은 아니 오고 얼다가 만 비가 추적추적 내리었다.
이날이야말로 동소문 안에서 인력거꾼 노릇을 하는 김 첨지에게는
오래간만에도 닥친 운수 좋은 날이었다.""")
f.close()					# 파일 닫기


# In[ ]:


fr = open("A lucky day.txt", "r")		# 파일 읽기 모드로 열기
line = fr.readline()					# 파일 내용 한 줄 출력
print(line)								# 한 줄 출력
fr.close()


# In[ ]:


fr1 = open("A lucky day.txt", "r")		# 파일 읽기 모드로 열기
print(fr1.read())						# 파일 내용 전체 출력
fr1.close()


# In[ ]:


fr4 = open("A lucky day.txt", "a")		# 파일 추가 모드로 열기
fr4.write("""
문안에(거기도 문밖은 아니지만) 들어간답시는 앞집 마나님을
전찻길까지 모셔다 드린 것을 비롯으로
행여나 손님이 있을까 하고 정류장에서 어정어정하며 내리는 사람 하나하나에게
거의 비는 듯한 눈결을 보내고 있다가
마침내 교원인 듯한 양복장이를 동광학교(東光學校)까지 태워다 주기로 되었다.""")
fr4.close()


# In[ ]:


fr4 = open("A lucky day.txt", "r")		# 파일 읽기 모드로 열기
print(fr4.read())						# 파일 내용 전체 출력
fr4.close()


# ### 내장 함수

# In[ ]:


abs(-5)


# In[ ]:


abs(2) == abs(-2)	# abs(2)와 abs(-2)는 같은 절대값을 가짐


# In[ ]:


for i in range(97, 123): print(chr(i), end=" ")  # for 문을 활용해 유니코드 97~122 문자 출력


# In[ ]:


for i in ["a", "b", "c", "d"]: print(ord(i), end=" ")  # "a", "b", "c", "d"의 유니코드 출력


# In[ ]:


for i, item in enumerate(["사과", "참외", "수박"]):  print(i, item)
# 리스트 문자열을 입력받아 인덱스는 변수 i에, 문자열은 변수 item에 대입


# In[ ]:


int("8")	# 문자열 8을 숫자 8로 반환


# In[ ]:


int(2.3)	# 숫자 2.3을 2로 반환


# In[ ]:


len("대한민국")	# 문자열의 길이를 반환


# In[ ]:


len([1,2,3,4,5,6,7])	# 리스트의 요소 수를 반환


# In[ ]:


test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max(test), min(test)	# 변수 test의 최대값과 최소값을 반환


# In[ ]:


pow(3, 2) 		# 3의 2제곱


# In[ ]:


pow(2, 10) 		# 2의 10제곱


# In[ ]:


round(32.3132, 2)	# 소수점 둘째 자리까지 반올림하여 반환


# In[ ]:


round(24.3788, 3)	# 소수점 셋째 자리까지 반올림하여 반환


# In[ ]:


sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])	# 리스트 요소를 모두 더함


# In[ ]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
avg = sum(a)/len(a)		 # sum()과 len() 함수를 이용해 리스트의 평균을 구함
print(avg)


# In[ ]:


sorted((3, 1, 4, 5, 2)), sorted((3, 1, 4, 5, 2), reverse = True)	# 튜플을 오름차순과 내림차순으로 정렬


# In[ ]:


sorted([3, 1, 4, 5, 2])		# 리스트를 오름차순으로 정렬


# In[ ]:


sorted("대한민국"), sorted(["b", "c", "a"])		#문자열은 글자를 분리하여 정렬, 리스트 문자열은 요소로 정렬


# ### 클래스와 객체

# In[ ]:


class message :							# 클래스 선언
    sayhello = "안녕하세요. 반갑습니다."		# 클래스 멤버변수
    goodbye = "감사합니다. 안녕히 가십시오."		# 클래스 멤버변수
    def __init__(self, name):			# 객체가 생성될 때 자동으로 호출, 초기화
        self.name = name 
    def hello(self):				# hello() 메소드 선언
        print(self.name, "님,", self.sayhello)		# 전달받은 변수와 intro 메시지 출력
    def bye(self) :					# bye() 메소드 선언
        print(self.name, "님,", self.goodbye)	# 전달받은 변수와 bye 메시지 출력


# In[ ]:


kim = message("김온달")		# kim 객체 생성, name변수에 "김온달" 저장
lee = message("이평강")		# lee 객체 생성, name 변수에 "이평강" 저장

kim.hello()					# kim 객체에서 message 클래스의 hello(), bye() 메소드 호출
kim.bye()


# In[ ]:


lee.hello()			# lee 객체에서 message 클래스의 hello(), bye() 메소드 호출
lee.bye()

