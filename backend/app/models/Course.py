import random
from datetime import datetime, date
from .CourseChapter import CourseChapter
from .Promotion import Promotion
image = [
  {
    "src": "https://fireship.io/courses/react-next-firebase/img/featured.png"
  },
  {
    "src": "https://fireship.io/courses/js/img/featured.webp"
  },
  {
    "src": "https://fireship.io/courses/supabase/img/featured.webp"
  },
  {
    "src": "https://fireship.io/courses/flutter-firebase/img/featured.webp"
  } ,
  {
      "src" : "https://fireship.io/courses/nextjs/img/featured.webp"
  },
  {
      "src" :"https://fireship.io/courses/dart/img/featured.webp"
  },
  {
      "src" : "https://fireship.io/courses/git/img/featured.webp"
  },
  {
      "src" : "https://fireship.io/courses/firebase-security/img/featured.webp"
  },
  {
      "src" : "https://fireship.io/courses/angular/img/featured.webp"
  },    
  {
      "src" : "https://fireship.io/courses/firestore-data-modeling/img/featured.webp"
  },
]
class Course():
    def __init__(self,id,name,short_description,date,language,purpose,chapters,requirement,description,target,price,info,categories,instructor):
        self._id = id
        self._name = name
        self._short_description = short_description
        self._date = date.strftime("%d/%m/%Y")
        self._language = language
        self._purpose = purpose
        self._chapters = chapters
        self._review = []
        self._average_rating = 0
        self._requirement = requirement
        self._description = description
        self._target = target
        self._price = price
        self._promotion = Promotion(0,'1/1/2000','1/1/2500',price)
        self._info = info
        self._categories = categories
        self._instructor = instructor
        self._image = image[random.randint(0,len(image)-1)].get("src")
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def short_description(self):
        return self._short_description
    @property
    def date(self):
        return self._date
    @property
    def language(self):
        return self._language
    @property
    def purpose(self):
        return self._purpose
    @property
    def chapters(self):
        return self._chapters
    @property
    def review(self):
        return self._review
    @property
    def requirement(self):
        return self._requirement
    @property
    def description(self):
        return self._description
    @property
    def target(self):
        return self._target
    @property
    def price(self):
        return self._price
    @property
    def promotion(self):
        return self._promotion
    @property
    def info(self):
        return self._info
    @property
    def categories(self):
        return self._categories
    @property
    def instructor(self):
        return self._instructor
    @property
    def image(self):
        return self._image
    @property
    def average_rating(self):
        return self._average_rating
    @id.setter
    def id(self,id):
        self._id = id
        return self._id
    @name.setter
    def name(self,name):
        self._name = name
        return self._name
    @short_description.setter
    def short_description(self,short_description):
        self._short_description = short_description
        return self._short_description
    @language.setter
    def language(self,language):
        self._language = language
        return self._language
    @purpose.setter
    def purpose(self,purpose):
        self._purpose = purpose
        return self.purpose
    @chapters.setter
    def chapers(self,chapters):
        self._chapters = chapters
        return self._chapters
    @requirement.setter
    def requirement(self,requirement):
        self._requirement = requirement
        return self._requirement
    @description.setter
    def description(self,description):
        self._description = description
        return self._description
    @target.setter
    def target(self,target):
        self._target = target
        return self._target
    @price.setter
    def price(self,price):
        self._price = price
        return self._price
    @info.setter
    def info(self,info):
        self._info = info
        return self._info
    @categories.setter
    def categories(self,categories):
        self._categories = categories
        return self._categories
    @instructor.setter
    def instructor(self,instructor):
        self._instructor = instructor
        return self._instructor
    @image.setter
    def image(self,image):
        self._image = image
        return self._image
    @average_rating.setter
    def average_rating(self,average_rating):
        self._average_rating = average_rating
        return self._average_rating

    def delete_chapter(self,chapter):
        self.chapers.remove(chapter)

    def add_chapter(self,name,video):
        last_chapter = self.chapters[len(self.chapers)-1]
        new_chapter = CourseChapter(last_chapter.id+1,0,name,video)
        self.chapters.append(new_chapter)

    def get_chapter_by_id(self,chapter_id):
        for chapter in self.chapers:
            if chapter.id == chapter_id:
                return chapter

    def add_promotion(self,promotion):
        self.promotion.percent = promotion.percent
        self.promotion.start_date = promotion.start_date
        self.promotion.end_date = promotion.end_date
        
    def add_review(self,review):
        self.review.append(review)
        self.get_average_rating()
        
    def get_average_rating(self):
        total = 0
        for review in self.review:
            total += review.rating
        self.average_rating = total/len(self.review)


class StudentCourse(Course):
    def __init__(self,id,name,short_description,date,language,purpose,chapters,requirement,description,target,price,info,categories,instructor,all_progress=0):
        super().__init__(id,name,short_description,date,language,purpose,chapters,requirement,description,target,price,info,categories,instructor)
        self.__all_progress = all_progress
    @property
    def all_progress(self):
        return self.__all_progress
    @all_progress.setter
    def all_progress(self,all_progress):
        self.__all_progress = all_progress
        return self.__all_progress
    
    def calculate_progress(self):
        all_progress = 0
        for chapter in self.chapters:
            all_progress += chapter.progress
        self.all_progress = int(all_progress/len(self.chapters))
        return self.all_progress

