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
    def sent():
        pass

midyear_sale = Notification(id = "3345", date = "25-06-2022", description = "mid year sale start now!!!")
christmas_sale = Notification(id = "2445", date = "25-12-2022", description = "christmas sale start now hohoho!!!")
eleven_eleven_sale = Notification(id = "2342", date = "11-11-2022", description = "11.11 sale up to 50 percent")
newyear_sale = Notification(id = "2456", date = "29-12-2022", description = "new year sale start now ")

