from random import *

from Soldier import Soldier
from Tank import Tank
from Stealth import Stealth

# 게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

# 게임 종료
def game_over():
    print("Player : Good Game")
    print("[Player] 님이 게임에서 퇴장했습니다.")

# 실제 게임 진행
game_start() # 게임 시작

# 보병 3기 생성
so1 = Soldier()
so2 = Soldier()
so3 = Soldier()

# 탱크 2기 생성
ta1 = Tank()
ta2 = Tank()

# 전투기 1기 생성
st1 = Stealth()

# 유닛 일괄 관리(생성된 모든 유닛 추가)
attack_units = []
attack_units.append(so1)
attack_units.append(so2)
attack_units.append(so3)
attack_units.append(ta1)
attack_units.append(ta2)
attack_units.append(st1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시지 모드 개발
Tank.siege_developed = True
print("[알림] 탱크의 시지 모드 개발이 완료됐습니다.")

# 공격 모드 준비(보병: 강화제, 탱크: 시지 모드, 전투기: 은폐 모드)
for unit in attack_units:
    if isinstance(unit, Soldier): # Soldier 클래스의 인스턴스이면 강화제
        unit.booster()
    elif isinstance(unit, Tank): # Tank 클래스의 인스턴스이면 시지 모드
        unit.set_siege_mode()
    elif isinstance(unit, Stealth): # Stealth 클래스의 인스턴스이면 은폐 모드
        unit.cloaking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 피해는 무작위로 받음(5~20)
    
# 게임 종료
game_over()
