class StudentCourseCollection():
    def __init__(self):
        self.__courses = []
    @property
    def courses(self):
        return self.__courses
    
    def get_studentcourse(self):
        return self.__courses
    
    def add_course_to_StudentCourse(self, course):
        return self.courses.append(course)