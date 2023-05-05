class UsersCollection :
    def __init__(self) -> None :
        self.__users = []
    @property
    def users(self):
        return self.__users
    
    @users.setter
    def set_users(self, users):
        self.__users = users
        return self.__users

    def get_user(self,username):
        for user in self.__users :
            if user.username == username :
                return user
            
    def add_user(self,new_user):
        self.users.append(new_user)
        return new_user
    
    def delete_user(self,user):
        self.users.remove(user)

    def hash_password(self,password):
        return hash(password)
    
    def verify_username(self,username):
        for user in self.users:
            if user.username == username:
                return False
        return True
    
    def verify_login(self,user_data):
        for user in self.users:
            if user.username == user_data.get("username"): 
                if user.password == self.hash_password(user_data.get("password")) :
                    return user
        return False

    def get_instructors(self):
        instructor = []
        for user in self.users:
            if user.role == "Instructor":
                instructor.append(user)
        return instructor
            
    def get_unverified_instructors(self):
        unverified_instructors = []
        for user in self.get_instructors():
            if user.verify == False:
                unverified_instructors.append(user)
        return unverified_instructors
            
    def verify_instructor(self,username):
            user =  self.get_user(username)
            if user.role == "Instructor":
                if user.verify == False:
                    user.verify = True
                    return True
                return False
    
    def unverify_instructor(self,username):
            user =  self.get_user(username)
            if user.role == "Instructor":
                if user.verify == True:
                    user.verify = False
                    return True
                return False
            
    def edit_profile(self,username,name,language,email,about):
        user = self.get_user(username)
        user.name = name
        user.language = language
        user.email = email
        user.about = about
        return user
                

   
