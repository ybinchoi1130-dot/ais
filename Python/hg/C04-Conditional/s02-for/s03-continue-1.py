# 반복문(for)
# continue

scores = [200,70,80,-70,90,100, 90, 90]
total = 0
faultcnt = 0

# continue를 만나면 다음 문장을 실행하지 않고
# 다시 for문의 처음으로 이동하여 계속 실행
for score in scores:
    if score < 0 or score > 100: # 유효값 : 0부터 100까지, 나머지는 무시
        faultcnt += 1            # 유효하지 않은 데이터의 갯수
        continue
    total += score

cnt = len(scores) - faultcnt # cnt = 8 - faultcnt
avg = total / cnt

print(f"잘못된 점수의 갯수: {faultcnt}")
print(f"총점={total}, 평균={avg}")     
