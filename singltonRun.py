from singleton.milkshop import Singleton

first_obj = Singleton()
first_obj.x = 10
second_obj = Singleton()
second_obj.x = 20
print("s1 : {} \ns2 : {}".format(first_obj.x,second_obj.x))


