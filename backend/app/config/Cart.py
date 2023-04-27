class CartCollection() :
    def __init__(self) -> None:
        self.__cart = []

    @property
    def cart(self) :
        return self.__cart
    
    def get_cart(self):
        return self.__cart
    
    def add_to_cart(self, course):
        self.cart.append(course)
        return "success"
    
    def remove_from_cart(self, course):
        self.cart.remove(course)
        return "success"