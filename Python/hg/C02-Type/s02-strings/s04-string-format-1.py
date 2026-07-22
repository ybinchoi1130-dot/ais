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

#%%

# 정수: %d
num = 99
print("이 숫자는 정수 %d 입니다." % num)        # 포맷 코드
print("이 숫자는 정수 {0} 입니다.".format(num)) # 문자열 함수: 문자열.format()
print(f"이 숫자는 정수 {num} 입니다.")          # f 포맷

#%%

# 문자열
# 포맷코드가 다중인 경우는 괄호에 포맷에 대응하는 변수를 나열해서 지정한다.
# name : %s
# age : %d, %s, %f

name = '홍길동'
age = 34

# namedms 문자열이고 출력 포맷은 decimal(#%d)이기 때문에 오류 발생
# TypeError: %d format: a real number is required, not str
# userfmt = "이름이 (%d)인 사람의 나이는 (%d)세 입니다." % (name, age)

#%%

# 숫자 자료형(age)는 문자포맷(%s) 포맷 가능
userfmt = "이름이 (%s)인 사람의 나이는 (%s)세 입니다." % (name, age)
print(userfmt)
# 이름이 (홍길동)인 사람의 나이는 (34)세 입니다.

#%%
# 숫자 자료형(age)는 실수포맷(%f) 포맷 가능
userfmt = "이름이 (%s)인 사람의 나이는 (%f)세 입니다." % (name, age)
print(userfmt) # 이름이 (홍길동)인 사람의 나이는 (34.000000)세 입니다.

#%%

userfmt = "이름이 (%s)인 사람의 나이는 (%d)세 입니다." % (name, age)
print(userfmt) # 이름이 (홍길동)인 사람의 나이는 (34)세 입니다.

#%%

# %를 문자 드대로 출력하기 위해서는?
# '%%'와 같이 연속해서 기술한다.

sv = 50

# TypeError: not enough arguments for format string
# 문자열 포맷에 %가 나오면 이어서 해당하는 포맷코드를 기대
print("오늘 눈이 올 확률은 (%d)%% 입니다." % sv)

#%%

print("오늘 눈이 올 확률은 (%d)%% 입니다." % sv)

