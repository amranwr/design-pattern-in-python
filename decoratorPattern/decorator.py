from decoratorPattern.pizza import Pizza
from abc import ABC, abstractmethod


class ToppingDecorator(Pizza, ABC):
    obj_pizza = None
    money = None
    def __init__(self, obj):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def setPrice(self,obj):
        pass
