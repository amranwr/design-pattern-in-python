from iteratorPattern.dinnerMenu import DinnerMenu
from iteratorPattern.pancakeHouseMenu import PancakeHouseMenu
class Waitress:
    def __init__(self):
        self.__dinnerMenu = DinnerMenu()
        self.__pancakeMenu = PancakeHouseMenu()

    def printAllMenus(self):
        iterator1 = self.__dinnerMenu.createIterator()
        iterator2 = self.__pancakeMenu.createIterator()
        self._print(iterator1)
        self._print(iterator2)

    def _print(self,iterator):
        while True:
            try:
                item = next(iterator)
                print(item.getName())
            except StopIteration:
                break