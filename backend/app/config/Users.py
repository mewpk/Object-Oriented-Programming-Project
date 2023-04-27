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
    
    def get_user(self,student_id):
        for user in self.__users :
            if user.id == int(student_id) :
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
    
    def add_to_wishlist(self,student_id,course):
        self.wishlist.append(course)
        return "success"
