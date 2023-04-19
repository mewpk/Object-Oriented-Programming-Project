from fastapi import APIRouter, Body

from ..config.database import review_collection
from ..models.Review import Review


router = APIRouter()

@router.get("/review")
async def get_review():
    return  review_collection.get_reviews()

@router.post("/review/")
async def create_review(review_data: dict = Body(...)):
    new_review = Review(review_data["username"],review_data["rating"],review_data["course_id"],review_data["description"])
    data = review_collection.add_review(new_review)
    if data:
        return {"message": "review successfully", "review": data}
    else:
        return {"message": "Failed to review"}


