
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name    # 이름
        self.hp = hp        # 체력
        self.speed = speed  # 공격력
        print("{0} 유닛을 생성했습니다.".format(name))

    def move(self, location): # 이동
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))

    def damaged(self, damage): # 피해정도
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))
