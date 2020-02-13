from commandPattern.garageDoor import GarageDoor
from commandPattern.light import Light
from commandPattern.lightOff import LightOff
from commandPattern.ligtOn import LightOn
from commandPattern.remote import Remote
from commandPattern.water import Water

remote = Remote(3)
lightOn = LightOn()
lightOff = LightOff()


remote.setCommand(1,lightOn,lightOff)


remote.buttonPressedOn(1,"on")
remote.undo()