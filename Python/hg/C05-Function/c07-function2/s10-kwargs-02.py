# -*- coding: utf-8 -*-

# 함수(Function)

# 가변인자
# 키워드 매개변수(kwargs)
# 호출할 때 반드시 인자에 키를 명시해야 한다.
#   - 파라미터의 요소명에 해당하는 키(key)는 호출자의 의해 결정된다.
#   - 인자: 키=값, ...
#   - named parameter 형태이다.

#%%

# 점수를 계산하는 함수
def score(**kw):
    kor = kw['kor']  # 국어
    eng = kw['eng']  # 영어
    tot = kor + eng
    avg = tot / len(kw)
    return tot, avg

#%%

tot, avg = score(kor=100, eng=90)
print("총점: ", tot)
print("평균:", avg)

#%%    

# 오류: KeyError: 'eng'
tot, avg = score(kor=100, sci=90)
print("총점: ", tot)
print("평균:", avg)
