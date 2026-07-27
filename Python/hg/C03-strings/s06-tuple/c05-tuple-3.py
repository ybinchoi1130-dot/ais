# 튜플(Tuple)

jobs = ('요리사', '교사', '사무원')
print(hex(id(jobs)), jobs)

jobs += ('기자', '앵커')

# 전체를 통으로 새로운 값을 할당은 가능
# id가 변경되며 새로운 메모리에 할당
print(hex(id(jobs)), jobs) # ('요리사', '교사', '사무원', '기자', '앵커')
