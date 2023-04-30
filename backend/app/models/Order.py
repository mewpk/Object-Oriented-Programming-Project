from datetime import datetime
class Order():
    order_id = 1
    def __init__ (self,status,course,net_price):
        self.__id = Order.order_id
        self.__status = status
        self.__date = datetime.now() 
        self.__course = course
        self.__net_price = net_price
        Order.order_id += 1
        
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
    def net_price(self):
        return self.__net_price
    @status.setter
    def status(self,status):
        self.__status = status
        return self.__status

 

