class WishListCollection():
    def __init__(self) -> None:
        self.__wishlist = []
    @property
    def wishlist(self) -> list:
        return self.__wishlist