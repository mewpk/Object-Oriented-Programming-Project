from .Cart import Cart
from .Order import Order
from .Favorite import Favorite
from ..config.database import studentcourse_collection
from .Payment import Payment
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
        self.__student_course = studentcourse_collection
        self.__wallet = 0
        self.__payment = []
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
    def wallet(self):
        return self.__wallet
    @property
    def payment(self):
        return self.__payment

    @review.setter
    def review(self,review):
        self.__review = review
        return self.__review
    @orders.setter
    def orders(self,orders):
        self.__orders = orders
        return self.__orders
    @wallet.setter
    def wallet(self,wallet):
        self.__wallet = wallet
        return self.__wallet
    
    #make payment
        
    # def make_payment(self,country,method):
    #     self.payment = Payment(country,method,"Pending")
    
    # def create_order(self):
    #     new_order = Order("pending",self.cart.course,self.cart.total_net_price,new_payment)
    #     self.add_order(new_order)
    #     self.clear_cart()
    #     return True
    
    # def clear_cart(self):
    #     self.cart.course = []

    # def finish_payment(self,id):
    #     order = self.get_order_by_id(id)
    #     order.status = "success"
    #     self.add_to_student_course(order)
    #     return True
    
    # def refund_order(self,id):
    #     order = self.get_order_by_id(id)
    #     order.status = "refunded"
    #     self.return_course_to_cart(id)
    #     return True
    
    # def cancel_order(self,id):
    #     order = self.get_order_by_id(id)
    #     order.status = "cancelled"
    #     self.return_course_to_cart(id)
    #     return True
    
    # def add_to_student_course(self,order):
    #     for course in order.course:
    #         self.student_course.add_course_to_StudentCourse(course)
    #     return True

    # def return_course_to_cart(self,id):
    #     order = self.get_order_by_id(id)
    #     for course in order.course:
    #         self.cart.course.append(course)
        
    def get_order_by_id(self,id):
        for order in self.__orders:
            if order.id == id:
                return order
            
    def add_order(self, order):
        self.orders.append(order)
        return self.orders

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
