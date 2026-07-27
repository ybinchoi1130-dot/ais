# -*- coding: utf-8 -*-

# 제어문(if)

#%%

"""
[문제] 아래의 조건에 맞게 조건문(if)를 사용해서 결과를 출력하라.
조건:
  - 택시 기본 요금은 5000원이다.
  - 버스 기본 요금은 1500원이다.
  - 가진 돈이 5000원 이상이면 택시를 타고
  - 가진 돈이 5000원 미만이고 1500원 이상이면 버스를 탄다.
  - 그렇지 않으면 걸어 간다.
"""
#%%









#%%

money = input("가진 돈을 입력하세요:")
money = int(money) # 정수로 변환

print(f"당신이 가진 돈은 ({money})원 입니다.")

if money >= 5000:
    print("택시를 탄다.")
elif money >= 1500: # else if: 상위의 조건이 만족하지 않으면 다시 조건을 확인    
    print("버스를 탄다.")    
else:
    print("걸어간다.")    
    
#%%    

money = input("가진 돈을 입력하세요:")
money = int(money) # 정수로 변환

print(f"당신이 가진 돈은 ({money})원 입니다.")

if money >= 5000:
    print("택시를 탄다.")
else: # 5000원 미만
    if money >= 1500: # 1500원 이상
        print("버스를 탄다.")    
    else: # 1500원 미만
        print("걸어간다.")    

    
#%%

money = input("가진 돈을 입력하세요:")
money = int(money) # 정수로 변환

# bool 자료형
c5000 = money >= 5000
c1500 = money >= 1500

print(f"당신이 가진 돈은 5000원 보다 크거나 같다: {c5000}")
print(f"당신이 가진 돈은 1500원 보다 크거나 같다: {c1500}")

print(f"당신이 가진 돈은 ({money})원 입니다.")

if c5000:
    print("택시를 탄다.")
elif c1500:
    print("버스를 탄다.")    
else:
    print("걸어간다.")

#%%

money = input("가진 돈을 입력하세요:")
money = int(money) # 정수로 변환

c5000 = money >= 5000
c1500 = money >= 1500

print(f"당신이 가진 돈은 5000원 보다 크거나 같다: {c5000}")
print(f"당신이 가진 돈은 1500원 보다 크거나 같다: {c1500}")

print(f"당신이 가진 돈은 ({money})원 입니다.")

if c1500:
    print("버스를 탄다.")    # 해당 문이 먼저 실행 된다.
elif c5000:
    print("택시를 탄다.")
else:
    print("걸어간다.")



    