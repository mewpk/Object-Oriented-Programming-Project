class CourseViewChapter():
    def __init__(self,progress,student_id,course_id):
        self.__progress = progress
        self.__student_id = student_id
        self.__course_id = course_id
    @property
    def progress(self):
        return self.__progress
    @property
    def student_id(self):
        return self.__student_id
    @property
    def course_id(self):
        return self.__course_id
    

chp = CourseViewChapter (
    progress = [100,50,0,0],
    student_id = "1111",
    course_id = "11111111",
)

