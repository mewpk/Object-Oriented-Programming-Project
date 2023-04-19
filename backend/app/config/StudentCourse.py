class StudentCourseCollection():
    def __init__(self):
        self.__StudentCourse_list = []
    @property
    def courses(self):
        return self.__StudentCourse_list
    
    def get_studentcourse(self):
        return self.__StudentCourse_list
    
    def add_course_to_StudentCourse(self, course):
        return self.courses.append(course)