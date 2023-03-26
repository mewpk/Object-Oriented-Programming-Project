import weakref
class Review():
    instances = []
    def __init__(self,by,rating,course_id,description):
        self.__by = by
        self.__rating = rating
        self.__course_id = course_id
        self.__description = description
        self.all_instances()
    @property
    def by(self):
        return self.__by
    @property
    def rating(self):
        return self.__rating
    @property
    def course_id(self):
        return self.__course_id
    @property
    def description(self):
        return self.__description
    def all_instances(self):
        self.__class__.instances.append(weakref.proxy(self))
    def get_course_id(self):
        return self.__course_id
    def collect_all_review(id):
        pass
    def add_review_to_course():
        pass
    def __str__(self) -> str:
        return str([{ "by" : self.__by , "rating" : self.__rating , "course_id"  : self.__course_id, "description" : self.__description  }])

review1 = Review(
    by = "ppp" ,
    rating = 5,
    course_id = "11111111",
    description =  "godd!!!"
)

review2 = Review(
    by = "mw",    
    rating = 4.5,  
    course_id = "11111111",
    description =  "love it !"
)

review3 = Review(
    by = "pkpk",
    rating = 4.5,
    course_id = "11111112",
    description =  "saranghaeee"
)