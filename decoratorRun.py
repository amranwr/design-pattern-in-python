from decoratorPattern.here import *

obj_first = Pepperoni()
obj_second = Mozzarella(obj_first)
obj_third = Tomato(obj_second)

print("order: "+obj_third.display())
print("price: "+str(obj_third.price())+" LE.")