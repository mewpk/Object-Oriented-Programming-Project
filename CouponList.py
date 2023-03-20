class CouponList():
    def __init__(self,type):
        self._type = type
    def check_coupon(self,code):
        pass
    def check_condition(self,coupon):
        pass

coupon1 = CouponList(type='CouponCourse')
coupon2 = CouponList(type='CouponInstructor')
coupon3 = CouponList(type='CouponAll')