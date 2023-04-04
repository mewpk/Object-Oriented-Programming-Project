class CatagoriesCollection():
    def __init__(self) -> None:
        self.__categories = []

    @property
    def get_catagories(self):
        return self.__categories