# 반복문(while)

# 예금을 예치하여 복리이자 계산
# 원금 10만원, 이자가 연 10%, 만기 10년, 복리로 계산하라.
# 단: while문을 이용하라.
count=1
year=10
won = 100000
total= won
#rate_percent = float(input("연 이자율을 입력하세요 "))
#rate = rate_percent /100
rate = 0.10
while count <=year:
    total += total * rate
    print(f"{count}년 : 금액{round(total)}")
    count += 1

print(f"{(year)}년 만기통장금액은 {round(total)}원입니다.")

#%%
year =10
won = 100000
total = won
rate = 0.10
for n in range(year):
    cost = total * rate
    print(f"{n+1}년 이자금액은{round(cost)}원")
    total += cost
    print(f"금액은{round(total)}원")
    n += 1

print(f"{(year)}년 만기통장금액은 {round(total)}원입니다.")

#%%
year =10
won = 100000
total = won
rate = 0.10

for n in range(year):
    cost = won *rate
    print(f"{n+1}년 이자금액은{round(cost)}원")
    total += cost
    print(f"금액은{round(total)}원")
    n+=1
    
print(f"{(year)}년 만기통장금액은 {round(total)}원입니다.")