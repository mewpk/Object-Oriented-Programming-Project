
from .Cart import Cart
from .Favorite import Favorite
from ..config.StudentCourse import StudentCourseCollection
from ..config.Payment import PaymentCollection
from datetime import datetime


class Account():
    def __init__(self,name,username,password,language ,email,role,about = "",active = True):
        self._name = name
        self._username = username
        self._password = password
        self._language = language
        self._email = email
        self._role = role
        self._about = about
        self._active = active

    @property
    def username(self) :
        return self._username
    @property
    def name(self) :
        return self._name
    @property
    def language(self) :
        return self._language
    @property
    def password(self) :
        return self._password
    @property
    def email(self) :
        return self._email
    @property
    def role(self) :
        return self._role
    @property
    def about(self) :
        return self._about
    
    @password.setter
    def password(self,password) :
        self._password = password
        return self._password
    @name.setter
    def name(self,name) :
        self._name = name
        return self._name
    @language.setter
    def language(self,language) :
        self._language = language
        return self._language
    @email.setter
    def email(self,email) :
        self._email = email
        return self._email
    @about.setter
    def about(self,about) :
        self._about = about
        return self._about
    
class Student(Account):
    def __init__(self,name,username,password,language,email,role,about = "",active= True ):
        super().__init__(name,username,password,language,email,role,about,active)
        self.__review = []
        self.__orders  = []
        self.__cart = Cart()
        self.__favorite = Favorite()
        self.__student_course = StudentCourseCollection()
        self.__payment_method = PaymentCollection()
    @property
    def review(self):
        return self.__review        
    @property
    def orders(self) :
        return self.__orders
    @property
    def cart(self):
        return self.__cart
    @property
    def favorite(self) :
        return self.__favorite
    @property
    def student_course(self):
        return self.__student_course
    @property
    def payment_method(self):
        return self.__payment_method

    @review.setter
    def review(self,review):
        self.__review = review
        return self.__review
    @orders.setter
    def orders(self,orders):
        self.__orders = orders
        return self.__orders

    def add_payment_method(self,payment):
        self.payment_method.add_payment_method(payment)

    def get_payment_method(self,type,name):
        return self.payment_method.get_payment_method(type,name)
    
    def return_amount(self):
        self.payment_method
        
    def get_order_by_id(self,id):
        for order in self.orders:
            if order.id == id:
                return order
    
    def add_order(self,order):
        self.orders.append(order)
        self.cart.clear_cart()
        return self.orders
    
    def check_course_in_order(self,course):
        for order in self.orders:
            for course in order.course:
                if course == course:
                    return False
        return True
    
    def pending_orders(self):
        result = []
        for order in self.orders:
            if order.status == "Pending":
                result.append(order)
        return result
    
    def close_order(self,order,payment):
        order.status = "Purchased"
        payment.amount -= order.net_price
        print(order.net_price)
        self.student_course.add_course_to_student_course(order.course)
        return "success"
    
    def refund_order(self,order_id,payment):     
        for order in self.orders:
            if order.id == order_id :
                if (datetime.now() - order.date).days <= 7:   
                    order.status = "Refuned"
                    payment.amount += order.net_price
                    for course in order.course:
                        self.student_course.remove_course(course.id)
                    return True
        return False
            
    def view_refunds(self) :
        list_refunds = []
        for order in self.orders :
            if order.status == "refunded" :
                list_refunds.append(order)
        return list_refunds

    def add_to_cart(self,course):
        self.cart.add_to_cart(course)
    
    def remove_from_cart(self,course):
        self.cart.remove_from_cart(course)

    def check_course_in_cart(self,course):
        if course not in self.cart.course:
            return True
        else: 
            return False

    def add_review(self,review):
        self.review.append(review)
        return True
   
class Instructor(Account):
    def __init__(self,name,username,password,language,email,role,about=" ",description=" ",active= True,verify=False ):
        super().__init__(name,username,password,language,email,role,about,active)
        self.__description = description
        self.__verify = verify
    @property
    def description(self):
        return self.__description
    @property
    def verify(self):
        return self.__verify
    
    @description.setter
    def description(self,description):
        self.__description = description
        return self.__description
    @verify.setter
    def verify(self,verify):
        self.__verify = verify
        return self.__verify
  
class Admin(Account):
    def __init__(self,name,username,password,language,email,role,about = "",active= True ):
        super().__init__(name,username,password,language,email,role,about,active)
