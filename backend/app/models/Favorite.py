class Favorite:
    def __init__(self):
        self.__favorite = []
    @property
    def favorite(self):
        return self.__favorite
    
    def add_to_favorite(self,course):
        self.favorite.append(course)
        return "successfully"
    
    def remove_from_favorite(self,course):
        self.favorite.remove(course)
        return "success"

    def check_course_in_favorite(self,course_id):
        for course in self.favorite:
            if course.id == course_id:
                print(course.id)
                return True
        print(course_id)
        return False