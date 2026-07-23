# -*- coding: utf-8 -*-

# 문자열 함수

# 문자열의 위치 : find()
# 처음 만나는 문자열의 위치
# 결과
#   성공 : 0부터
#   실패 : -1(찾지 못하면)

s = "Python is the best choice, version 3.18"
print("0123456789" * 4)
print(s)

#%%

print(s.find('3')) # 35
print(s.find('s'))
print(s.find('k'))
#%%

# 문자 한개 탐색
ipos = s.find('i')
kpos = s.find('k')

print(f"'{s}'.find('i') : ", ipos) # 7, is ...
print(f"'{s}'.find('k') : ", kpos) # -1

#%%

# 문자열 탐색
print(f"'{s}'.find('is') : ", s.find('is'))   # 7
print(f"'{s}'.find('the') : ", s.find('the')) # 10

#%%

# [문제]
# 문자열을 연속해서 찾기.
# 문자열 변수(s)에서 지정된 문자열('t')의 위치를 모두 찾아라.
# 단. find() 함수를 이용하라.
# 정답: 2 10 17

s = "Python is the best choice"
#%%

s = "Python is the best choice"

# 1. 찾을 문자('t')와 검색을 시작할 위치(idx) 초기화
idx = s.find('t')

# 2. find()가 문자를 찾지 못해 -1을 반환할 때까지 반복
while idx != -1: #!=서로 같지가 않다.
    # 찾은 위치 출력 (공백으로 띄워서 출력)
    print(idx, end=' ')
    
    # 현재 찾은 위치 바로 다음 칸(idx + 1)부터 다시 't'를 검색
    idx = s.find('t', idx + 1)


#%%

print("0123456789" * 4)
print(s)

# 찾을 문자열
findstr = 't'
print(f"문자열 ('{s}')에서 문자열('{findstr}')의 갯수는?", s.count(findstr))

#%%

# [해결1] 슬라이싱
t1 = s.find(findstr)
t2 = s[t1+1:].find(findstr) + t1 + 1
t3 = s[t2+1:].find(findstr) + t2 + 1
print(t1,t2,t3) # 2 10 17



#%%
#스스로 예제 만들어보기
car = "357어1328"
print(type(car))
print(car)
findd = '3'
print(f"차량번호 ({car})에서 문자열 ('{findd}')의 갯수는 :",car.count(findd))
t1 = car.find(findd)
t2 = car[t1+1:].find(findd) + t1+1
print(f"차량번호 {findd}의위치는 : {t1+1},{t2+1}입니다.")


#%%

# 분할: 검증
t1 = s.find(findstr)
s1 = s[t1+1:]  # 슬라이싱
t2 = s1.find(findstr) + t1 + 1 # 이전위치
s2 = s[t2+1:]  # 슬라이싱 
t3 = s2.find(findstr) + t2 + 1 # 이전위치
print(t1,t2,t3) # 2 10 17

#%%

# [해결2] find() 함수의 시작위치
# str.find(sub[, start[, end]])
# 결과 = 문자열.find(탐색문자열, 시작위치[, 종료위치])

t1 = s.find(findstr)
t2 = s.find(findstr, t1 + 1) # 다음위치
t3 = s.find(findstr, t2 + 1) # 다음위치
print(t1,t2,t3) # 2 10 17


#%%

# [문제2]
# 전화번호(010-1234-5678)에서 하이픈(-)을 기준으로 번호를 추출하라.
# 단: 문자열.find() 메서드를 이용하라.

tel = "010-1234-5678"
tfs = '-'

# 첫 번째 번호
s1 = tel.find(tfs)
t1 = tel[:s1]

# 두 번째 번호
s2 = tel.find(tfs, s1+1)
t2 = tel[s1+1:s2]

# 세 번째 번호
s3 = tel.find(tfs, s2+1)
# t3 = tel[s2+1:s3] # -1은 맨 마지막 요소('8')를 제외
t3 = tel[s2+1:]

print("위치:", s1, s2, s3) # 3, 8, -1
print("번호:", t1, t2, t3) # 010 1234 5678

#%%

tel = "010-2499-8895"

tfs = tel.find('-')

while tfs != -1:             
    print(tfs,end=' ')
    restart = tfs+1
    tfs = tel.find('-', restart)
tel.append(tel[restart:])
print("위치추출:",tfs)
print("추출된 번호 리스트:", tel)
print(f"식별번호: {tel[0]}")
print(f"국번(중간): {tel[1]}")
print(f"개인번호(끝): {tel[2]}")

#while tfs != -1:"하이픈이 몇 개인지 난 몰라! 문장이 아무리 길어도 전부 다 찾아낼 때까지 계속 뺑뺑이 돌려!"
    #➡️ 하이픈이 5개든 10개든 다 찾아냄.
#if tfs != -1:"하이픈이 있는지 없는지 딱 한 번만 검사해 보고 있으면 출력하고 그냥 끝내!" 
    #➡️ 개수가 정해져 있을 때 안전하게 쓰기 좋음.
#%%
tel = "010-2499-8895"

# [수정] 조각난 번호들을 차곡차곡 담아줄 진짜 '리스트 바구니'를 만듭니다.
phone_parts = []

# 자르기 시작할 위치(start)와 첫 번째 하이픈 위치 찾기
start = 0
tfs = tel.find('-')

print("하이픈 위치 확인:", end=' ')
while tfs != -1:             
    print(tfs, end=' ')
    
    # 1. 시작 위치부터 하이픈 직전까지 잘라서 리스트 바구니에 넣기
    phone_parts.append(tel[start:tfs])
    
    # 2. 다음 자르기 시작 위치를 하이픈 다음 칸으로 갱신
    restart = tfs + 1
    start = restart
    
    # 3. 다음 하이픈 찾기
    tfs = tel.find('-', restart)

# [수정] 문자열 tel이 아니라, 리스트 바구니(phone_parts)에 마지막 남은 조각을 담습니다.
phone_parts.append(tel[restart:])

print("\n--------------------------------")
print("위치추출 종료 후 tfs 값은:", tfs)  # 더 이상 없으므로 -1이 나옵니다.
print("추출된 번호 리스트:", phone_parts)
print(f"식별번호: {phone_parts[0]}")
print(f"국번(중간): {phone_parts[1]}")
print(f"개인번호(끝): {phone_parts[2]}")

