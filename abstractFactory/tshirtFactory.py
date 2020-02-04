from abstractFactory.AbstractFactory import Factory
from abstractFactory.greenShirt import GreenShirt
from abstractFactory.whiteShirt import WhiteShirt

class TshirtFactory(Factory):
    def createObject(self,name):
        name = str(name).lower()
        if name == "green":
            self.__obj = GreenShirt()
        elif name == "white":
            self.__obj = WhiteShirt()
        else :
            self.__obj = GreenShirt()

        return self.__obj
