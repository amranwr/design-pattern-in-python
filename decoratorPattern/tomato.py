from decoratorPattern.decorator import ToppingDecorator


class Tomato(ToppingDecorator):
    def __init__(self, obj):
        self.obj_pizza = obj
        self.money = 2

    def price(self):
        return self.obj_pizza.price() + self.money

    def display(self):
        return self.obj_pizza.display()+"+tomato "

    def setPrice(self, obj):
        self.money = obj
