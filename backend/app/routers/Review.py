from fastapi import APIRouter, Body

from ..config.database import review_collection, course_collection, user_collection
from ..models.Review import Review


router = APIRouter()

@router.get("/review")
async def get_review():
    return  review_collection.get_reviews()

@router.post("/review/")
async def create_review(review_data: dict = Body(...)):
    try:
        course = course_collection.get_course(review_data.get("course_id"))
        student = user_collection.get_user(review_data.get("username"))
        # if course not in student.student_course():
        if review_data.get("rating") <= 5 and review_data.get("rating") >= 1 :
            if review_collection.check_review_by_username(review_data.get("username"),review_data.get("course_id"))==True:
                new_review = Review(review_data.get("username"),review_data.get("rating"),review_data.get("course_id"),review_data.get("description"))
                review_collection.add_review(new_review)
                course.add_review(new_review)
                student.add_review(new_review)
                return {"message": "review successfully", "review": new_review}
            else:
                return "fail"
            # else :
            #     return "fail to add review"
    except:
        return "please try again"


