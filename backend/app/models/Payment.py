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
    
    def add_payment_method(self,method):
        self.method.append(method)
        return self.method
    
    def __str__(self) -> str:
        return str ( [ {"contry" : self.__country  , "method" : self.__method} ])

payment1 = Payment(country = "Thailand", method = "credit card")
payment2 = Payment(country = "Laos", method = "credit card")
payment3 = Payment(country = "Thailand", method = "debit card")
payment4 = Payment(country = "Myanmar", method = "debit card")