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
            self.courses.append(course)
            return course
        except  :
            return False

    def add_chapter(self,chapter):
        # self.courses.chapter
        pass

    def get_course(self,course_id):
        for course in self.courses:
            if course.id == course_id:
                return course
        

    def search_by_course(self,course_name):
        result = []
        for course in self.courses:
            if course_name == course.name:
                result.append(course)
        result.sort(key=lambda c: c.average_rating)
        return result
        
    def search_by_instructor(self,instructor_name):
        result = []
        for course in self.courses :
            if course.instructor == instructor_name:
                result.append(course)
        result.sort(key=lambda c: c.average_rating)
        return result
    
    def search_by_category(self,category_name):
        result = []
        for course in self.courses :
            for category in course.categories:
                if category == category_name:
                    result.append(course)
        result.sort(key=lambda c: c.average_rating)
        return result
    
    def sort_by_rating(self):
        result = sorted(self.courses, key=lambda k: k.average_rating , reverse=True)
        return result

                