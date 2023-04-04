class CatagoriesCollection():
    def __init__(self) -> None:
        self.__catagories = []
    @property
    def catagories(self):
        return self.__catagories
    @catagories.setter
    def set_catagories(self, catagories):
        self.__catagories = catagories
        return self.__catagories
        