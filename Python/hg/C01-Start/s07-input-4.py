# input() 명령어
# 키보드로부터 내용을 입력
# 변수 = input('안내문자')

age = input('나이값을 입력하세요: ')

print("당신의 현재 나이는", age, "세입니다.")

# age10= int(age) +10

#int(문자열) : 문자열을 정수(int)로 변환 한다.
agenm =int(age)
age10 =agenm + 10
print("당신의 10년 후의 나이는", age10,"세입니다.")
print('age 자료형은:', type(age))
print('age10 자료형은:', type(age10))
    # str : 문자열, string의 약자