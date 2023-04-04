from ..models.Course import Course
from ..config.Course import CourseCollection
class CourseService():
    Course_Collection = CourseCollection()
    def add_course(self,course):
        self.Course = Course_Collection.get_course(course)
