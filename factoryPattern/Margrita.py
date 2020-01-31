from factoryPattern.Pizza import Pizza
class Margrita(Pizza):
    __des=""
    __price=""
    def __init__(self):
        self.des = "pizza margrita"
        self.price = 5
    def display(self):
        print(self.des)

    def price(self):
        print(self.price)