from ..config.database import cart_collection,course_collection,coupon_collection
# from .Coupon import Coupon
class Cart():
    def __init__(self):
        self.__price = 0
        self.__net_promotion = 0
        self.__net_coupon = 0
        self.__net_price = 0
        self.__course = []
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
    @property
    def course(self):
        return self.__course
       
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
    
    def add_to_cart(self,course):
        self.course.append(course)
        return "success"
            
    def remove_from_cart(self,course):
        self.course.remove(course)
        return "success"
    
    def total_price(self):
        total = 0
        for course in self.course:
            total += course.price 
        return total
    
    def total_promotion(self):
        print("to total promotion")
        total = 0
        for course in self.__course:
            total += (course.price*(100-course.promotion))/100
            print(course.price,course.promotion)
            print("total :",total)
        print("total after loop :",total)
        return total
           
    def total_net_price(self,coupon):
        total_price = self.total_promotion() - coupon
        return total_price
