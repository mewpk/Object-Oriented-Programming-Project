class Account():
    def __init__(self,id,name,username,password,language ,email,role,about,active = True):
        self._id = id
        self._name = name
        self._username = username
        self._password = password
        self._language = language
        self._email = email
        self._role = role
        self._about = about
        self._active = active

    @property
    def id(self) :
            return self._id

class Student(Account):
    def __init__(self,id,name,username,password,language,email,role,about,review  ,active= True ):
        super().__init__(id,name,username,password,language,email,role,about,active)
        self.__review = review
        self.__orders  = []
    @property
    def review(self):
        return self.__review
    @property
    def orders(self) :
        return self.__orders
    @review.setter
    def review(self,review):
        self.__review = review
        return self.__review
    @orders.setter
    def orders(self,orders):
        self.__orders = orders
        return self.__orders
    def add_order(self,student_id, order):
        user = self.get_user(student_id)
        if user :
            user.orders.append(order)
            return order
        return False
    
    def view_orders(self , student_id) :
        user  = self.get_user(student_id)
        return user.orders

    def view_refunds(self,student_id) :
        orders = self.view_orders(student_id)
        list_refunds = []
        for order in orders :
            if order.status == "refunded" :
                list_refunds.append(order)
        return list_refunds
   
class Instructor(Account):
    def __init__(self,id,name,username,password,language,email,role,about,description,active= True ):
        super().__init__(id,name,username,password,language,email,role,about,active)
        self.__description = description
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self,description):
        self.__description = description
        return self.__description
  
class Admin(Account):
    def __init__(self,id,name,username,password,language,email,role,about,active= True ):
        super().__init__(id,name,username,password,language,email,role,about,active)
