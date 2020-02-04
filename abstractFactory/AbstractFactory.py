from abc import ABC, abstractmethod


class Factory:
    __obj = None
    @abstractmethod
    def createObject(self):
        pass
