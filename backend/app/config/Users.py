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
    def get_user(self,student_id):
        for user in self.__users :
            if user.id == int(student_id) :
                return user
    def add_user(self,new_user):
        self.users.append(new_user)
        return new_user
    
        