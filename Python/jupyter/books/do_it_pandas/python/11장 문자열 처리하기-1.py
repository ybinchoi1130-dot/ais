#!/usr/bin/env python
# coding: utf-8

# ## 11-1 문자열 다루기

# In[1]:


word = 'grail'     # 잔
sent = 'a scratch' # 긁다


# ### 인덱스로 문자열 추출하기

# #### [Do It! 실습] 문자 추출하기

# ##### 1. 문자 1개 추출하기

# In[2]:

# 'grail'
print(word[0]) # 'g'


# In[3]:

# 'a scratch'   
print(sent[3]) # 'c'


#%%

# ##### 2. 문자 여러 개 추출하기

# In[4]:

# 'grail'
print(word[0:3]) # gra


#%%
# #### [Do It! 실습] 음수 인덱스로 추출하기

# In[5]:

# 맨 마지막 요소
# 'a scratch'
print(sent[-1]) # 'h'


# In[6]:

# 'a scratch'
# -9(0) ~ -8(1)
print(sent[-9:-8]) # 'a'

# In[7]:

print(sent[0:-8]) # 'a'


# In[8]:

# 'a scratch'
# 2부터 맨마지막 바로전 요소까지
print(sent[2:-1]) # 'scratc'


# In[9]:

# 'a scratch'
# -7(2) ~ -1
print(sent[-7:-1]) # scratc


#%%

# ### 슬라이싱 구문으로 마지막 문자 추출하기

# In[10]:

# 'a scratch'
s_len = len(sent)
print(s_len) # 9


# In[11]:

# 2부터 끝까지
print(sent[2:s_len])

#%%
# #### [Do It! 실습] 슬라이딩 구문에서 왼쪽이나 오른쪽 인덱스를 지정하지 않고 문자 추출하기

# In[12]:

# 'grail'
print(word[0:3]) # gra


# In[13]:

# 0부터 3이전까지
print(word[ :3]) # gra


# In[14]:

# 2부터 끝까지
# 'a scratch'
print(sent[2:len(sent)]) # scratch


# In[15]:

# 'a scratch'
print(sent[2: ]) # scratch


# In[16]:

# 전체
print(sent[ : ]) # a scratch


#%%

# #### [Do It! 실습] 슬라이싱 간격 설정하기

# In[17]:

# 스텝(step)
# 전체에서 2스텝
# 'a scratch'
print(sent[::2]) # 'asrth'


# In[18]:

# 전체에서 3스텝
# 'a scratch'
print(sent[::3]) # 'act'

#%%

# ## 11-2 문자열 메서드

# In[19]:

# 첫 번재 문자만 대문자로 변환하고 나머지는 소문자료 변환
print("black Knight".capitalize())  # Black knight

#%%

# 문자열의 갯수
print("It's just a flesh wound!".count('u')) # 2

#%%

# 문자열이 특정 문자로 시작하면 True
print("Halt! Who goes there?".startswith('Halt')) # True

#%%

# 문자열이 특정 문자로 끝나면 True
print("coconut".endswith('nut')) # True

#%%

# 찾을 문자열의 첫 번째 인덱스를 리턴하며 실패 시 -1
print("It's just a flesh wound!".find('u'))    # 6
print("It's just a flesh wound!".find('x'))    # -1
print("It's just a flesh wound!".find('just')) # 5

# 찾을 문자열의 첫 번째 인덱스를 리턴하며 실패 시 예외(ValueError)
# 오류: ValueError: substring not found
# print("It's just a flesh wound!".index('scratch'))
print("It's just a flesh wound!".index('flesh'))   # 12

#%%

# 모든 문자열이 알파벳이면 True
# 유니코드(unicode)도 문자(Letter)에 해당하므로 
# 알파벳과 동일하게 취급
print("oldwoman".isalpha())  # True
print("old woman".isalpha()) # False: Space(공백)이 포함 됨
print("1234".isalpha())      # False

print("유니코드")
print("한글".isalpha())      # True
print("漢字".isalpha())      # True

print("특수문자")
print(" ".isalpha())       # False
print("!".isalpha())       # False
print("@".isalpha())       # False
print("#".isalpha())       # False
print("$".isalpha())       # False
print(".".isalpha())       # False

#%%

# isascii: 특수문자, 영어 알파벳
print("abcd".isascii()) # True
print("ABCD".isascii()) # True
print("1234".isascii()) # True
print("!@#$".isascii()) # True

print("유니코드")
print("한글".isascii()) # False
print("漢字".isascii()) # False

#%%

# 순수 알파벳만 검사하려면?
# 제외: 다국어, 특수문자
alphabet = "abcdABCD"
unicode = "한글漢字"
special = "!@#$"

print(alphabet, ':', alphabet.isalpha() and alphabet.isascii()) # True
print(unicode, ':', unicode.isalpha() and unicode.isascii())    # False
print(special, ':', special.isalpha() and special.isascii())    # False


#%%

print("37".isdecimal())    # True
print("I'm 37".isalnum())  # False
print("Black Knight".lower()) # black knight
print("Black Knight".upper()) # BLACK KNIGHT
print("flesh wound!".replace('flesh wound', 'scratch')) # scratch!
print("  I'm not dead.  ".strip()) # I'm not dead.
print("NI! NI! NI! NI!".split(sep=' ')) # ['NI!', 'NI!', 'NI!', 'NI!']
print("3,4".partition(',')) # ('3', ',', '4')

#%%

# 지정한 너비로 문자열을 늘리고 가운데 정렬
# 총 10자리 문자열
print('[1234567890]')
print('[', "nine".center(10), ']', sep='')
# [1234567890]
# [   nine   ]

#%%

# 문자열 빈칸을 '0'으로 채움
# 전체: 5자리에서 남은 빈칸을 0으로 채움
# zfill: zero fill
print("9".zfill(5)) # 00009

#%%

# ## 11-3 문자열 메서드 더 알아보기

# #### [Do It! 실습] join() 메서드

# In[20]:


d1 = '40°' 
m1 = "46'" 
s1 = '52.837"' 
u1 = 'N'

d2 = '73°' 
m2 = "58'" 
s2 = '26.302"' 
u2 = 'W'

# 리스트의 각 요소를 결합하여 하나의 문자열로 만드는데 
# 각 요소의 사이에 빈칸으로 연결
coords = ' '.join([d1, m1, s1, u1, d2, m2, s2, u2])
print(coords) # 40° 46' 52.837" N 73° 58' 26.302" W

#%%

# 콤마(,)로 연결
print(','.join([d1, m1, s1, u1, d2, m2, s2, u2]))
# 40°,46',52.837",N,73°,58',26.302",W


# In[21]:

# 분할: 문자열을 빈칸으로 분할(split)하여 리스트로 요소를 구성 리턴
coords_list = coords.split(" ")
print(type(coords_list)) # <class 'list'>
print(coords_list) # ['40°', "46'", '52.837"', 'N', '73°', "58'", '26.302"', 'W']

#%%

# #### [Do It! 실습] splitlines() 메서드

# In[22]:

# 멀티 라인 문자열(다중 라인 문자열)
multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together.
""" 
print(multi_str)


# In[23]:

# 줄 바꿈(엔터)를 기준으로 분할하여 리스트로 리턴
multi_str_split = multi_str.splitlines()
print(multi_str_split) # len: 5

#%%

# 맨 마지막 뒤(\n)에 문자열이 없으면 무시
"""
[
 'Guard: What? Ridden on a horse?', 
 'King Arthur: Yes!', 
 "Guard: You're using coconuts!", 
 'King Arthur: What?', 
 "Guard: You've got ... coconut[s] and you're bangin' 'em together. "
]
"""
#%%

# 문자열(multi_str)의 맨 마지막 라인의 엔터(\n)를 기준으로 양쪽으로 분할
multi_str_split2 = multi_str.split('\n') 
print(multi_str_split2) # len: 6

#%%

# 맨 마지막 뒤(\n)에 문자열이 없어도 분할에 포함
"""
[
 'Guard: What? Ridden on a horse?', 
 'King Arthur: Yes!', 
 "Guard: You're using coconuts!", 
 'King Arthur: What?', 
 "Guard: You've got ... coconut[s] and you're bangin' 'em together. ", 
 ''  
]
"""

# In[24]:


guard = multi_str_split[::2] 
print(guard)


# In[25]:

guard = multi_str.replace("Guard: ", "").splitlines()[::2] 
print(guard)

#%%%

# 원본 문자열을 .replace("Guard: ", "") 한 후
# splitlines으로 분할만 한 경우
"""
[
 'What? Ridden on a horse?', 
 'King Arthur: Yes!', 
 "You're using coconuts!", 
 'King Arthur: What?', 
 "You've got ... coconut[s] and you're bangin' 'em together. "
]
"""

#%%

# splitlines으로 분할 후 슬라이스[::2]
"""
[
 'What? Ridden on a horse?', 
 "You're using coconuts!", 
 "You've got ... coconut[s] and you're bangin' 'em together."
]
"""

#%%
# ## 11-4 문자열 포매팅

# #### [Do It! 실습] f-문자열을 이용하여 포매팅하기

# In[26]:


s = f"hello"
print(s)


# In[27]:


num = 7
s = f"I only know {num} digits of pi."
print(s)


# In[28]:


const = "e"
value = 2.718
s = f"Some digits of {const}: {value}"
print(s)


# In[29]:


lat = "40.7815° N"
lon = "73.9733° W"
s = f"Hayden Planetarium Coordinates: {lat}, {lon}"
print(s)


# In[30]:


word = "scratch"
s = f"""Black Knight: 'Tis but a {word}.
King Arthur: A {word}? Your arm's off!
"""
print(s)


#%%

# #### [Do It! 실습] 숫자 포매팅하기

# In[31]:


p = 3.14159265359
print(f"Some digits of pi: {p}")


# In[32]:


digits = 67890
s = f"In 2005, Lu Chao of China recited {67890:,} digits of pi."
print(s)


# In[33]:

# 변수(prop)에 대해서    
# {prop:.4}  : 전체 숫자에서 의미있는 유효자리 4자리(0.0001031)
# {prop:.4%} : 백분율(퍼센트), 숫자에 100 곱해서 소수점 아래 4자리(0.0103%)
prop = 7 / 67890 # 0.00010310796877301516
s = f"I remember {prop:.4} or {prop:.4%} of what Lu Chao recited."
print(s)

# I remember 0.0001031 or 0.0103% of what Lu Chao recited.

# In[34]:

# 빈 칸을 0으로 채움
id = 42
print(f"My ID number is {id:05d}") # My ID number is 00042


# In[35]:

# 문자열에 0을 채움
id_zfill = "42".zfill(5)
print(f"My ID number is {id_zfill}") # My ID number is 00042


# In[36]:


print(f"My ID number is {'42'.zfill(5)}")


#%%

# 숫자 42를 전체 5자리에 출력을 하는데 빈 칸을 0으로 채워라.
# 문자열.zfill()을 이용하라.
val = 42
zln = 5
val_fill = str(val).zfill(zln)
print(val_fill) # 00042

#%%

# ## 11-5 정규식으로 문자열 처리에 날개 달기

# #### [Do It! 실습] 정규식으로 패턴 찾기

# In[37]:


import re

tele_num = '1234567890'


# In[38]:


m = re.match(pattern='\d\d\d\d\d\d\d\d\d\d', string=tele_num) 
print(type(m))


# In[39]:


print(m)


# In[40]:


print(bool(m))


# In[41]:


if m:
    print('match')
else:
    print('no match')


# In[42]:


print(m.start())
print(m.end())
print(m.span())
print(m.group())


# In[43]:


tele_num_spaces = '123 456 7890'


# In[44]:


m = re.match(pattern='\d{10}', string=tele_num_spaces)
print(m)


# In[45]:


if m:
    print('match')
else:
    print('no match')


# In[46]:


p = '\d{3}\s?\d{3}\s?\d{4}'
m = re.match(pattern=p, string=tele_num_spaces)
print(m)


# In[47]:


tele_num_space_paren_dash = '(123) 456-7890'
p = '\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=tele_num_space_paren_dash)
print(m)


# In[48]:


cnty_tele_num_space_paren_dash = '+1 (123) 456-7890'
p = '\+?1\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
print(m)


# #### [Do It! 실습] 알기 쉬운 정규식 만들기

# In[49]:


p = (
    '\+?'
    '1'
    '\s?'
    '\(?'
    '\d{3}'
    '\)?'
    '\s?'
    '\d{3}'
    '\s?'
    '-?'
    '\d{4}'
)
print(p)


# In[50]:


p = (
    '\+?'    # +가 0개 또는 1개
    '1'      # 숫자 1
    '\s?'    # 공백 문자가 0개 또는 1개
    '\(?'    # ( 문자가 0개 또는 1개
    '\d{3}'  # 숫자 3개
    '\)?'    # ) 문자가 0개 또는 1개
    '\s?'    # 공백 문자가 0개 또는 1개
    '\d{3}'  # 숫자 3개
    '\s?'    # 공백 문자가 0개 또는 1개
    '-?'     # - 문자가 0개 또는 1개
    '\d{4}'  # 숫자 4개
)
print(p)


# In[51]:


cnty_tele_num_space_paren_dash = '+1 (123) 456-7890'
m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
print(m)


# #### [Do It! 실습] 패턴과 일치하는 모든 문자열 찾기

# In[52]:


s = (
    "14 Ncuti Gatwa, "
    "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi, "
    "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
)
print(s)


# In[53]:


p = "\d+"
m = re.findall(pattern=p, string=s)
print(m)


# #### [Do It! 실습] 패턴과 일치하는 문자열 대체하기

# In[54]:


multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together.
"""

p = '\w+\s?\w+:\s?'
s = re.sub(pattern=p, string=multi_str, repl='')
print(s)


# In[55]:


guard = s.splitlines()[ ::2]
kinga = s.splitlines()[1::2]
print(guard)


# In[56]:


print(kinga)


# ### compile() 메서드

# In[57]:


p = re.compile('\d{10}')
s = '1234567890'
m = p.match(s)
print(m)


# In[58]:


p = re.compile('\d+')
s = (
    "14 Ncuti Gatwa, "
    "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi, "
    "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
)
m = p.findall(s)
print(m)


# In[59]:


p = re.compile('\w+\s?\w+:\s?')
s = "Guard: You're using coconuts!"
m = p.sub(string=s, repl='')
print(m)


# ## 11-6 regex 라이브러리

# In[60]:


import regex

p = regex.compile('\d+')
s = (
    "14 Ncuti Gatwa, "
    "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi, "
    "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
)
m = p.findall(s)
print(m)


# In[ ]:




