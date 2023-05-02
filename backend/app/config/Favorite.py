class FavoriteCollection():
    def __init__(self):
        self.__favorite = []
    @property
    def favorite(self):
        return self.__favorite