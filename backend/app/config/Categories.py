class CategoriesCollection():
    def __init__(self) -> None:
        self.__categories = []
    @property
    def categories(self):
        return self.__categories
    @categories.setter
    def set_categories(self, categories):
        self.__categories = categories
        return self.__categories
    
    def add_categories(self,categories):
        try :
            self.__categories.append(categories)
            return categories
        except  :
            return False
