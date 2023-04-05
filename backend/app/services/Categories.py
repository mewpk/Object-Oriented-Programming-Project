
from ..config.database import categories_collection
class CategoriesService():
    def get_categories():
        return categories_collection.catagories
    
    def add_categories(category):
       try :
           categories_collection.catagories.append(category)
           return category
       except :
           return False                    
