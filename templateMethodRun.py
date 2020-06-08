from templateMethodPattern.coffe import CoffeeWithHock
from templateMethodPattern.tea import Tea
item = Tea()
item2 = CoffeeWithHock()

item.prepareRecipe()
print()
item2.prepareRecipe()