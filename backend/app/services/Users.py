from ..config.database import user_collection

class UsersService :
    def get_users(self):
        return user_collection.users
    def get_user_by_id(self,user_id : str ):
        for user in user_collection.users :
            if user.id == user_id :
                return user
        return None
    def add_user(self , user):
        try :
            user_collection.users.append(user)
            return user
        except  :
            return False
