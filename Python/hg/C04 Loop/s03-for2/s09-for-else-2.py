# 반복문(for)
# for ... else

#contents = []
contents = ['article', 'magazine']

for content in contents:
    print('content:', content)
    break # 반복을 끊어내기
#for 반복문 실행종료 후 else 문 실행
else:
    print('컨텐츠가 없습니다')

#%%
contents = [1,3,5,7]
odd=0
for content in contents:
    if content % 2 == 0:
       break   
    print('content:', content)
else:
    print('컨텐츠가 없습니다')