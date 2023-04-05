class Cart():
    def __init__(self,price,net_promotion,net_coupon,net_price):
        self.__price = price
        self.__net_promotion = net_promotion
        self.__net_coupon = net_coupon
        self.__net_price = net_price
    @property
    def price(self):
        return self.__price
    @property
    def net_promotion(self):
        return self.__net_promotion
    @property
    def net_coupon(self) :
        return self.__net_coupon
    @property
    def net_price(self) :
        return self.__net_price
    
    
    @price.setter
    def price(self,price):
        self.__price = price
        return self.__price
    @net_promotion.setter
    def net_promotion(self,net_promotion):
        self.__net_promotion = net_promotion
        return self.__net_promotion
    @net_coupon.setter
    def net_coupon(self,net_coupon):
        self.__net_coupon = net_coupon
        return self.__net_coupon
    @net_price.setter
    def net_price(self,net_price):
        self.__net_price = net_price
        return self.__net_price
