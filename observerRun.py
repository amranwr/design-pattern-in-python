# from factoryPattern.factory import Factory
from observerPattern.here import *

# publisher
# --------------------
obj_publisher = Asfora()

# subscribers
# --------------------
obj_subscriber = Amr(obj_publisher)
obj_subscriber2 = Amr(obj_publisher)
# --------------------
obj_publisher.measurmentChanged("amr")
obj_subscriber.remove()  # subscriber removing him or her -self
obj_publisher.measurmentChanged("anwr")
obj_subscriber.changeSubject(obj_publisher)  # subscribe to another subject
obj_publisher.measurmentChanged("mohamed")
