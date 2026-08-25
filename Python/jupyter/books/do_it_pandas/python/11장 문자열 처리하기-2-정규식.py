# ## 11-5 정규식으로 문자열 처리에 날개 달기

# #### [Do It! 실습] 정규식으로 패턴 찾기

# In[37]:


import re

tele_num = '1234567890'  # <class 're.Match'>
tele_num = 'A1234567890' # <class 'NoneType'>
tele_num = '1234567890A' # <class 're.Match'>

# In[38]:

# 문자열의 가장 처음(시작) 부분부터 지정한 패턴과 일치하는지 검사
# 패턴(\d): 숫자 1개를 의미한다.
# 숫자 10개
# 결과
#   - 매치가 된 패턴이 없으면: <class 'NoneType'>  
#   - <class 're.Match'> 매치 객체
m = re.match(pattern='\d\d\d\d\d\d\d\d\d\d', string=tele_num) 
print(type(m))

# In[39]:

print(m) # <re.Match object; span=(0, 10), match='1234567890'>

# In[40]:

print(bool(m)) # True

# In[41]:


if m:
    print('match')    # 매치 되는 패턴이 존재
else:
    print('no match') # 매치 되는 패턴이 존재하지 않음


# In[42]:

if m:
    print(m.start()) # 0
    print(m.end())   # 10
    print(m.span())  # (0,10)
    print(m.group()) # 1234567890
else:
    print("매치 되는 패턴이 존재하지 않음")

# In[43]:

tele_num_spaces = '123 456 7890'

# In[44]:

# 문자열의 가장 처음(시작) 부분부터 지정한 패턴과 일치하는지 검사
# 연속한 숫자가 10개이면
# 결과: None, 문자열 중간에 공백이 있기 때문에
m = re.match(pattern='\d{10}', string=tele_num_spaces)
print(m) # None


# In[45]:


if m:
    print('match')
else:
    print('no match')


# In[46]:

# \d{3} : 숫자(3자리)
# \s?   : 공백. 
# \d{3} : 숫자(3자리)
# \d{4} : 숫자(3자리)
# 물음표(?): 옵션(선택사항), 있어도 되고 없어도 된다. 0번 또는 1번
p = '\d{3}\s?\d{3}\s?\d{4}'
m = re.match(pattern=p, string=tele_num_spaces)
print(m)

# <re.Match object; span=(0, 12), match='123 456 7890'>

#%%

p = '\d{3}\s?\d{3}\s?\d{4}'
m = re.match(pattern=p, string="0101234567")
print(m) # <re.Match object; span=(0, 10), match='0101234567'>

#%%

p = '\d{3}\s?\d{3}\s?\d{4}'
m = re.match(pattern=p, string="010 1234567")
print(m) # <re.Match object; span=(0, 11), match='010 1234567'>

#%%

p = '\d{3}\s?\d{3}\s?\d{4}'
m = re.match(pattern=p, string="010123 4567")
print(m) # <re.Match object; span=(0, 11), match='010123 4567'>

#%%

# In[47]:

tele_num_space_paren_dash = '(123) 456-7890'
p = '\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=tele_num_space_paren_dash)
print(m) # <re.Match object; span=(0, 14), match='(123) 456-7890'>

#%%
    
# 괄호, 공백, 하이픈(-)은 필수적으로 포함
tele_num_space_paren_dash = '(081) 1234-5678'
p = '\(\d{3}\)\s?\d{4}-\d{4}'
m = re.match(pattern=p, string=tele_num_space_paren_dash)
print(m) # <re.Match object; span=(0, 15), match='(081) 1234-5678'>

#%%

# 괄호, 하이픈(-)은 필수적으로 포함
# 나라번호 뒤의 공백은 옵션: \s?
tele_num_space_paren_dash = '(081)1234-5678'
p = '\(\d{3}\)\s?\d{4}-\d{4}'
m = re.match(pattern=p, string=tele_num_space_paren_dash)
print(m) # <re.Match object; span=(0, 15), match='(081) 1234-5678'>


# In[48]:

# 국가코드 : +1 또는 1
cnty_tele_num_space_paren_dash = '+1 (123) 456-7890'
p = '\+?1\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
print(m) # <re.Match object; span=(0, 17), match='+1 (123) 456-7890'>

#%%

# 국가코드 : +1 또는 1
cnty_tele_num_space_paren_dash = '1 (123) 456-7890'
p = '\+?1\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
print(m) # <re.Match object; span=(0, 16), match='1 (123) 456-7890'>

#%%

# 국가코드('1')가 없으면 못참음
cnty_tele_num_space_paren_dash = '(123) 456-7890'
p = '\+?1\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
print(m) # <None>

#%%

# 국가코드를 가변적으로 하려면?
# \d{1,3}: 최소 1자리, 최대 3자리 숫자
cnty_tele_num_space_paren_dash = '+82 (123) 456-7890'
p = '\+?\d{1,3}\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
print(m) # <re.Match object; span=(0, 18), match='+82 (123) 456-7890'>

#%%

# 국가코드를 가변적으로 하려면?
# \d{1,3}: 최소 1자리, 최대 3자리 숫자
cnty_tele_num_space_paren_dash = '+1 (123) 456-7890'
p = '\+?\d{1,3}\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
print(m) # <re.Match object; span=(0, 17), match='+1 (123) 456-7890'>


#%%
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


#%%

# #### [Do It! 실습] 패턴과 일치하는 모든 문자열 찾기

# In[52]:


s = (
    "14 Ncuti Gatwa, "
    "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi, "
    "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
)
print(s)


# In[53]:

# "\d+": 숫자가 1개 이상인 패턴
# findall: 지정판 패턴을 찾아 리스트로 반환
p = "\d+"
m = re.findall(pattern=p, string=s)
print(m)


#%%

# #### [Do It! 실습] 패턴과 일치하는 문자열 대체하기

# In[54]:

multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together.
"""

# \w: 알파벳 또는 숫자, 밑줄 1개를 의미한다.
# sub(pattern=패턴, string=대상문자열, repl=교체문자열)
# 패턴과 일치하는 것을 찾아서 지움(repl='')
p = '\w+\s?\w+:\s?'
s = re.sub(pattern=p, string=multi_str, repl='')
print(s)

#%%

"""
What? Ridden on a horse?
Yes!
You're using coconuts!
What?
You've got ... coconut[s] and you're bangin' 'em together.
"""

#%%   

guard = s.splitlines()[ ::2]
kinga = s.splitlines()[1::2]
print(guard)
print(kinga)


#%%
# ### compile() 메서드

# In[57]:

# compile()
#  - 패턴을 반복해서 사용해야 하는 경우 효율을 높일 수가 있다.
#  - 한 번 만는 패턴을 재활용
p = re.compile('\d{10}')
s = '1234567890'
m = p.match(s)
print(m)


# In[58]:


# 숫자가 1개 이상인 패턴
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



#%%

# ## 11-6 regex 라이브러리
# pip install regex

# In[60]:


import regex

p = regex.compile('\d+')
s = (
    "14 Ncuti Gatwa, "
    "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi, "
    "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
)
m = p.findall(s)
print(m) # ['14', '13', '12', '11', '10', '9']


# In[ ]:




