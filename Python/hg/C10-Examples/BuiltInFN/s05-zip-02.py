# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:12:51 2024

@author: Solero
"""

# zip()
# zip(*iterable)
# 여러개로 구성된 데이터를 묶어서 리턴

#%%

kw = ['월','화','수','목','금','토','일']
ew = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

weeks = tuple(zip(kw,ew))

print(weeks)
# (('월', 'Mon'), 
#  ('화', 'Tue'), 
#  ('수', 'Wed'), 
#  ('목', 'Thu'), 
#  ('금', 'Fri'), 
#  ('토', ',Sat'), 
#  ('일', 'Sun'))

#%%

for week in weeks:
    print(week)
    
"""
('월', 'Mon')
('화', 'Tue')
('수', 'Wed')
('목', 'Thu')
('금', 'Fri')
('토', 'Sat')
('일', 'Sun')    
"""    

#%%
   
# 딕셔너리로 변환(dict)
dweeks = dict(zip(kw,ew))
print(dweeks)
"""
{'월': 'Mon', 
 '화': 'Tue', 
 '수': 'Wed', 
 '목': 'Thu', 
 '금': 'Fri', 
 '토': 'Sat', 
 '일': 'Sun'}
"""





