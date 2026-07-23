# 문자열 함수
# index()
# 처음 만나는 문자열의 위치 리턴
# 결과:
#   - 성공: 0이상의 값
#   - 실패: ValueError 예외 발생
#
# 형식
# 문자열.index(sub[, start[, end]])

s = "Python is the best choice"
print("0123456789" * 4)
print(s)

# 문자 한개 탐색
ipos = s.index('i') # 'i'가 있는 위치
print(f"'{s}'.index('i') : ", ipos)

# 문자 'k'가 있는 위치
# 예외가 발생하여 프로그램이 강제 종료 됨
# ValueError: substring not found
# kpos = s.index('k')  
# print(f"'{s}'.index('k') : ", kpos)

# 'i'가 있는 위치
# 시작 위치 지정
ipos = s.index('i', 0) 
print(f"'{s}'.index('i') : ", ipos)

# 'i'가 있는 위치
# 시작, 종료 위치 지정
ipos = s.index('i', 0, -1) 
print(f"'{s}'.index('i') : ", ipos)

ipos = s.index('i', 0, 8) 
print(f"'{s}'.index('i') : ", ipos)

ipos = s.index('i', 0, len(s)) 
print(f"'{s}'.index('i') : ", ipos)


#
print("프로그램을 정상적으로 처리했습니다.")