from factoryPattern.Pizza import Pizza
from factoryPattern.Peparoni import Peparoni
from factoryPattern.Margrita import Margrita
class Factory():
    __des=""
    def createObj(self,name):
        des = str(name).lower()
        if(des =="margrita"):
            return Margrita()
        elif(des == "peparoni"):
            return Peparoni()
        else:
            return Margrita()
