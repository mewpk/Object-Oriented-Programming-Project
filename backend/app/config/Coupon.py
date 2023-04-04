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