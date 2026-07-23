# 문자열 인덱스
# 문자열의 위치를 참조

# 문자열은 연속된 문자의 집합
# 시작위치: 0
# 참조방법: 문자열[인덱스]
# 참조범위: 0부터 문자열 길이에서 -1까지. len(문자열) - 1
# 제약사항: 문자열은 참조는 할 수 있지만 바꿀 수는 없다.(읽기 전용)

s = "abcdefghijklmnopqrstuvwxyz"
l = len(s)

# 객체의 고유 주소값(리퍼런스)을 리턴
print('id:', hex(id(s)))  # 실행할 때마다 값이 변경 됨

print('길이:', l)       # 26
print('s[0] :', s[0])   # a
print('s[10] :', s[10]) # k
print('s[25] :', s[25]) # z

a = s[0] # 참조
print('s[0] :', a)   # a

# 인덱싱을 통해서 개별 요소를 바꿀 수 없다.
# TypeError: 'str' object does not support item assignment
# read-only
# s[0] = 'A' 

# 전체 문자열은 바꿀 수 있다.
s = "ABCDEFG"
print('id:', hex(id(s)))  # 바뀜: 새로운 주소값이 지정 됨
print('전체 문자열 변경: len=', len(s), ':', s)

# 문자열의 마지막 요소
print("# 문자열의 마지막 요소")
print(s[-1]) # 'G'
print(s[len(s)-1]) # 'G'

# 마이너스로 첫 번째 요소를 참조
print("# 문자열의 첫 번째 요소")
print(s[len(s) * -1]) # 'A'
print(s[-len(s)]) # 'A'

#
x = 10
y = -x
z = -y
print("x,y,z:", x, y, z, sep=', ') # 10, -10, 10

y = x * -1
z = y * -1
print("x,y,z:", x, y, z, sep=', ') # 10, -10, 10
