class CourseViewChapterCollection():
    def __init__(self)->None :
        self.__chapter = []
    @property
    def chapter(self)->list:
        return self.__chapter