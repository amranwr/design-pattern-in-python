from factoryPattern.Pizza import Pizza
class Peparoni(Pizza):
    __des=""
    __price=""
    def __init__(self):
        self.des = "pizza peparoni"
        self.price = 5
    def display(self):
        print(self.des)

    def price(self):
        print(self.price)