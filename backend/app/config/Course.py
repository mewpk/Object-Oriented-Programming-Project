class CourseCollection():
    def __init__(self) -> None:
        self.__courses = []

    @property
    def courses(self)->list:
        return self.__courses
    @courses.setter
    def courses(self,courses):
        self.__courses = courses
        return self.__courses