# -*- coding: utf-8 -*-

# 함수형 프로그래밍(Functional Programming)

#%%

# [문제]
# makeAlert()에 의해서 만들어진 내부함수의 호출된 횟수를 카운트하라.
#   - 내부함수가 호출된 총 횟수를 카운드하라.
#   - 내부함수별로 호출된 횟수를 카운트하라.

#%%

# 글로벌 변수
# 경고창이 호출된 횟수를 카운트
gcount = 0

#%%

# 경고창을 출력하는 함수
def makeAlert(name):
    def alert(message):
        global gcount
        gcount += 1
        print(f"[{name}] gcount({gcount}): {message}")
        
    return alert

#%%

infoAlert = makeAlert("INFO")
warnAlert = makeAlert("WARN")

infoAlert("새로운 사용자가 접속을 하였습니다.")
infoAlert("비번이 변경 되었습니다.")        

warnAlert("다른 네트워크에서 로그인이 되었습니다.")

warnAlert("로그인이 5번 연속해서 실패했습니다.")

