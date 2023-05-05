# from ..models.Course import Course
from ..models.CourseChapter import CourseChapter
from datetime import datetime
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
            
    def edit_course(self,course_id,name,short_description,language,purpose,chapters,requiremen,description,target,price,info,categories): 
        course = self.get_course(course_id)
        course.name = name
        course.short_description = short_description
        course.language = language
        course.purpose = purpose
        for chapter in chapters:
            self.edit_chapters(course,chapter)
        course.requiremen = requiremen
        course.description = description
        course.target = target
        course.price = price
        course.info = info
        course.categories = categories
        return course

    def edit_chapters(self,course,new_chapter):
        for chapter in course.chapters:
            chapter.name = new_chapter.name
            chapter.video = new_chapter.video

    def delete_course(self,course):
        self.courses.remove(course)

    def expire_promotion(self):
        for course in self.courses:
            if course.promotion.end_date < datetime.now():
                course.promotion.percent = 0
                course.promotion.start_date = datetime.strptime('1/1/2000','%d/%m/%Y')
                course.promotion.end_date = datetime.strptime('1/1/2500','%d/%m/%Y')

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
    def add_chapter(self,course_id,name,video):
        course = self.get_course(course_id)
        id = len(course.chapters)+1
        new_chapter = CourseChapter(id,0,name,video)
        course.chapters.append(new_chapter)
        
    def edit_course(self,id,name,short_description,language,purpose,requirement,description,target,info,categories):
        course = self.get_course(id)
        course.name = name
        course.short_description = short_description
        course.language = language
        course.purpose = purpose
        course.requirement = requirement
        course.description = description
        course.target = target
        course.info = info
        course.categories = categories
        return course
