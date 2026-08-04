# -*- coding: utf-8 -*-

# 모듈에서 함수나 변수의 이름을 변경해서 사용할 수 있다.

# from 모듈명 import 함수 as 별칭
# from 모듈명 import 변수 as 별칭

# 동일한 이름으로 중복이 되면 맨 나중에 지정된 것이 사용된다.
from cals import PI as pi # math.pi에 의해서 대체
from math import pi

print("원주율:", pi) # 3.141592653589793
print("원주율:", pi) # 3.141592653589793

#%%

from math import pi       # cals.PI에 의해서 대체
from cals import PI as pi

print("원주율:", pi) # 3.141592
print("원주율:", pi) # 3.141592


