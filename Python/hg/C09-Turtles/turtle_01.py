#Turtle
import turtle
import time

# 1. 스크린 및 거북이 설정
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")    # ★ 화살표를 진짜 거북이 모양으로 변경!
t.color("forestgreen") # 거북이에게 어울리는 초록색 지정
t.shapesize(2, 2)    # 거북이 크기를 2배로 키우기
t.speed(1)           # 거북이 이동 속도를 가장 느리게 (1~10 중 1)

# 2. 엉금엉금 기어가는 반복문
for i in range(4):
    # 앞으로 갈 때 조금씩 끊어서 이동하여 기어가는 느낌 주기
    for _ in range(5):
        t.forward(20)
        time.sleep(0.1) # 각 걸음마다 살짝 멈춤
        
    t.left(90) # 왼쪽으로 회전

turtle.done()