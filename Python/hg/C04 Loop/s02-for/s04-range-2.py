# 반복문(for)
# range(시작, 끝) 
#   - 시작부터 끝까지 연속적인 숫자를 생성

# 0부터 9까지 숫자를 생성
# 생성된 숫자만큼 반복 수행
for cnt in range(11): # 0,1,2,3, ... 9,10
    print(cnt)

#%%
from random import randint



for n in range(10,randint(10,15)):
    print(n)
    
#%%
counter = range(5)

print(counter)

for cnt in counter:
    print(cnt)
    