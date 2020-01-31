from decoratorPattern.pizza import Pizza


class Pepperoni(Pizza):
    __price = None

    def __init__(self):
        self.__price = 6

    def display(self):
        print("pizza pepperoni ")

    def price(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price
