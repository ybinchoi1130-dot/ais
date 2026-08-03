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
# 전역변수: dict
gcounts = {
    'GLOBAL':0, #전체호출횟수
    'INFO':0, #정보 호출 횟수
    'WARN':0} #경고 호출 횟수




#%%
# global 변수: 객체형인 경우는 생략가능 왠만하면 사용
# 경고창을 출력하는 함수
def makeAlert(name):
    def alert(message):
        # global gcounts #생략가능
        gcounts['GLOBAL']+=1
        gcounts[name] += 1
        print(f"[{name}] gcounts({name}): {message}")
        
    return alert

#%%

infoAlert = makeAlert("INFO")
warnAlert = makeAlert("WARN")

infoAlert("새로운 사용자가 접속을 하였습니다.")
infoAlert("비번이 변경 되었습니다.")        

warnAlert("다른 네트워크에서 로그인이 되었습니다.")

warnAlert("로그인이 5번 연속해서 실패했습니다.")
print("gcount:",gcounts)
