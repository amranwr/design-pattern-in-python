from singleton.milkshop import Singleton
import threading
lock = threading.Lock()
t1 = threading.Thread(target=Singleton(),args=(lock,))
t2 = threading.Thread(target=Singleton(),args=(lock,))


