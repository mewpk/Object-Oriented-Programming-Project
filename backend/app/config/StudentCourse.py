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

    def add_course_to_StudentCourse(self,courses):
        for course in courses:
            print(len(self.courses))
            student_course = StudentCourse(len(self.courses)+1,course.id,course.name,course.short_description,datetime.strptime(course.date, '%d/%m/%Y'),course.language,course.purpose,course.chapters,course.requirement,course.description,course.target,course.price,course.info,course.categories,course.instructor)
            self.courses.append(student_course)

    def update_course(self,id):
        course = self.get_course(id)
        updated_course = CourseCollection.get_course(id)
        course.name = updated_course.name
        course.short_description = updated_course.short_description
        course.language = updated_course.language
        course.purpose = updated_course.purpose
        course.requirement = updated_course.requirement
        course.description = updated_course.description
        course.target = updated_course.target
        course.info = updated_course.info
        course.categories = updated_course.categories
        return course
