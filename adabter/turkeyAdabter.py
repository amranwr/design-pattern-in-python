from adabter.duck import Duck
from adabter.turkey import Turkey
class TurkeyAdabter(Duck):
    __bird = None
    def __init__(self,bird):
        self.__bird = bird
    def quack(self):
        self.__bird.gobble()
    def fly(self):
        self.__bird.fly()