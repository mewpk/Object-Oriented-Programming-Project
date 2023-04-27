from fastapi import APIRouter, Body

from ..config.database import wishlist_collection,course_collection,user_collection
from ..models.WishList import Wishlist

router = APIRouter()

@router.get("/wishlist")
async def get_wishlist(username : str):
    student = user_collection.get_user(username)
    return  student.get_wishlist()

@router.post("/add_to_wishlist/")
async def add_to_wishlist(course_id : str , username :str):
    student = user_collection.get_user(username)
    for course in course_collection.courses:
        if course.id == course_id:
            student.add_to_wishlist(course)
            return "success"
    return "error"