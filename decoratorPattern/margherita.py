from decoratorPattern.pizza import Pizza


class Margherita(Pizza):
    __price = None

    def __init__(self):
        self.__price = 5

    def display(self):
        return "pizza margherita"

    def price(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price
