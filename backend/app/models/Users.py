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
    @property
    def review(self):
        return self.__review
    @review.setter
    def review(self,review):
        self.__review = review
        return self.__review
   
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
