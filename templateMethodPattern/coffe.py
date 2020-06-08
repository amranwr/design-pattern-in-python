from templateMethodPattern.caffeineBeverage import CaffeineBeverage
class CoffeeWithHock(CaffeineBeverage):
    def brew(self):
        print("dripping coffee through filter!!!!")

    def addCondiments(self):
        print("adding sugar and milk!!!")