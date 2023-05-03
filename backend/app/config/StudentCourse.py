from ..models.Course import StudentCourse
from datetime import datetime

class StudentCourseCollection():
    def __init__(self):
        self.__courses = []
    @property
    def courses(self):
        return self.__courses
    
    def get_studentcourse(self):
        return self.__courses
    
    def add_course_to_StudentCourse(self,courses):
        for course in courses:
            print(len(self.courses))
            student_course = StudentCourse(len(self.courses)+1,course.id,course.name,course.short_description,datetime.strptime(course.date, '%d/%m/%Y'),course.language,course.purpose,course.chapters,course.requirement,course.description,course.target,course.price,course.info,course.categories,course.instructor)
            self.courses.append(student_course)
