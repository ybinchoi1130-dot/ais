# -*- coding: utf-8 -*-

# 문자열 인덱싱
# 문자열은 연속된 문자들의 연속된 집합
#
# 참조: 특정한 위치의 문자를 본다(읽음)
# 시작위치 : 0부터 시작
# 참조방법 : 문자열[인덱스]
# 참조범위 : 0 ~ n-1, n=len(문자열)
# 제약사항 : 참조는 할 수 있지만 바꿀 수 없다. (read-only)

# 문자열 길이 함수: len()
#   문자열길이 = len(문자열)

#%%

# 문자열의 길이(length)
s ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sl = len(s)  # 문자열의 길이(length)를 리턴
print(sl, ':', s)
print('id:', id(s)) # id: 논리적인 가장의 메모리 주소
print(type(s))
print(type(sl))
#%%

# 문자열 인덱싱
# 참조 : 0부터 25(26-1)
print("첫번째 문자: ", s[0])    # 'A'
print("마지막 문자: ", s[sl-1]) # 'Z'

print(s[0], s[1], '...', s[24], s[25])
print(s[0], s[1], '...', s[sl-2], s[sl-1])


#%%

# 음수(minus)로 참조 가능
# 뒤에서부터 참조
# 맨 마지막 위치 : -1, len(문자열) - 1
slast1 = s[len(s) - 1]
slast2 = s[-1]
slast3 = s[len(s) - 2]

print(slast1) # Z
print(slast1) # Z
print(s[-2])  # Y

#%%

print(s[-1]) # Z
print(s[-2]) # Y
print(s[-3]) # X

print(s[0]) # A
print(s[ -len(s) ]) # A
print(s[ len(s) * -1 ]) # A

#%%
a="abcd"

print(a[len(a)*-1])

#%%

# 문자열의 요소를 개별적으로 바꿀 수 없다.
# 제약사항 : 참조는 할 수 있지만 바꿀 수 없다. (read-only)
# TypeError: 'str' object does not support item assignment
# s[0] = 'a'
s[sl-1] = 'z'

#%%

# 문자열 전체를 다른 문자열로 대체는 가능
# s1, s의 id 값은 같다. : 공유
s1 = s
print(' s:', id(s))
print('s1:', id(s1))

#%%

s1 += "."
print(' s:', id(s))
print('s1:', id(s1))

#%%

s += '.'
s1 += '.'
print(' s:', id(s))
print('s1:', id(s1))

#%%

s += ' '
s1 += ' '


print(' s:', id(s))
print('s1:', id(s1))

#%%

# 문자열 전체의 값을 변경은 가능
print(id(s))
s = "abcdefghijklmnopqrstuvw..."
print(id(s), s, len(s))
