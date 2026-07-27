# 반복문(for)
# for ... else

# for ... else를 쓰지 않고 처리하려면?

contents = []
# contents = ['article', 'magazine']
existed = False

for content in contents:
    existed = True
    print('content:', content)

if not existed:
    print('컨텐츠가 없습니다')
else:    
    print('컨텐츠가 있습니다')
