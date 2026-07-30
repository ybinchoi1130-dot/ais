# -*- coding: utf-8 -*-

# 함수형 프로그래밍(Functional Programming)

#%%

# 글로벌 변수
# makeAlert()에 의해서 만들어진 함수별로 호출된 횟수를 카운트하라.

# 전역변수
# gcount = 0

#%%

# 경고창을 출력하는 함수
def makeAlert(name):
    count = 0
    def alert(message):
        # NameError: name 'count' is not defined
        # global count 
        nonlocal count # 외부함수에 선언된 지역변수를 사용
        count += 1
        print(f"[{name}] count({count}): {message}")
        
    return alert

#%%

infoAlert = makeAlert("INFO")
warnAlert = makeAlert("WARN")

infoAlert("눈길을 주의하세요.") # count: 1
infoAlert("빗길을 조심하세요.") # count: 2

warnAlert("공사중, 도로끝")     # count: 1

infoAlert("요철을 주의하세요.") # count: 2

        
