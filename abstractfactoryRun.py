from abstractFactory.here import *

trouser_factory = TrousersFactory()
tshirt_factory = TshirtFactory()
obj = trouser_factory.createObject("jeans")
obj2 = tshirt_factory.createObject("Green")

obj.display()
obj2.display()