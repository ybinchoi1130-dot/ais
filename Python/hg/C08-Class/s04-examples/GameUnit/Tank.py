from AttackUnit import *

# 탱크 유닛
class Tank(AttackUnit):
    # 클래스 변수: 객체가 생성되지 않아도 기본적으로 가지고 있는 변수, 공유 변수
    # 시지 모드 : 탱크를 지상에 고정, 이동 불가, 공격력 증가
    siege_developed = False # 시지 모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1) # 이름, 체력, 공격력, 이동 속도
        self.siege_mode = False # 시지 모드(해제 상태)

    # 시지 모드 설정
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시지 모드가 개발되지 않았으면 바로 반환
            return
        # 현재 일반 모드일 때
        if self.siege_mode == False:
            print("{0} : 시지 모드로 전환합니다.".format(self.name))
            self.damage *= 2 # 공격력 2배 증가
            self.siege_mode = True # 시지 모드 설정
        # 현재 시지 모드일 때
        else:
            print("{0} : 시지 모드를 해제합니다.".format(self.name))
            self.damage //= 2 # 공격력 절반으로 감소
            self.siege_mode = False # 시지 모드 해제