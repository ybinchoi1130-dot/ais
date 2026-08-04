
from AttackUnit import AttackUnit
from Flyable import Flyable

# 공중 공격 유닛
# 다중 상속: AttackUnit, Flyable
class FlyableAttackUnit(AttackUnit, Flyable): 
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)