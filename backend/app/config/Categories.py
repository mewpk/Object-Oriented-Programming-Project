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
    
    def verify_category(self,name):
        for category in self.__categories:
            if category.name == name:
                return False
        return True
    
    def add_category(self,category):
        if self.verify_category(category) == True:
            try :
                self.__categories.append(category)
                return category
            except  :
                return False
        else:
            return False        