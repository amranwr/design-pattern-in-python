from observerPattern.subject import Subject
from observerPattern.amr import Amr
class Asfora(Subject):
    __name = None
    list = None

    def __init__(self):
        self.list = []
        self.__name = ""

    def __notify(self):
       for x in range(len(self.list)):
           self.list[x].update(self.__name)

    def register(self, obj):
        self.list.append(obj)

    def remove(self, obj):
        for i in range(len(self.list)):
            if self.list[i] == obj:
                del self.list[i]
                break

    def measurmentChanged(self, name):
        self.__name = name
        self.__notify()
