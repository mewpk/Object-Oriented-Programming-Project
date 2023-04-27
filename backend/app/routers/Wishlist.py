from fastapi import APIRouter, Body

from ..config.database import wishlist_collection,course_collection
from ..models.WishList import Wishlist

router = APIRouter()

@router.get("/wishlist")
async def get_category():
    return  wishlist_collection.get_wishlist()

@router.post("/add_to_wishlist/")
async def add_to_wishlist(course_id : str):
    for course in course_collection.courses:
        if course.id == course_id:
            wishlist_collection.add_to_wishlist(course)
            return "success"
        else: return "error"