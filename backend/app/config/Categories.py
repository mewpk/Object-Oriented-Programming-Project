class CatagoriesCollection():
    def __init__(self) -> None:
        self.__catagories = []

    @property
    def get_catagories(self):
        return self.__catagories