from datetime import datetime
class Order():
    def __init__ (self,id,status,course,price,net_price):
        self.__id = id
        self.__status = status
        self.__date = datetime.now() 
        self.__course = course
        self.__price = price
        self.__net_price  = net_price
        
    @property
    def id(self):
        return self.__id
    @property
    def status(self):
        return self.__status
    @property
    def course(self):
        return self.__course
    @property
    def date(self):
        return self.__date
    @property
    def price(self):
        return self.__price
    @property
    def net_price(self):
        return self.__net_price
    
    @status.setter
    def status(self,status):
        self.__status = status
        return self.__status

        

 

