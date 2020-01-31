from decoratorPattern.decorator import ToppingDecorator


class Mozzarella(ToppingDecorator):
    def __init__(self, obj):
        self.obj_pizza = obj
        self.money = 3

    def display(self):
        return self.obj_pizza.display() +"+mozzarella "

    def price(self):
        return (self.obj_pizza.price() + self.money)

    def setPrice(self, price):
        self.money = price
