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