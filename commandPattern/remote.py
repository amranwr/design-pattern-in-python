from commandPattern.noCommand import NoCommand
from commandPattern.command import Command
from commandPattern.lightOff import LightOff
from commandPattern.ligtOn import LightOn
class Remote :
    commandsOn = None
    commandsOff =  None
    undoCommand = None
    size = None

    def __init__(self,size):
        self.commandsOff = [NoCommand()] *size
        self.commandsOn = [NoCommand()] *size
        self.size = size

    def setCommand(self,slot,commandOn,commandOff):
        if slot <= self.size or slot <= 0:
            self.commandsOn[slot-1] = commandOn
            self.commandsOff[slot-1]= commandOff
        else:
            self.commandsOff[self.size - 1]=commandOff
            self.commandsOn[self.size -1] = commandOn


    def buttonPressedOn(self,slot,decision):
        if decision =="on":
            self.commandsOn[slot-1].execute()
            self.undoCommand = self.commandsOff[slot-1]
        else:
            self.commandsOff[slot-1].execute()
            self.undoCommand = self.commandsOn[slot-1]

    def undo(self):
        if self.undoCommand:
            self.undoCommand.execute()


