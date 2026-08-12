#!/usr/bin/env python
# coding: utf-8

# ## 11-1 문자열 다루기

# In[1]:


word = 'grail'
sent = 'a scratch'


# ### 인덱스로 문자열 추출하기

# #### [Do It! 실습] 문자 추출하기

# ##### 1. 문자 1개 추출하기

# In[2]:


print(word[0])


# In[3]:


print(sent[3])


# ##### 2. 문자 여러 개 추출하기

# In[4]:


print(word[0:3])


# #### [Do It! 실습] 음수 인덱스로 추출하기

# In[5]:


print(sent[-1])


# In[6]:


print(sent[-9:-8])


# In[7]:


print(sent[0:-8])


# In[8]:


print(sent[2:-1])


# In[9]:


print(sent[-7:-1])


# ### 슬라이싱 구문으로 마지막 문자 추출하기

# In[10]:


s_len = len(sent)
print(s_len)


# In[11]:


print(sent[2:s_len])


# #### [Do It! 실습] 슬라이딩 구문에서 왼쪽이나 오른쪽 인덱스를 지정하지 않고 문자 추출하기

# In[12]:


print(word[0:3])


# In[13]:


print(word[ :3])


# In[14]:


print(sent[2:len(sent)])


# In[15]:


print(sent[2: ])


# In[16]:


print(sent[ : ])


# #### [Do It! 실습] 슬라이싱 간격 설정하기

# In[17]:


print(sent[::2])


# In[18]:


print(sent[::3])


# ## 11-2 문자열 메서드

# In[19]:


print("black Knight".capitalize())
print("It's just a flesh wound!".count('u'))
print("Halt! Who goes there?".startswith('Halt'))
print("coconut".endswith('nut'))
print("It's just a flesh wound!".find('u'))
#print("It's just a flesh wound!".index('scratch'))  # 오류
print("old woman".isalpha())
print("37".isdecimal())
print("I'm 37".isalnum())
print("Black Knight".lower())
print("Black Knight".upper())
print("flesh wound!".replace('flesh wound', 'scratch'))
print("  I'm not dead.  ".strip())
print("NI! NI! NI! NI!".split(sep=' '))
print("3,4".partition(','))
print("nine".center(10))
print("9".zfill(5))


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

coords = ' '.join([d1, m1, s1, u1, d2, m2, s2, u2])
print(coords)


# In[21]:


coords.split(" ")
print(coords)


# #### [Do It! 실습] splitlines() 메서드

# In[22]:


multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together. 
""" 
print(multi_str)


# In[23]:


multi_str_split = multi_str.splitlines() 
print(multi_str_split)


# In[24]:


guard = multi_str_split[::2] 
print(guard)


# In[25]:


guard = multi_str.replace("Guard: ", "").splitlines()[::2] 
print(guard)


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


# #### [Do It! 실습] 숫자 포매팅하기

# In[31]:


p = 3.14159265359
print(f"Some digits of pi: {p}")


# In[32]:


digits = 67890
s = f"In 2005, Lu Chao of China recited {67890:,} digits of pi."
print(s)


# In[33]:


prop = 7 / 67890
s = f"I remember {prop:.4} or {prop:.4%} of what Lu Chao recited."
print(s)


# In[34]:


id = 42
print(f"My ID number is {id:05d}")


# In[35]:


id_zfill = "42".zfill(5)
print(f"My ID number is {id_zfill}")


# In[36]:


print(f"My ID number is {'42'.zfill(5)}")


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




