from datetime import datetime
class Order():
    order_id = 1
    def __init__ (self,status):
        self.__id = Order.order_id
        self.__status = status
        self.__date = datetime.now() 
        Order.order_id += 1
        
    @property
    def id(self):
        return self.__id
    @property
    def status(self):
        return self.__status
 

