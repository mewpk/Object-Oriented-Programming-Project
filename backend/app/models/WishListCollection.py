from .Course import Course
class WishListCollection():
    def __init__(self):
        self.__wishlist = []

    def get_wishlist(self):
        return self.__wishlist
    
    def add_to_wishlist(self,course : Course) -> bool:
        if course not in self.__wishlist:
            self.__wishlist.append(course)
            return True
        return False

    def remove_from_wishlist(self,course : Course) -> bool:
        if course  in self.__wishlist:
            self.__wishlist.remove(course)
        return False

