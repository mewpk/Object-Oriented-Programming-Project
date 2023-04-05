
from ..config.database import coupon_collection

class CouponService():
    def get_coupon():
        return coupon_collection.coupon
    def add_coupon(self, coupon):
        try :
            coupon_collection.coupon.append(coupon)
            return coupon
        except :
            return False
