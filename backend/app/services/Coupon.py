from ..config.Coupon import CouponCollection

class CouponService():
    def add_coupon(self, new_coupon):
        CouponCollection.coupon.append(new_coupon)