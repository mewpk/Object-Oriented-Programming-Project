from datetime import datetime

class Coupon():
    def __init__(self, id, passcode, start_date, end_date, type,condition):
        self._id = id
        self._passcode = passcode
        self._start_date = datetime.strptime(start_date, '%d/%m/%Y')
        self._end_date = datetime.strptime(end_date, '%d/%m/%Y')
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
    

class CouponInstructor(Coupon):
    def __init__(self, id, passcode, start_date, end_date, type,condition):
        super().__init__(id, passcode, start_date, end_date, type,condition)

class CouponAll(Coupon):
    def __init__(self, id, passcode, start_date, end_date, type,condition):
        super().__init__(id, passcode, start_date, end_date,type,condition)
