class CouponCollection():
    def __init__(self) -> None:
        self.__coupons = []
    @property
    def coupons(self):
        return self.__coupons
    @coupons.setter
    def set_coupons(self, coupons):
        self.__coupons = coupons
        return self.__coupons
    
    def add_coupon(self,coupon):
        try :
            self.coupons.append(coupon)
            return coupon
        except  :
            return False

    def get_coupon_by_passcode(self,passcode):
        for coupon in self.coupons:
            if coupon.passcode == passcode:
                return coupon
    
    def expire_coupon(self,time):
        for coupon in self.coupons:
            if coupon.end_date < time:
                self.coupons.remove(coupon)
        return "Coupon updated successfully"
    
    def use_coupon(self,coupon,cart,total):
        cart.net_promotion = cart.total_promotion() 
        if total >= coupon.at_least:
            if coupon.type == "Instructor":
                total = self.use_coupon_instructor(coupon,cart)
            elif coupon.type == "Course":
                total = self.use_coupon_course(coupon,cart)
            discount = int((total*coupon.discounted_percent)/100 + coupon.discounted_price)   
            cart.net_coupon = cart.net_promotion - discount
            # cart.net_price = cart.net_coupon  
            return cart.net_coupon

    def use_coupon_course(self,coupon,cart):
        for course in cart.course:
            if course.id == coupon.course_id :
                return course.price 

    def use_coupon_instructor(self,coupon,cart):
        total = 0
        for course in cart.course:
            if course.instructor == coupon.instructor_name:
                total += course.price
        if total != 0 :
            return total
        
    def show_coupon_type(self,type):
        result = []
        for coupon in self.coupons:
            if coupon.type == type:
                result.append(coupon)
        return result
