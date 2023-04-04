# from ..models.Course import Course
from ..config.database import CourseCollection

Course_Collection = CourseCollection()
class CourseService():
    def get_course():
        return Course_Collection.courses
    def add_course(self,course):
        try :
            course_list = Course_Collection.courses 
            course_list.append(course)
            return course
        except  :
            return False
        