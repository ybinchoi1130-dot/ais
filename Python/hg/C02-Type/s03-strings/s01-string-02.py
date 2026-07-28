# -*- coding: utf-8 -*-

# 문자열(string): str()
# 멀티라인(다중라인)
# Enter: CRLF(Windows), CR(Mac), LF(Unix), \n
# LF(\n): 라인피드, 줄바꿈, 다음 줄로 이동    
# CR(\r): 캐리지 리턴, 커서를 맨 앞으로 이동
# FF(\f): 폼 피드, 다음 페이지

#%%

# 탈출문자(Escape Character)
# ord() : 문자에 해당하는 값을 리턴
cr = ord('\r') # Carriage Return
lf = ord('\n') # Line Feed
ff = ord('\f') # Form Feed
ht = ord('\t') # Horizontal Tab
bs = ord('\b') # Backspace
sp = ord(' ')  # Space
print('CR:', cr, hex(cr)) # 13(0x0d)
print('LF:', lf, hex(lf)) # 10(0x0a)
print('FF:', ff, hex(ff)) # 12(0x0c)
print('HT:', ht, hex(ht)) #  9(0x09)
print('BS:', bs, hex(bs)) #  8(0x08)
print('SP:', sp, hex(sp)) # 32(0x20)

#%%
goodmoring = "안녕하세요 \n좋은아침입니다."
print(goodmoring)
#%%
ssl = "안녕하세요?\n반갑습니다.\n환영합니다.\n"
print(ssl)

#%%

# 동일 라인에 덮어 쓰기가 됨
print("-----------------------------------------")
ss1 = "안녕하세요?\r반갑습니다.\r환영\r"
print(ss1) # 환영습니다.

#%%

print("-----------------------------------------")
ss2 = "안녕하세요?\n\r반갑습니다.\n\r환영합니다.\n\r"
print(ss2)

#%%

# Windows: CRLF(\r\n)
print("-----------------------------------------")
ss3 = "안녕하세요?\r\n반갑습니다.\r\n환영합니다.\r\n"
print(ss3)

#%%

# Horizontal Tab(수평탭)
# 8칸
print("1234567890" * 5)
print("ABC\tDEFGHIJK\tLMNOPQ\tEND")

#%%

# 탭 스페이스 4칸인 경우
"""
12345678901234567890123456789012345678901234567890
ABC	DEFGHIJK	LMNOPQ	END
"""

#%%
# 탭 스페이스 8칸인 경우
# (Windows CMD)
"""
12345678901234567890123456789012345678901234567890
ABC     DEFGHIJK        LMNOPQ  END
"""
#%%

# BS(Backspace)
print("Backspace:", "ABC\b\b\bD") # DBC



