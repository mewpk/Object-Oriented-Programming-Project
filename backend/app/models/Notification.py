class Notification():
    def __init__(self,id,date,description):
        self.__id = id
        self.__date = date
        self.__description = description
    @property
    def id(self):
        return self.__id
    @property
    def date(self):
        return self.__date
    @property
    def description(self):
        return self.__description


