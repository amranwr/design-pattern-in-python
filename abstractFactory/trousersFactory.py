from abstractFactory.AbstractFactory import Factory
from abstractFactory.cloth import Cloth
from abstractFactory.jeans import Jeans
class TrousersFactory(Factory):
    def createObject(self,name):
        name = str(name).lower()
        if name == "jeans":
            self.__obj = Jeans()
        elif name == "cloth":
            self.__obj = Cloth()
        else :
            self.__obj = Jeans()

        return self.__obj
