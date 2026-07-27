# 리스트에서 모든 요소를 제거
# 리스트.clear()

l1 = ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']
l2 = ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']
l3 = ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']

print('l1:', hex(id(l1)), l1)
print('l2:', hex(id(l2)), l2)
print('l3:', hex(id(l3)), l3)

l1.clear() # 리스트의 메서드 이용
del l2[:]  # 내장 명령어를 이용
l3 = []    # 변수에 빈 리스트를 할당해서 대체

print('l1:', hex(id(l1)), l1) # 기존 주소 유지
print('l2:', hex(id(l2)), l2) # 기본 주소 유지
print('l3:', hex(id(l3)), l3) # 주소가 변경

