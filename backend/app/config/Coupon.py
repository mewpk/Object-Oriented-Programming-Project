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
        return "Success"