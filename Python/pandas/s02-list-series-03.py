# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:39:06 2026

@author: Solx
"""
# 리스트로 판다스의 시리즈 객체를 생성
# 시리즈의 인덱스를 리스트로 지정

import pandas as pd

# 리스트
lst = [ '2026-08-10', '홍길동', 3.14, 178, True, "HGD"]

# 명시적으로 인덱스(index)를 지정
sr = pd.Series(lst, index=[1,2,3,4,5,6])
print(sr)

#%%

"""
1    2026-08-10
2           홍길동
3          3.14
4           178
5          True
6           HGD
dtype: object
"""

#%%

# 인덱스의 순번을 range()를 이용하여
# 1부터 순차적으로 자동 부여
# len(lst) + 1을 한 이유?
#   -> 시작번호가 1부터 시작했기 때문이다.
#   -> range()의 종료 번호는  n - 1이므로 1을 더해주어야 한다.
start_num = 1          # 인덱스의 시작번호
end_num = len(lst) + 1 # 인덱스의 종료번호
sr2 = pd.Series(lst, index=range(start_num, end_num))
print(sr2)

#%%

"""
1    2026-08-10
2           홍길동
3          3.14
4           178
5          True
6           HGD
dtype: object
"""

