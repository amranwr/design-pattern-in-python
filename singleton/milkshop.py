class Singleton(object):
    __intance = None
    x = None
    def __new__(cls):
        if not cls.__intance:
            cls.__intance = super(Singleton,cls).__new__(cls)
        return cls.__intance

