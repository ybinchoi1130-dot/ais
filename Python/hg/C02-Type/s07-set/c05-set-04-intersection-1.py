# 집합 자료형(set)
# 양쪽 공통되는 값을 선택
#
# 교집합: &
# 메소드: set.intersection()

s1 = set('123456')
s2 = set('456789')

print(s1) # {'2', '1', '4', '3', '6', '5'}
print(s2) # {'8', '4', '7', '9', '6', '5'}

#%%
#내장 함수
s1_sorted = sorted(s1)
s2_sorted = sorted(s2)

print(type(s1_sorted), s1_sorted)
print(type(s2_sorted), s2_sorted)
#%%
sg= s1 &s2
print('sg:',sg)

#%%

# 양쪽 공통되는 값을 선택 : &
s3 = s1 & s2
print('s3:', sorted(s3)) # s3: ['4', '5', '6']

#%% 

s4 = s1.intersection(s2)
print('s4:', sorted(s4)) # s4: ['4', '5', '6']

#%%

s5 = s2.intersection(s1)
print('s5:', sorted(s5)) # s5: ['4', '5', '6']


    