class CourseCollection():
    def __init__(self) -> None:
        self.__courses = []

    @property
    def get_courses(self)->list:
        return self.__courses