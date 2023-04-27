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
    def password(self) :
        return self._password
    @property
    def role(self) :
        return self._role
    @password.setter
    def password(self,password) :
        self._password = password
        return self._password
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
    
    def add_order(self,username, order):
        user = user_collection.get_user(username)
        if user :
            user.orders.append(order)
            return order
        return False
    
    def view_orders(self , username) :
        user  = user_collection.get_user(username)
        return user.orders

    def view_refunds(self,username) :
        orders = self.view_orders(username)
        list_refunds = []
        for order in orders :
            if order.status == "refunded" :
                list_refunds.append(order)
        return list_refunds

    def add_to_cart(self,course_id):
        self.cart.add_to_cart(course_id)

    def get_wishlist(self):
        return self.wishlist
    
    def add_to_wishlist(self,course_id):
        self.wishlist.append(course_id)
        return "success"

   
class Instructor(Account):
    def __init__(self,name,username,password,language,email,role,about = "",description = "",active= True ):
        super().__init__(name,username,password,language,email,role,about,active)
        self.__description = description
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self,description):
        self.__description = description
        return self.__description
  
class Admin(Account):
    def __init__(self,name,username,password,language,email,role,about = "",active= True ):
        super().__init__(name,username,password,language,email,role,about,active)
