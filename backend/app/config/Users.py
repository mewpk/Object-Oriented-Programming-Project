

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
        