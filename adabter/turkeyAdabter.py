from adabter import duck
class TurkeyAdabter(duck):
    tempTurkey = None
    def __init__(self,item):
        self.tempTurkey = item
    def quack(self):
        self.tempTurkey.gobble()

    def fly(self):
        self.tempTurkey.fly()