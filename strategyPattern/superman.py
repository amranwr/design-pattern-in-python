from strategyPattern.hero import Hero
from strategyPattern.ice import Ice

class Superman(Hero):
    def __init__(self):
        self.power = Ice()

    def superPower(self):
        self.power.pwr()