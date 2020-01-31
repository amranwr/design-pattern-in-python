from decoratorPattern.here import *

obj_first = Pepperoni()
obj_second = Mozzarella(obj_first)
obj_third = Mozzarella(obj_second)

obj_third.display()
print(obj_third.price())