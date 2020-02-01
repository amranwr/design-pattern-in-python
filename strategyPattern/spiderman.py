from strategyPattern.hero import Hero
from strategyPattern.fire import Fire


class Spiderman(Hero):
    def __init__(self):
        self.power = Fire()

    def superPower(self):
        self.power.pwr()
