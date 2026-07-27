# 리스트 정렬
#  리스트.sort()
# 요소의 위치를 순서대로 변경
# 오름차순 : 작은 값에서 큰 값 순서
# 원본 데이터의 위치가 변경

lst = [4,7,3,10,99,22]

print(lst) # [4, 7, 3, 10, 99, 22]

# 정렬 오름차순(ascendi)
lst.sort()

print(lst) # [3, 4, 7, 10, 22, 99]

#%%

# 주의 사항
lst.append('end')
print(lst)

#%%
# 문자열과 숫자는 혼용되어 있는 요소의 정렬은 불가
# TypeError: '<' not supported between instances of 'str' and 'int'
# lst.sort()

#%%

# 문자열은 유니코드(unicode) 값의 순서로 정렬을 한다.
lstr = ['한글', 'x', 'start', 'a', 'end', 'abc', 'abx', '기역']
lstr.sort()
print(lstr) # ['a', 'abc', 'abx', 'end', 'start', 'x',  '기역', '한글']

#%%

# 내림차순
lstr = ['한글', 'x', 'start', 'a', 'end', 'abc', 'abx', '기역']
lstr.sort(reverse=True) 
print(lstr) # ['한글', '기역', 'x', 'start', 'end', 'abx', 'abc', 'a']

#%%

# 내림차순으로 정렬이 되며 반전이 되지 않는다.
lstr.sort(reverse=True) 
print(lstr) # ['한글', '기역', 'x', 'start', 'end', 'abx', 'abc', 'a']

#%%

# 반전 
lstr.reverse()
print(lstr) # ['a', 'abc', 'abx', 'end', 'start', 'x', '기역', '한글']

#%%

# 뒤집기 오름차순이나 내림차순으로 정렬을 안하고 단순반전 용어
lstr = ['한글', 'x', 'start', 'a', 'end', 'abc', 'abx', '기역']
lstr.reverse() 
print(lstr) # ['기역', 'abx', 'abc', 'end', 'a', 'start', 'x', '한글']

lstr.reverse()
print(lstr) # ['한글', 'x', 'start', 'a', 'end', 'abc', 'abx', '기역']




