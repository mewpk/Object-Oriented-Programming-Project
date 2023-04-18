class StudentCourse():
    def __init__(self,all_progress,student_id,course_id):
        self.__all_progress = all_progress
        self.__student_id = student_id
        self.__course_id = course_id
    @property
    def all_progress(self):
        return self.__all_progress
    @property
    def student_id(self):
        return self.__student_id
    @property
    def course_id(self):
        return self.__course_id