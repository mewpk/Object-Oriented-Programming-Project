class Review():
    def __init__(self,by,rating,course_id,description,id):
        self.__id = id
        self.__by = by
        self.__rating = rating
        self.__course_id = course_id
        self.__description = description
    @property
    def id(self):
        return self.__id
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
    @property
    def get_course_id(self):
        return self.__course_id
 