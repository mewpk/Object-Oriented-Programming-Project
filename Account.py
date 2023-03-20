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

class Student(Account):
    def __init__(self,id,name,username,password,language,email,role,about,review,active= True ):
        super().__init__(id,name,username,password,language,email,role,about,active)
        self.__review = review
    def add_payment_method(self,method):
        pass
    def request_history(self,status) :
        pass
    def create_user(self,Account):
        pass

class Instructor(Account):
    def __init__(self,id,name,username,password,language,email,role,about,description,active= True ):
        super().__init__(id,name,username,password,language,email,role,about,active)
        self.__description = description
    def add_course(self,Course):
        pass
    def edit_course(Course) : 
        pass
    def create_coupon(id,passcode,start_date,end_date,type) : 
        pass
    def edit_profile(Account)  : 
        pass
    def create_user(Account ) : 
        pass
    def search_instructor(keyword) : 
        pass

class Admin(Account):
    def __init__(self,id,name,username,password,language,email,role,about,verify_course,active= True ):
        super().__init__(id,name,username,password,language,email,role,about,active)
        self.__verify_course = verify_course
    def verify_instructor(Account) : 
        pass
    def create_coupon(id,passcode,start_date,end_date,type) : 
        pass
    def create_user(Account ) : 
        pass
