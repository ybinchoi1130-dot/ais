# 예외처리(Exception)
# KeyError: 
# Raised when a mapping (dictionary) key is not found in the set of existing keys.    

d = {
     1: '하나',
     3: '셋',
     5: '다섯'
}

print(d[1])
print(d[3])
print(d[5])
print(d[7]) # KeyError: 7

#%%

try:
    key = 7
    print(d[key])
except KeyError as e:
    print(f"딕셔너리에서 해당하는 키({e})가 존재하지 않습니다.")    
    