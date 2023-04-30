from fastapi import APIRouter, Body

from ..config.database import review_collection
from ..models.Review import Review


router = APIRouter()

@router.get("/review")
async def get_review():
    return  review_collection.get_reviews()

@router.post("/review/")
async def create_review(review_data: dict = Body(...)):
    try:
        new_review = Review(review_data.get("username"),review_data.get("rating"),review_data.get("course_id"),review_data.get("description"))
        data = review_collection.add_review(new_review)
        if data:
            return {"message": "review successfully", "review": data}
        else:
            return {"message": "Failed to review"}
    except:
        return "please try again"


