# 문자열(String)
# 변수 이름과 구별되며 리터럴(literal)
# 문자열은 데이터로서 문자들의 집합
# 큰 따옴표(")로 감싸서 문자열이라는 것을 알린다.
# 작은 따옴표(')로 감싸서 문자열이라는 것을 알린다.

# 빈 문자열 생성
hello = ""
world = ''
print(f'hello=[{hello}]') # hello=[]
print(f"world=[{world}]") # world=[]

hello="안녕"
world="세계"
print(f"{hello}, {world}!") # 안녕, 세계!

#%%

# 공백 문자열 : ASCII(32, 0x20)
space = ' '
print(f"공백 문자열=[{space}]")

#%% 
#r을 붙이지 않으면 '\n'이 이스케이프 문자로 인식해서 new 폴더가 작성되지 않는다.
#raw 포맷을 쓰면 이스케이프 문자를 무시한다.
rpath = r"D:\AI_yb\Github\ais\Python\hg\C02-Type\s01-operator\new"
print(rpath)

npath = "D:\AI_yb\Github\ais\Python\hg\C02-Type\s01-operator\new"
print(npath) # 안되는 예시 

epath = "D:\AI_yb\Github\ais\Python\hg\C02-Type\s01-operator\\new"
print(epath)