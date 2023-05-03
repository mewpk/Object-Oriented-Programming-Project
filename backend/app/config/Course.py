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

    # def edit_course(self,id,name,short_description,language,purpose,requirement,description,target,info):
    #     course = self.get_course(id)
    #     course.name = name
    #     course.short_description = short_description
    #     course.language = language
    #     course.purpose = purpose
    #     course.requirement = requirement
    #     course.description = description
    #     course.target = target
    #     course.info = info
    #     return course