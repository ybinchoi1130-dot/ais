# 문자열(string)

# 큰 따옴표, 작은 따옴표 혼용

msg = "Python's favorite food is perl"
print(msg) # Python's favorite food is perl 

# 역스래시를 사용해서 문자 자체로 처리
msg = 'Python\'s favorite food is perl'
print(msg)

# 줄바꾸기(Line Feed) : \n
ssl = "안녕하세요?\n반갑습니다.\n환영합니다.\n"
print('-' * 30)
print(ssl, end='')
print('-' * 30)

# 수평탭(Hirizontal Tab) : \t
# 기본 : 8칸 
print("1234567890" * 5)
print("ABC\tDEFGHIJK\tLMNOPQ\tEND")
"""
12345678901234567890123456789012345678901234567890
ABC     DEFGHIJK        LMNOPQ  END
"""
# 백스페이스(Backspace) : \b
print("백스페이스:", "ABC\b\b\bD") # DBC