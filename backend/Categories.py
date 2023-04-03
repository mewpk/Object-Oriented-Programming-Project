import weakref
class Categories():
    instances = []
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
        self.all_instances()
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
        return self.__name
    
    def request_catagories() : 
        pass
    def search_categories(keyword) : 
        pass
    def all_instances(self):
        self.__class__.instances.append(weakref.proxy(self))
    def __str__(self) -> str:
        return self.__name

# create instances categories
programming_language = Categories(id=1,name="Programming Language")
development = Categories(id=2,name="development")
web_development = Categories(id = 3 , name ="Web Development")