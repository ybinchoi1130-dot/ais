# print()
# print(파라미터, ...)
# print(parameter, ...)
# 호출: print(argument, ...)
# 각각의 파라미터를 공백(스페이스) 띄어서 출력
# 콤마(,)에 분리되는 내용을 한 칸씩 띄어서 출력
#%%

print("시작")
print()
print("종료")

#%%
# 실행결과
"""
시작

종료
"""


#%%
x = 10
y = 20
print(x) #인자 1개
print(y) #인자 1개
print(x,y) #인자 2개
print('x와 y의 값은?',x,y) #인자 3개

#%%
 
xy = 'x와  y의 값은?'
print(xy, x, y) #인자 3개

#%%
# 구분자를 지정할 수 있다.
print(x, y, sep=',')
print(x, y, sep=', ')
print(x, y, sep='/')

#%%

tel1 = "010"
tel2 = "1234"
tel3 = "4567"
print(tel1, tel2, tel3, sep='.')
print(tel1, tel2, tel3, sep='-')

