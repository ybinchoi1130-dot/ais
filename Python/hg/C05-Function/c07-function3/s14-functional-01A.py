# -*- coding: utf-8 -*-

# 함수형 프로그래밍(Functional Programming)

#%%

# 글로벌 변수
# 경고창이 호출된 횟수를 카운트
gcount = 0

#%%

# 경고창을 출력하는 함수
def makeAlert(name, count):
    def alert(message):
        global gcount
        gcount += 1
        # UnboundLocalError: cannot access local variable 'count' 
        # where it is not associated with a value
        # count += 1
        print(f"[{name}] count({count}), gcount({gcount}): {message}")
        
    return alert

#%%

infoAlert = makeAlert("INFO", gcount)
warnAlert = makeAlert("WARN", gcount)

# 함수 이름으로 용도를 결정
infoAlert("눈길을 주의하세요.")
infoAlert("빗길을 조심하세요.")

warnAlert("공사중, 도로끝")
warnAlert("홍수로 도로소실!!!")

#%%
