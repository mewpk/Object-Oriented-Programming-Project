from ..config.Users import UsersCollection

class UsersService :
    def get_users():
        try: 
            return str(UsersCollection.users)
        except :
            return False
    def get_user_by_id(self,user_id : str ):
        for user in UsersCollection.users :
            if user.id == user_id :
                return user
        return None
    def add_user(self , user):
        try :
            UsersCollection.users.append(user)
            return user
        except  :
            return False
