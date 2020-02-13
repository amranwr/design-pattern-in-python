from commandPattern.garageDoor import GarageDoor
from commandPattern.command import Command
class GarageDoorOpen(Command):
    garage = None
    def __init__(self):
        self.garage = GarageDoor()

    def execute(self):
        self.garage.open()