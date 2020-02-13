from commandPattern.water import Water
from commandPattern.command import Command
class WaterOn(Command):
    water = None
    def __init__(self):
        self.water = Water()


    def execute(self):
        self.water.on()