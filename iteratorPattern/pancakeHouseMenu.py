from iteratorPattern.menuItem import  MenuItem
class PancakeHouseMenu:
    __mylist =None
    def __init__(self):
        self.__mylist = list()
        self.__mylist.append( MenuItem("Fakin Bacon with lettuce  tomato on whole wheat",  2.99))

    def addItem(self,name ,desc):
        menuItem = MenuItem(name,desc)
        self.__mylist.append(menuItem)


    def createIterator(self):
        return iter(self.__mylist)


