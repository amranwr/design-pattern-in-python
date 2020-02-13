from commandPattern.command import Command
from commandPattern.garageDoor import GarageDoor


class GarageDoorClose(Command):
    garageDoor = None

    def __init__(self):
        self.garageDoor = GarageDoor()

    def execute(self):
        self.garageDoor.close()
