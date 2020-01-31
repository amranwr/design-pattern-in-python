from observerPattern.observers import Observer
from observerPattern.display import Display

class Amr(Observer, Display):
    name = None
    __obj = None

    def __init__(self, obj):
        self.__obj = obj
        self.__attach()

    def update(self, myname):
        self.name = myname
        self.__display()

    def __display(self):
        print(self.name)

    def __attach(self):
        self.__obj.register(self)

    def changeSubject(self, obj):
        self.__obj = obj
        self.__attach()

    def remove(self):
        self.__obj.remove(self)
        self.__obj = None
