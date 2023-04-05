class OrderCollection():
    def __init__(self) -> None :
        self.__order = []
    @property
    def order(self)->list:
        return self.__order