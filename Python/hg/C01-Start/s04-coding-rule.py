# 코딩 규칙
# 변수(variable) : 메모리 영역(주소)의 별칭
# 메모리 주소는 2진수로 되어 있으며 8비트(1바이트) 단위로 구성
# 변수 a를 선언하게 되면 메모리의 영역을 할당한다.
#%%

tt=1234
print(type(tt)) # <class 'int'>
print(tt) # 1234

#%%

# 따옴표(', ")로 감싸면 문자열이다.
tt='1234'
print(type(tt)) # <class 'str'>: string(문자열)

print(tt) # 1234


#%%
x = 10      # x <- 10, x에 값 10을 넣어라
y = 20      # y <- 20, y에 값 20을 넣어라
print(x)
print(y)

#%%

# 변수이름으로 다국어(한글)를 사용 할 수 있다.
# ※ 권장하지 않는다.
홍길동 = 100000
전우치 = '나의 이름은 전우치'
양귀비 = '나는 양귀비입니다.'  
양귀비 = 전우치  # 원래의 값은 사라진다. 전우치의 내용은 유지된다.

print(홍길동) # 100000
print(전우치) # 나의 이름은 전우치
print(양귀비) # 나의 이름은 전우치

#%%

# 변수를 선언하는 명명규칙(이름을 만드는 규칙)
# 소문자(a~z)
# 대문자(A~Z)
# 숫자(0~9)
# 특수문자: 언더스코어(_), Shift + - (마이너스) 
# 제약조건(예외사항)
#   -> 숫자로 시작할 수 없다.
#   -> 영문자나 언더스코어로 시작해야 한다.
#   -> 예약어(reserved word, key-word)를 사용할 수 없다.

#%%

# 변수명은 숫자로 시작할 수 없다.
# SyntaxError: invalid decimal literal
# 1abc = 1234
# print(1abc)

#%%

# 특수문자는 언더스코어(_)만 가능하다.
# 언더스코어(_)를 맨 앞에 쓰는 것은 특수한 용도로 사용되며
# 가능한 사용하지 않는 것을 추천
_abc = 'abc'
print(_abc)

abc_12 = "abc_1234"
print(abc_12)

abc_ = "abc_"
print(abc_)

#%%

# 언더스코어(_)를 제외한 특수문자는 사용할 수 없다.
# SyntaxError: invalid syntax
# $abc = 'abc'
# abc$ = 'abc'
# abc_$ = 'abc'

# 공백도 특수문자이며 변수명으로 사용할 수 없다.
# abc fg = 'abc'

#%%

# 키워드는 변수로 사용할 수 없다.
# Keyword(Reserved Word) : 35개
# 파이썬 버전: 3.13.14
"""
['False',    'None',    'True',  'and',   'as', 
 'assert',   'async',   'await', 'break', 'class', 
 'continue', 'def',     'del',   'elif',  'else', 
 'except',   'finally', 'for',   'from',  'global', 
 'if',       'import',  'in',    'is',    'lambda', 
 'nonlocal', 'not',     'or',    'pass',  'raise', 
 'return',   'try',     'while', 'with',  'yield']
"""

#%%

# 키워드
# SyntaxError: invalid syntax
# global = "글로벌"

# 다른 문자와 결합하면 가능
global1 = "글로벌"
print(global1) # 글로벌

#%%

# 대소문자는 구별
# 대.소문자는 다른 변수로 취급한다.
xy = 10 # 소문자
XY = 20 # 대문자
xY = 30 # 소문자, 대문자
Xy = 40 # 대문자, 소문자

print('xy=', xy) # xy= 10
print('XY=', XY) # XY= 20
print('xY=', xY) # xY= 30
print('Xy=', Xy) # Xy= 40
print(xy, XY, xY, Xy) # 10 20 30 40


#%%
# 변수 y의 값이 x 값으로 먼저 변경되어
# 변수 x,y의 값이 같아 진다.

"""
y=x
x=y
print('x=', x)
print('y=', y)

"""

#%%
#전통적인 방식의 데이터 교환
print('x와 y값의 교환')
z=y  # y값을 z에 임시 보관(대피)
y=x
x=z

print('x=',x)
print('y=',y)


#%%

y=20
x=10

print('x=', x)
print('y=', y)

print('x와 y값의 교환')
x, y = y, x
print('x=',x)
print('y=',y)

#%%
Msg = "소식"; _Hello = "Hi!"; Hello = "Hi!"; A123 = "A123";
print(Msg, _Hello, Hello, A123)

#%%

# SyntaxError: invalid syntax
# $Dal = 10

# SyntaxError: invalid syntax
# 9abc = 99

# SyntaxError: can't assign to keyword
# False = "False"


#%%
# 변수를 선언하고 값을 지정하지 않으면?

# NameError: name 'Welcome' is not defined
# 변수를 선언할 때 반드시 초기값을 지정해야 한다.
# 변수에 초깃값을 지정하여 변수의 자료형이 결정된다.
# Welcome

# 빈 문자열
Welcome = ""
print(Welcome)

#%%

# 숫자 zero
# zero
zero = 0
print(zero)

#%%

# NameError: name 'null' is not defined
# Unknown = null

# NameError: name 'Null' is not defined
# Unknown = Null

# 자료형을 결정하지 않고 무의미한 값을 지정할 수 있다.
Unknown = None
print(type(Unknown), Unknown) # <class 'NoneType'> None

#%%
# 자료형
# 정수(int), 실수(float), 문자열(str), 논리형(bool), 객체(object)

#%%

# 들여쓰기(indent)
# 원래 Tab은 기본적으로 8칸이다.
# 코드 블럭은 일반적으로 Tab(4칸) 단위로 들여쓰기를 한다.
# 같은 블럭에서 들여쓰기 간격이 같아야 한다.
# 탭(Tab), 스페이스(Space)를 혼용해서는 않는다.
# (혼용해도 오류가 나지는 않는다)

"""
01234567890
대분류
    중분류
        소분류1
        소분류2

"""        

#%%

# 세미콜론(;)
# 문장의 끝에 붙인다.
# 일반적으로 생략한다.
# 여러 명령문을 하나의 라인에 기술할 때 세미콜론을 붙여서 쓸 수 있다.
# 명시적으로 문장의 끝을 세미콜론으로 표시할 수 있다.
print('hello, python, ');   

# 자동으로 붙여서 처리를 해 준다.
print('welcome to korea!')  

#%%

# 들여쓰기를 하지 않고 줄바꿈을 해도 된다.
hp = 1234
print
(hp)

# 1234

#%%
# 하나의 라인으로 연속해서 기술할 수 있다.
# 반드시 문장을 구분하기 위해서 세미콜론을 붙여야 한다.
print('hello, python, '); print('welcome to korea!')

#%%

print()

#%%
print('hello, python, ', end=''); print('welcome to korea!')

#%%
print('hello, python, welcome to korea!')

#%%

a = 10
b = 20
c = a + b
print('a=', a, ', b=', b, ', c=', c, sep='') # a=10, b=20, c=30
print("a={0}, b={1}, c={2}".format(a, b, c)) # a=10, b=20, c=30

#%%

# 콜론(:), 세미콜론(;)
x=10; y=20; z=x+y
print("z={2}, y={1}, x={0}".format(x, y, z)) # z=30, y=20, x=10
print("x=%d, y=%d, z=%d" % (x, y, z))        # x=10, y=20, z=30









