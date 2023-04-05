from ..models.Course import Course
class CourseCollection():
    def __init__(self) -> None:
        self.__courses = []

    @property
    def courses(self)->list:
        return self.__courses
    @courses.setter
    def courses(self,courses):
        self.__courses = courses
        return self.__courses  
    
    def add_course(self,course):
        try :
            self.__courses.append(course)
            return course
        except  :
            return False

    def search_by_course(self,course_name):
        result = []
        for course in self.__courses:
            if course_name == course.name:
                result.append(course)
        return result
        
    def search_by_instructor(self,instructor_name):
        result = []
        for course in self.__courses :
            if course.instructor == instructor_name:
                result.append(course)
        return result
    
    def search_by_category(self,search_category):
        result = []
        for course in self.__courses :
            for category in course.category:
                if category == search_category:
                    result.append(course)
        return result
                