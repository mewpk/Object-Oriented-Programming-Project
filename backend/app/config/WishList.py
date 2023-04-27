class WishListCollection():
    def __init__(self) -> None:
        self.__wishlist = []
    @property
    def wishlist(self) -> list:
        return self.__wishlist
    
    def get_wishlist(self):
        return self.__wishlist
    
    def add_to_wishlist(self,course):
        self.wishlist.append(course)
        return "success"