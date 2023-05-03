class ReviewCollection() :
    def __init__(self) -> None :
        self.__review = []

    @property
    def review(self) :
        return self.__review
    
    def get_reviews(self):
        return self.__review
    
    def add_review(self,review):
        self.review.append(review)
        return "success"
    
    def check_review_by_username(self,username,course_id):
        for review in self.review:
            if review.username == username:
                print("check username")
                if review.course_id == course_id:
                    print("check id")
                    return False
        return True