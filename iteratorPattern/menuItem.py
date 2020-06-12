class MenuItem:
    __name = None
    __descrption = None
    def __init__(self ,name,description):
        self.__name = name
        self.__descrption = description

    def getName(self):
        return self.__name

    def getDec(self):
        return self.__descrption