# 집합 자료형(set)
# a에서 b를 제외한 나머지 요소를 선택
#
# 차집합: -
# 메소드: set.difference()

s1 = set('123456')
s2 = set('456789')

print(s1) # {'2', '1', '4', '3', '6', '5'}
print(s2) # {'8', '4', '7', '9', '6', '5'}

#%%

# s1에서 s2를 제외한 나머지 요소를 선택
s3 = s1 - s2
print('s1 - s2:', sorted(s3)) # ['1', '2', '3']
 
#%%

s4 = s2 - s1
print('s2 - s1:', sorted(s4)) # ['7', '8', '9']

#%%

# s5 = s1 - s2
s5 = s1.difference(s2)
print('s1.difference(s2):', sorted(s5)) # ['1', '2', '3']
    
#%%
l1=set('대전 청주 세종 수원 화성 용인 평택 인천'.split())
l2=set('대전 청주 세종 논산 천안'.split())
print(l1)
print(l2)

l3=l2-l1
print(l3)