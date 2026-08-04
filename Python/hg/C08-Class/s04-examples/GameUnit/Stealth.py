
from FlyableAttackUnit import FlyableAttackUnit

# 전투기 유닛
class Stealth(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "전투기", 80, 20, 5) # 이름, 체력, 공격력, 이동 속도
        self.cloaked = False # 은폐 모드(해제 상태)

    # 은폐 모드: 토글(toggle)
    def cloaking(self):
    # 현재 은폐 모드일 때
        if self.cloaked == True:
            print("{0} : 은폐 모드를 해제합니다.".format(self.name))
            self.cloaked = False
        # 현재 은폐 모드가 아닐 때
        else:
            print("{0} : 은폐 모드를 설정합니다.".format(self.name))
            self.cloaked = True