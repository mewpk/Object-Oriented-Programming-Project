from ..models.Categories import Categories
from ..config.Categories import CatagoriesCollection

class CategoriesService(Categories):
    def add_category(self):
       return CatagoriesCollection.get_catagories().append(Categories)                          