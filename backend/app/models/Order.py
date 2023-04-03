import weakref
class Order():
    instances = []
    def __init__ (self,id,status,date):
        self.__id = id
        self.__status = status
        self.__date = date 
        self.all_instances()
        # self.__order = order
    @property
    def id(self):
        return self.__id
    @property
    def status(self):
        return self.__status
    @property
    def date(self):
        return self.__date
    
    def collect_order(status):
        pass
    def add_course(Course):
        pass
    def update_status_order(order):
        pass
    def remove_course(Course):
        pass
    def all_instances(self):
        self.__class__.instances.append(weakref.proxy(self))
    def __str__(self) -> str:
        return str([{ "id" : self.id, "status" : self.status, "date" : self.date}])
    

order1 = Order(id = "2233", status = "finish", date = "24-5-2022")
order2 = Order(id = "3456", status = "unfinish", date = "28-6-2022")
order3 = Order(id = "5677", status = "unfinish", date = "23-4-2022")
order4 = Order(id = "4566", status = "finish", date = "14-3-2023")


