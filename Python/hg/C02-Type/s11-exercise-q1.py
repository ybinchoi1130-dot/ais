# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 10:26:25 2025

@author: solgits
"""

"""
[문제1]
지갑에 아래와 같이 돈을 가지고 있다. 
총 금액은 얼마인가?
1만원짜리 4장
1000원짜리 3장
500원짜리 동전 5개
100원짜리 동전 9개
10원짜리 동전 6개
--------------------------------------------------------
위 총 금액에서 아래의 금액을 지출하고 남은 금액은 얼마인가?
15000원짜리 2개를 지출
"""
# 1. 지갑 속 자산 정의 및 총 금액 계산
won_10000 = 4 * 10000  # 1만원짜리 4장
won_1000 = 3 * 1000    # 1000원짜리 3장
won_500 = 5 * 500      # 500원짜리 동전 5개
won_100 = 9 * 100      # 100원짜리 동전 9개
won_10 = 6 * 10        # 10원짜리 동전 6개

total_amount = won_10000 + won_1000 + won_500 + won_100 + won_10

# 2. 지출 금액 계산
expense = 15000 * 2    # 15000원짜리 2개 지출

# 3. 남은 금액 계산
remaining_amount = total_amount - expense

# 4. 결과 출력
print(f"■ 지갑 속 총 금액: {total_amount:,.0f}원")
print(f"■ 총 지출 금액  : {expense:,.0f}원")
print(f"■ 지출 후 남은 돈: {remaining_amount:,.0f}원")


#%%

"""
[문제2]
한 달 급여가 400만원이다.
분기별로 보너스가 월 급여의 30%가 지급된다.
세금은 월 수령액의 3%이다.
보너스에 대한 세금은 없다.
월 세후 수령액은 얼마인가?
연 수령액(세후 총 수령액)은 얼마인가?
총 세금은 얼마인가?
"""

# 1. 기본 조건 설정
monthly_salary = 4000000       # 월 급여: 400만 원
bonus_rate = 0.30              # 분기별 보너스 비율: 월 급여의 30%
tax_rate = 0.03                # 월 급여에 대한 세율: 3%

# 2. 항목별 계산 진행
# 월 세금 및 월 세후 수령액 (보너스 미지급 달 기준)
monthly_tax = monthly_salary * tax_rate
monthly_net_pay = monthly_salary - monthly_tax

# 분기별 보너스 (보너스에는 세금이 없음)
quarterly_bonus = monthly_salary * bonus_rate
annual_total_bonus = quarterly_bonus * 4  # 1년 = 4분기

# 연간 총 세금 및 연간 총 수령액
annual_total_tax = monthly_tax * 12
annual_net_pay = (monthly_salary * 12 - annual_total_tax) + annual_total_bonus

# 3. 결과 출력
print(f"■ 월 세후 수령액 (일반 달) : {monthly_net_pay:,.0f}원")
print(f"■ 연 수령액 (세후 총 합계) : {annual_net_pay:,.0f}원")
print(f"■ 연간 총 세금             : {annual_total_tax:,.0f}원")
#%%
# 초기 내가 한 자료 
#문제1
a=10000
b=1000
c=500
d=100
e=10
f=a*4+b*3+c*5+d*9+e*6

print("만원짜리 =",a*4)
print("천원짜리 =",b*3)
print("오백원짜리 =",c*5)
print("백원짜리 =",d*9)
print("십원짜리 =",e*6)
print("총 금액 =",f)
print("지출 금액 =",(a+(b*5))*2)
print("지출하고 남은 금액 =",f-(a+(b*5))*2)


#%%%
#문제2

a= 400
b= 0.3
c= a*0.03 
d= a*b
s="만원"

print("월급 =",a,s)
print("보너스 =",a*b,s)
print("세금 =",a*0.03,s)
print("총 연수령액 =",(a*12+d*4)-(c*12),s)
print("총 세금 =",c*12,s)