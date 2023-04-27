class CouponCollection():
    def __init__(self) -> None:
        self.__coupon = []
    @property
    def coupon(self):
        return self.__coupon
    @coupon.setter
    def set_coupon(self, coupon):
        self.__coupon = coupon
        return self.__coupon
    def add_coupon(self,coupon):
        try :
            self.coupon.append(coupon)
            return coupon
        except  :
            return False
    
    def get_coupon(self):
        return self.coupon
    
    def expire_coupon(self,time):
        for coupon in self.coupon:
            if coupon.end_date < time:
                self.coupon.remove(coupon)
        return "success"