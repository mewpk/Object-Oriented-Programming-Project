from ..models.Course import StudentCourse
from ..config.Course import CourseCollection
from datetime import datetime

class StudentCourseCollection():
    def __init__(self):
        self.__courses = []
    @property
    def courses(self):
        return self.__courses
    
    def get_studentcourse(self):
        return self.__courses
    
    def get_course(self,id):
        for course in self.courses:
            if course.id == id:
                return course

    def add_course_to_student_course(self,courses):
        for course in courses:
            student_course = StudentCourse(course.id,course.name,course.short_description,datetime.strptime(course.date, '%d/%m/%Y'),course.language,course.purpose,course.chapters,course.requirement,course.description,course.target,course.price,course.info,course.categories,course.instructor)
            self.courses.append(student_course)

    def check_course(self,course_id):
        for course in self.courses:
            if course.id == course_id:
                return False
        return True
    
    def remove_course(self,course_id):
        for course in self.courses:
            if course.id == course_id:
                self.courses.remove(course)

