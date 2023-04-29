from datetime import datetime

class Coupon():
    def __init__(self, id, passcode, start_date, end_date, type,condition,at_least,discounted_price,discounted_percent):
        self._id = id
        self._passcode = passcode
        self._start_date = datetime.strptime(start_date, '%d/%m/%Y')
        self._end_date = datetime.strptime(end_date, '%d/%m/%Y')
        self._type = type
        self._condition = condition
        self._at_least = at_least
        self._discounted_price = discounted_price
        self._discounted_percent = discounted_percent
    
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
    @property
    def at_least(self):
        return self._at_least
    @property
    def discounted_price(self):
        return self._discounted_price
    @property
    def discounted_percent(self):
        return self._discounted_percent
        
class CouponCourse(Coupon):
    def __init__(self, id, passcode, start_date, end_date, type,condition,at_least,discounted_price,discounted_percent,course_id):
        super().__init__(id, passcode, start_date, end_date, type,condition,at_least,discounted_price,discounted_percent)
        self.__course_id = course_id
    @property
    def course_id(self):
        return self.__course_id
    

class CouponInstructor(Coupon):
    def __init__(self, id, passcode, start_date, end_date, type,condition,at_least,discounted_price,discounted_percent,instructor_name):
        super().__init__(id, passcode, start_date, end_date, type,condition,at_least,discounted_price,discounted_percent)
        self.__instructor_name = instructor_name
    @property
    def instructor_name(self):
        return self.__instructor_name

