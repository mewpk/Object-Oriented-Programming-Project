class Coupon():
    def __init__(self, id, passcode, start_date, end_date, type,condition):
        self._id = id
        self._passcode = passcode
        self._start_date = start_date
        self._end_date = end_date
        self._type = type
        self._condition = condition
    @property
    def id(self):
        return self._id
    @property
    def passcode(self):
        return self._passcode
    @property
    def start_date(self):
        return self._start_date
    @property
    def end_date(self):
        return self._end_date
    @property
    def type(self):
        return self._type
    @property
    def condition(self):
        return self._condition
        
class CouponCourse(Coupon):
    def __init__(self, id, passcode, start_date, end_date, type,condition):
        super().__init__(id, passcode, start_date, end_date, type,condition)
    

coupon1 = CouponCourse(
    id = '123',
    passcode = '123456ab',
    start_date = '21/01/66',
    end_date = '30/01/66',
    type = 'CouponCourse' ,
    condition = 'ยอดซื้อขั้นต่ำ500'
)

coupon5 = CouponCourse(
    id = '127',
    passcode = '10894ak',
    start_date = '02/02/66',
    end_date = '30/02/66',
    type = 'CouponCourse' ,
    condition = 'เฉพาะคอร์สที่อยู่ในหมวด python'
)



class CouponInstructor(Coupon):
    def __init__(self, id, passcode, start_date, end_date, type,condition):
        super().__init__(id, passcode, start_date, end_date, type,condition)


coupon2 = CouponInstructor(
    id = '124',
    passcode = '123776af',
    start_date = '2/02/66',
    end_date = '14/02/66',
    type = 'CouponInstructor' ,
    condition = 'ยอดซื้อขั้นต่ำ 500 บาท'
)

coupon6 = CouponInstructor(
    id = '128',
    passcode = '120843f',
    start_date = '14/02/66',
    end_date = '20/02/66',
    type = 'CouponInstructor' ,
    condition = 'เฉพาะลูกค้าที่เคยซื้อคอร์สกับผู้สอนมาแล้วอย่างน้อย 1 คอร์ส'
)

class CouponAll(Coupon):
    def __init__(self, id, passcode, start_date, end_date, type,condition):
        super().__init__(id, passcode, start_date, end_date,type,condition)

coupon3 = CouponAll(
    id = '125',
    passcode = '0094kl00',
    start_date = '22/02/66',
    end_date = '16/03/66',
    type = 'CouponAll' ,
    condition = 'ยอดซื้อขั้นต่ำ 1000 บาท'
)

coupon7 = CouponAll(
    id = '129',
    passcode = '0123l00',
    start_date = '22/02/66',
    end_date = '16/03/66',
    type = 'CouponAll' ,
    condition = 'เฉพาะลูกค้าที่เคยซื้อคอร์สเรียนมาก่อน'
)