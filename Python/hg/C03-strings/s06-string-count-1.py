# -*- coding: utf-8 -*-

# 문자열 함수

# 문자 개수 세기 : count()
s = "Hello World."
l = 'l'
c = s.count(l)
print(f"문자열('{s}')에 문자('{l}')는 ({c})개 있다.")
print(f"문자열(\"{s}\")에 문자('{l}')는 ({c})개 있다.")
print(f'문자열("{s}")에 문자("{l}")는 ({c})개 있다.')
print(f'문자열("{s}")에 문자(\'{l}\')는 ({c})개 있다.')

#%%

# 없는 함수(메서드)를 호출하면?
# AttributeError: 'str' object has no attribute 'countx'
# s.countx('0')

"".capitalize()




#%%

# 전화번호에 하이픈(-)이 몇개 포함되어 있는가?
tel = "010-1234-5678"
telcnt = tel.count('-')
print(f"'{tel}'.count('-') : {telcnt}개")

#%%

# 문자열을 변수에 담지 않고 직접 함수를 지정하여 처리
spcnt = "Welcome to korea".count(' ')
print("공백 갯수: ", spcnt) # 2

#%%

cnt = "Welcome to korea".count('.')
print("마침표 갯수: ", cnt) # 0

#%%

# 문자열에서 해당하는 문자열의 갯수
cnt = "Welcome to korea".count('korea')
print("마침표 갯수: ", cnt) # 1

#%%

# 문자열에서 빈문자열의 갯수는?
wct = "Welcome to korea"
cnt = wct.count('')
print("문자열의 길이: ", len(wct)) # 16
print("빈문자열의 갯수: ", cnt)    # 17 = len(str) + 1
#\w\e\l\c\o\m\e\ \t\o\ \k\o\r\e\a\
spnt = "_w_e_l_c_o_m_e_ _t_o_ _k_o_r_e_a_".count('_')
print("/ 갯수",spnt)






