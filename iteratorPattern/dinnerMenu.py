from iteratorPattern.menuItem import MenuItem
class DinnerMenu:
    __myMap = None
    __pos = 1
    def __init__(self):
        self.__myMap = dict()
        self.__myMap[self.__pos]=MenuItem("Fakin Bacon with lettuce  tomato on whole wheat", 2.99)
        self.__pos+=1

    def addItem(self,name,desc):
        menuItem = MenuItem(name,desc)
        self.__myMap[menuItem] = pos

    def createIterator(self):
        items = self.__myMap.values()
        return iter(items)
