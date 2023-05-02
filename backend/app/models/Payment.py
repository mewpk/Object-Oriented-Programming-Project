class Payment(): 
    def __init__(self,name,amount,type):
        self.__name = name
        self.__amount = amount
        self.__type = type

    @property
    def name(self):
        return self.__name
    @property
    def amount(self):
        return self.__amount
    @property
    def type(self):
        return self.__type
    
        
    