# print(인자, end='...')
# default(기본값)은 다음 라인으로 이동)
# Line Feed : 라인을 다음 라인으로 이동(Enter)
# ------------------------------------------------
# CRLF : Windows
# LF : Linux, MacOS

print("안녕하세요?")
print("반갑습니다.")

#%%
# 다음 라인으로 이동하지 않고 연속해서 출력
print("안녕하세요?", end=' ') 
print("반갑습니다.", end=' ')
print("환영합니다.")

# 결과: 안녕하세요? 반갑습니다. 환영합니다.

#%%
t1 = '010'
t2 = '1234'
t3 = '4567'
print(t1, end='-')
print(t2, end='-')
print(t3)


#%%
#문자열 더하기
s1 = "안녕"
s2 = '하세요'
 
print(s1,s2)
print("s1,s2")

s3= s1 + s2
print(s3)

#%%
#문자열 곱하기

h1 = '*' * 20
h2 = '-' * 20
print('123456789' * 2)
print(h1)
print(h2)
print('='*30)
h3 = "$" * 10
print(h3)

#%%
#따음표의 혼용
sx = "철수는 영수에게 '어디에 가니?'라고 물었다." 
print(sx)
print("sx") #sx 문자열 출력

print('철수는 영우에게"어디에가니?"')
print("철수는 영수에게 \"어디에 가니?\"라고 물었다.")
print("I don't want to go school..")
print('I don\'t want to go school..')
