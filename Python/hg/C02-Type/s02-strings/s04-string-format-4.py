# -*- coding: utf-8 -*-

# 문자열 포맷팅(String Formatting)
# 문자열 포맷 코드
"""
    %s : 문자열(string)
    %c : 문자(character)
    %d : 정수(10진수, decimal)
    %f : 실수(float)
    %o : 8진수(octal)
    %x : 16진수(hexa-decimal)
    %% : Literal %(문자 % 자체)
"""
#%%

# 정렬
# > : 오른쪽
# < : 왼쪽
# ^ : 가운데

n = 12345
s = "hello"
f = 0.12345

#%%

# 정수
print("#정수")
print(f"정수 : ({n})")      # 오른쪽
print(f"정수 : ({n:>10})")  # 오른쪽
print(f"정수 : ({n:<10})")  # 왼쪽
print(f"정수 : ({n:^10})")  # 가운데
print(f"정수 : ({n:>10d}) <- 10진수") # 오른쪽(10진수)
print(f"정수 : ({n:>10x}) <- 16진수") # 오른쪽(16진수)
print(f"정수 : ({n:>10o}) <- 8진수")  # 오른쪽(8진수)

#%%

print("#실수")
print(f"                 1         2")
print(f"        12345678901234567890")
print(f"실수 : ({f:>10})")
print(f"실수 : ({f:<10})")
print(f"실수 : ({f:<10.3})")  # 전체 10자리(소숫점 포함), 소숫점 이하 3자리
print(f"실수 : ({f:>10.3})")
print(f"실수 : ({f:>10.3f})")
print(f"실수 : ({f:^10.3})")

#%%

# 문자열
print("#문자열")
print(f"문자 : ({s:>10})")  # 오른쪽 정렬
print(f"문자 : ({s:<10})")  # 왼쪽 정렬
print(f"문자 : ({s:^10})")  # 가운데 정렬
print(f"문자 : ({s:^10s})") # 가운데 정렬

#%%

# 문자열.format() 함수
# format() 인자의 대입 순서 지정
print("정수 : ({0:^10})".format(n)) # 가운데 정렬
print("실수 : ({0:^10})".format(f)) # 가운데 정렬
print("문자 : ({0:^10})".format(s)) # 가운데 정렬
print("전체 : ({0:^10})({1:^10})({2:^10})".format(n, f, s)) # 가운데 정렬

#%%

# 인자의 순번을 생략
print("전체 : ({:^10})({:^10})({:^10})".format(n, f, s)) # 가운데 정렬
print("전체 : ({})({})({})".format(n, f, s)) 
print(f"전체 : ({n})({f})({s})") # 

#%%

# 가변처리(동적처리)
# 고객정보 처리
name = "홍길동"
age = 34

msg = "고객님의 이름은 ({0})이며 나이는 ({1})세 입니다.".format(name, age)
print(msg)

#%%

fmt = "고객님의 이름은 ({0})이며 나이는 ({1})세 입니다."
print(fmt.format(name, age))

#%%

print(fmt.format('전우치', 27))
print(fmt.format('임꺽정', 37))
print(fmt.format('장길산', 18))

#%%

# 고정(정적)
# fmt에 할당되는 문자열이 만들어 질 때 해당하는 변수의 값도 결정되어
# fmt 형식을 재활용 하여 동적으로 변수의 값을 재할당 할 수 없다.
name = '임꺽정'
age = 42
fmt = f"고객님의 이름은 ({name})이며 나이는 ({age})세 입니다."
print(fmt) # 고객님의 이름은 (임꺽정)이며 나이는 (42)세 입니다.

name = '전우치'
age = 55
print(fmt) # 고객님의 이름은 (임꺽정)이며 나이는 (42)세 입니다.




