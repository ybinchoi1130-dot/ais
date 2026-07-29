import turtle
import time
import math

# 1. 그래픽 화면 기본 설정
screen = turtle.Screen()
screen.title("숫자가 표시되는 실시간 아날로그 시계")
screen.bgcolor("#fbfbfb")  # 부드러운 화이트 배경
screen.setup(width=600, height=600)
screen.tracer(0)

# 2. 그래픽용 거북이(펜) 설정
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def draw_clock(hour, minute, second):
    pen.clear()
    
    # [1] 시계판 테두리 그리기
    pen.penup()
    pen.goto(0, -210)
    pen.pendown()
    pen.color("#333333")
    pen.pensize(6)
    pen.circle(210)
    
    # [2] 1부터 12까지 숫자 및 눈금 그리기 (원주율 활용)
    for i in range(1, 13):
# 파이썬 수학 좌표는 3시 방향이 0도이므로, 12시(90도)를 기준으로 시계방향 감산 계산
# 1시간당 각도는 360도 / 12 = 30도 (라디안 단위: math.pi / 6)
        angle = math.pi / 2 - (i * (math.pi / 6))
        
        # 눈금선 좌표 계산 (반지름 195 ~ 210 구간)
        x_line_start = 195 * math.cos(angle)
        y_line_start = 195 * math.sin(angle)
        x_line_end = 210 * math.cos(angle)
        y_line_end = 210 * math.sin(angle)
        
        pen.penup()
        pen.goto(x_line_start, y_line_start)
        pen.pendown()
        pen.pensize(3)
        pen.goto(x_line_end, y_line_end)
        
        # 숫자 글자 배치 좌표 계산 (반지름 170 안쪽 지점)
        x_text = 170 * math.cos(angle)
        # 글자 높이를 보정하기 위해 Y축 좌표를 약간 내림 (-10)
        y_text = 170 * math.sin(angle) - 10
        
        pen.penup()
        pen.goto(x_text, y_text)
        # 숫자를 정중앙 정렬(align='center')하여 예쁘게 출력
        pen.write(str(i), align="center", font=("Arial", 14, "bold"))

    # [3] 실시간 바늘 각도 계산 (12시 방향 기준)
    angle_s = math.pi / 2 - (second * (2 * math.pi / 60))
    angle_m = math.pi / 2 - (minute * (2 * math.pi / 60) + second * (2 * math.pi / 3600))
    angle_h = math.pi / 2 - ((hour % 12) * (2 * math.pi / 12) + minute * (2 * math.pi / 720))
    
    # [4] 삼각함수 좌표 변환 후 바늘 그리기
    # 시침
    pen.penup(); pen.goto(0, 0); pen.color("#222222"); pen.pensize(8); pen.pendown()
    pen.goto(100 * math.cos(angle_h), 100 * math.sin(angle_h))
    
    # 분침
    pen.penup(); pen.goto(0, 0); pen.color("#0066cc"); pen.pensize(5); pen.pendown()
    pen.goto(145 * math.cos(angle_m), 145 * math.sin(angle_m))
    
    # 초침
    pen.penup(); pen.goto(0, 0); pen.color("#ff3333"); pen.pensize(2); pen.pendown()
    pen.goto(175 * math.cos(angle_s), 175 * math.sin(angle_s))
    
    # 중앙 고정 핀 데코
    pen.penup(); pen.goto(0, -6); pen.color("#222222"); pen.pendown(); pen.begin_fill(); pen.circle(6); pen.end_fill()

# 3. 메인 루프 (실시간 컴퓨터 시간 동기화)
while True:
    now = time.localtime()
    draw_clock(now.tm_hour, now.tm_min, now.tm_sec)
    screen.update()
    time.sleep(0.2)
