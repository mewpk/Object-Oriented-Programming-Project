class CartCollection() :
    def __init__(self) -> None:
        self.__cart = []

    @property
    def cart(self) :
        return self.__cart
    
    def get_cart(self):
        return self.__cart
