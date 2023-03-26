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
    
    def check_condition(coupon):
        pass

cart_1245 = Cart(price = "1000", net_promotion = "20", net_coupon = "20", net_price = "600")
cart_2345 = Cart(price = "2344", net_promotion = "15", net_coupon = "30", net_price = "1290")
cart_4634 = Cart(price = "1034", net_promotion = "0", net_coupon = "40", net_price = "620")
cart_5678 = Cart(price = "5432", net_promotion = "25", net_coupon = "50", net_price = "1358")

print(cart_1245)