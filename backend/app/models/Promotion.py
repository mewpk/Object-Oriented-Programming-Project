from datetime import datetime

class Promotion():
    def __init__(self, percent, start_date, end_date,net):
        self.__percent = percent
        self.__start_date = datetime.strptime(start_date, '%d/%m/%Y')
        self.__end_date = datetime.strptime(end_date, '%d/%m/%Y')
        self.__net = net

    @property
    def percent(self):
        return self.__percent
    @property
    def start_date(self):
        return self.__start_date
    @property
    def end_date(self):
        return self.__end_date
    @property
    def net(self):
        return self.__net
    @percent.setter
    def percent(self,percent):
        self.__percent = percent
        return self.__percent
    @start_date.setter
    def start_date(self,start_date):
        self.__start_date = start_date
        return self.__start_date
    @end_date.setter
    def end_date(self,end_date):
        self.__end_date = end_date
        return self.__end_date
    @net.setter
    def net(self,net):
        self.__net= net
        return self.__net
    
    def add_promotion(self,promotion):
        self.percent = promotion.percent
        self.start_date = promotion.start_date
        self.end_date = promotion.end_date
    
    def net_promotion_price(self,price):
        if self.percent != 0:
            self.net = int((price*(100-self.percent))/100)+1
        else : self.net = price
