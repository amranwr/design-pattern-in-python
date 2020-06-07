import threading

class Singleton(object):
    __intance = None
    x = None
    def __new__(cls):
        if  cls.__intance == None:
            cls.__intance = super(Singleton,cls).__new__(cls)
        return cls.__intance


