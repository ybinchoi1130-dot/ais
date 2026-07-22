# -*- coding: utf-8 -*-

# 문자열 포맷팅(String Formatting)
# 문자열 포맷 코드
"""
    %s : 문자열(string)
    %c : 문자(character)
    %d : 정수(10진수, decimal)
    %f : 실수(float)
    %o : 8진수(octal)
    %x : 16진수(hexa-decimal)
    %% : Literal %(문자 % 자체)
"""
# 형식: 
# 포맷문자열 % 변수
# 포맷문자열 % (변수, ...)

# 문자(character) : 단일 문자
# 'a', 'A', '한', "#", "X"

#%%

# 문자열을 포맷(%c)에 전달하면?
abc = "abc"

# TypeError: %c requires int or char
# print("문자열 (%s)를 포맷코드(%c)에 전달하면 오류 발생" % (abc, abc))


#%%

a = 'a'
print("문자포맷 : (%c)" % a) # 문자포맷 : (a)

av = ord(a) # 문자에 해당하는 ASCII 코드 값
print("문자 (%c)의 ASCII 값은 (%d)이다." % (a, av)) # 97

print("ord('%c')의 값에 해당하는 문자는 ('%c')이다." % (a, av))  # a(97)

#%%

# 한글

hangeul = '한'
hancode = ord(hangeul)
hanhexa = hex(hancode) 
print(type(hanhexa), hanhexa) # <class 'str'> 0xd55c

print("문자 ('%c')의 코드 값은 (%d)(0x%x)(%s)이다." % (hangeul, hancode, hancode, hex(hancode)))
# 문자 ('한')의 코드 값은 (54620)(0xd55c)이다.

# hex() 함수와 동일한 기능
hexastr = "0x%x" % hancode
print(hexastr) # 0xd55c


