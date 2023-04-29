from .Cart import Cart
from ..config.database import user_collection


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
        self.__wishlist = []
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
    def wishlist(self) :
        return self.__wishlist

    @review.setter
    def review(self,review):
        self.__review = review
        return self.__review
    @orders.setter
    def orders(self,orders):
        self.__orders = orders
        return self.__orders
    
    def add_order(self, order):
        self.orders.append(order)
        return True

    def view_refunds(self) :
        # orders = self.view_orders(username)
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
        else: return False
        
    def get_wishlist(self):
        return self.wishlist
    
    def add_to_wishlist(self,course_id):
        self.wishlist.append(course_id)
        return "success"
    
    def check_course_in_wishlist(self,course_id):
        for course in self.wishlist:
            if course.id == course_id:
                print(course.id)
                return True
        print(course_id)
        return False
    
    def remove_from_wishlist(self,course_id):
        self.wishlist.remove(course_id)
        return "success"
    
    def view_total_price(self):
        return self.cart.total_price()

   
class Instructor(Account):
    def __init__(self,name,username,password,language,email,role,about,description,active= True,verify=False ):
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
