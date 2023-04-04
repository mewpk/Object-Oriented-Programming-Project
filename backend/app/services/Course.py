# from ..models.Course import Course
from ..config.Course import CourseCollection

Course_Collection = CourseCollection()
class CourseService():
    def add_course(self,course):
        course_list = Course_Collection.get_courses
        return course_list.append(course)
    