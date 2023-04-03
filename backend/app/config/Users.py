class UsersCollection :
    def __init__(self) -> None :
        self.__users = []
    @property
    def users(self) -> list:
        return self.__users