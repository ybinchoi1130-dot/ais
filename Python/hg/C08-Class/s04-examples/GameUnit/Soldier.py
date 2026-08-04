
from AttackUnit import *

# 보병 유닛
class Soldier(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "보병", 40, 5, 1) # 이름, 체력, 공격력, 이동 속도

    # 강화제: 일정 시간 동안 이동 속도와 공격 속도 증가, 체력 10 감소
    def booster(self):
        if self.hp > 10:
            self.hp -= 10 # 체력 10 소모
            print("{0} : 강화제를 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족해 기술을 사용할 수 없습니다".format(self.name))

