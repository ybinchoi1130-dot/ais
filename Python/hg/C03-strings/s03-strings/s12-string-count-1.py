# 문자열 관련 함수
# 문자열.함수(...)

a = "hobby"
print(a.count('a')) # 0
print(a.count('b')) # 2

print("hello".count('l')) # 2

print(f'문자열 ({a})의 길이는? {len(a)}') # 5

# 정수
x = 12345
# AttributeError: 'int' object has no attribute 'count'
# x.count(3)

s = "abc,abc,hello,end"
f = 'abc'
scnt = s.count(f)
print(f"문자열 ('{s}').count('{f}')는 ({scnt})개이다.")
# 문자열 ('abc,abc,hello,end').count('abc')는 (2)개이다.