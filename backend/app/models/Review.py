class Review():
    def __init__(self,username,rating,course_id,description):
        self.__username = username
        self.__rating = rating
        self.__course_id = course_id
        self.__description = description

    @property
    def username(self):
        return self.__username
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
 