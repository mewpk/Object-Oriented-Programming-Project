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
    
    def get_users(self):
        return self.__users
    def get_user(self,username):
        for user in self.__users :
            if user.username == username :
                return user
    def add_user(self,new_user):
        self.users.append(new_user)
        return new_user

    def hash_password(self,new_user):
        hash_result = hash(new_user.password)
        new_user.password = hash_result
        return new_user
    
    def verify_username(self,username):
        for user in self.users:
            if user.username == username:
                return False
        return True
    
    def verify_login(self,user_data):
        for user in self.users:
            if user.username == user_data["username"]: 
                if user.password == hash(user_data["password"]):
                    return user
        return False
    

    def get_unverified_instructors(self):
        unverified_instructors = []
        for user in self.users:
            if user.role == "Instructor":
                if user.verify == False:
                    unverified_instructors.append(user)
                    return unverified_instructors
            
    def verify_instructors(self,username):
            user =  self.get_user(username)
            print(str(user))
            if user.role == "Instructor":
                if user.verify == False:
                    user.verify = True
                    return True
                return False
            
    def edit_profile(self,username,name,language,email,about):
        user = self.get_user(username)
        user.name = name
        user.language = language
        user.email = email
        user.about = about
        return True
                

        
   
    
