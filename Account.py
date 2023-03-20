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

# create 4 instances of Student
student1 = Student(
    id=123,
    name="John Doe",
    username="johndoe",
    password="mypassword",
    language="English",
    email="johndoe@example.com",
    role="Student",
    about="I am a student.",
    review="Great student!",
    active=True
)

student2 = Student(
    id=124,
    name="Jane Smith",
    username="janesmith",
    password="mypassword",
    language="Spanish",
    email="janesmith@example.com",
    role="Student",
    about="I am also a student.",
    review="Excellent student!",
    active=True
)

student3 = Student(
    id=125,
    name="Bob Johnson",
    username="bobjohnson",
    password="mypassword",
    language="French",
    email="bobjohnson@example.com",
    role="Student",
    about="I am a student too.",
    review="Very dedicated student!",
    active=True
)

student4 = Student(
    id=126,
    name="Sarah Lee",
    username="sarahlee",
    password="mypassword",
    language="German",
    email="sarahlee@example.com",
    role="Student",
    about="I am also a student.",
    review="Highly recommended student!",
    active=True
)
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

# create 4 instances of Instructor
instrutor1 = Instructor(
    id=127,
    name="John Doe",
    username="johndoe",
    password="mypassword",
    language="English",
    email="johndoe@example.com",
    role="instrutor",
    about="I am a instrutor.",
    description="Great instrutor!",
    active=True
)

instrutor2 = Instructor(
    id=128,
    name="Jane Smith",
    username="janesmith",
    password="mypassword",
    language="Spanish",
    email="janesmith@example.com",
    role="instrutor",
    about="I am also a instrutor.",
    description="Excellent instrutor!",
    active=True
)

instrutor3 = Instructor(
    id=129,
    name="Bob Johnson",
    username="bobjohnson",
    password="mypassword",
    language="French",
    email="bobjohnson@example.com",
    role="instrutor",
    about="I am a instrutor too.",
    description="Very dedicated instrutor!",
    active=True
)

instrutor4 = Instructor(
    id=130,
    name="Sarah Lee",
    username="sarahlee",
    password="mypassword",
    language="German",
    email="sarahlee@example.com",
    role="instrutor",
    about="I am also a instrutor.",
    description="Highly recommended instrutor!",
    active=True
)
class Admin(Account):
    def __init__(self,id,name,username,password,language,email,role,about,active= True ):
        super().__init__(id,name,username,password,language,email,role,about,active)
    def verify_instructor(Account) : 
        pass
    def create_coupon(id,passcode,start_date,end_date,type) : 
        pass
    def create_user(Account ) : 
        pass
admin1 = Admin(
    id=131,
    name="Sarah Lee",
    username="sarahlee",
    password="mypassword",
    language="German",
    email="sarahlee@example.com",
    role="admin",
    about="I am also a instrutor.",
    active=True
)