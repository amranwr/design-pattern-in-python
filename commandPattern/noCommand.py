from commandPattern.command import Command
class NoCommand(Command):
    def execute(self):
        print("there is no command here bro !!!")