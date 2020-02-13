from commandPattern.command import Command
from commandPattern.light import Light

class LightOff(Command):
    light = None
    def __init__(self):
        self.light = Light()

    def execute(self):
        self.light.off()