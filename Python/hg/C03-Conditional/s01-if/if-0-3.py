# -*- coding: utf-8 -*-

# 조건문(if)

"""
# [문제]
# 내가 가진 돈에 따라서 마실 음료수를 구매하는데
# 가진 돈에 따라서 가장 비싼 음료수를 선택한다.
# 가격: 생수 1000원, 사이다 2000원, 커피 3000원
# 조건: 생수, 사이다, 커피 순으로 조건을 물어서 선택한다.
# 그리고 가진 돈인 1000원 미만이면 수도물을 마신다.
"""
#%%%

money = int(input("가진 돈은 얼마인가?"))

print(f"당신이 가진돈은 {money}원 입니다.")


if money < 2000:
    print("생수를 구매한다")
elif money < 3000:
    print("사이다를 구매한다")
elif money > 3000:
    print("커피를 구매한다")
else :
    print("수도물을 마신다")
    



















#%%

money = int(input("당신이 가진 돈은 얼마인가? "))

print(f"당신이 가진 돈은 {money}원 입니다.")

if money < 1000:
    print('수도물을 마신다.')
elif money < 2000:
    print("생수를 산다.")    
elif money < 3000:
    print("사이다를 산다.")
else:
    print("커피를 산다.")    
    
#%%

money = int(input("당신이 가진 돈은 얼마인가? "))

print(f"당신이 가진 돈은 {money}원 입니다.")

# 비교연산자가(>=, <, ...)가 논리연산자(and, or) 보다 우선순위가 높다.
if money >= 1000 and money < 2000: 
    print("생수를 산다.")    
elif (money >= 2000) and (money < 3000): # 괄호로 연산자 우선순위를 지정해도 된다.
    print("사이다를 산다.")
elif money >= 3000:
    print("커피를 산다.")     
else:
    print('수도물을 마신다.')

