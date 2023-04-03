class CouponCollection():
    def __init__(self) -> None:
        self.__coupon = []
    @property
    def coupon(self):
        return self.__coupon