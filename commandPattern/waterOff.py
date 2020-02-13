from commandPattern.command import Command
from commandPattern.water import Water
class WaterOff(Command):
    water = None
    def __init__(self):
        self.water = None

    def execute(self):
        self.water.off()