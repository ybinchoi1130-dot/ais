# 문자열이면서 포맷 형식을 가지고 있다.
fmt = "I eat {0} apples"

print(fmt) # I eat {0} apples

msg = fmt.format(10)
print(msg) # I eat 10 apples

print(fmt.format(11))
print(fmt.format(20))
print(fmt.format(30))

# 포맷을 변수에 넣어서 동적처리 불가
cnt = 10; print(f"I eat {cnt} apples")
cnt = 11; print(f"I eat {cnt} apples")
cnt = 20; print(f"I eat {cnt} apples")



