class Order():
    instances = []
    def __init__ (self,id,status,date):
        self.__id = id
        self.__status = status
        self.__date = date 
        self.all_instances()
    @property
    def id(self):
        return self.__id
    @property
    def status(self):
        return self.__status
    @property
    def date(self):
        return self.__date
    

