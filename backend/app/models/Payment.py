class Payment(): 
    def __init__(self,country,method):
        self.__country = country
        self.__method = [method]
    @property
    def country(self):
        return self.__country
    @property
    def method(self):
        return self.__method
