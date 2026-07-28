# 집합 자료형(set)
# 양쪽 모두를 선택
# 중복되는 요소는 하나만 선택
# 
# 합집합: |
# 메소드: set.union()

s1 = set('123456')
s2 = set('456789')

print(s1) # {'2', '1', '4', '3', '6', '5'}
print(s2) # {'8', '4', '7', '9', '6', '5'}

#%%

# 양쪽 모두 선택
# 중복되는 요소는 하나만 선택
s3 = s1 | s2
print('s3:', sorted(s3)) 
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#%% 
s4 = s1.union(s2)
print('s4:', sorted(s4)) 
#  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
#%%

# AttributeError: 'set' object has no attribute 'sort'
s3.sort()

#%%

# 리스트
sl = [4,1,8]
sl.sort()
print(sl)



