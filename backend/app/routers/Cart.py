from fastapi import APIRouter, Body

from ..config.database import cart_collection,course_collection,user_collection
from ..models.Course import Course
from ..models.Users import Student

router = APIRouter()

@router.post("/cart/")
async def get_cart(username : str):
    for user in user_collection.users:
        if user.username == username:
            student = user
            return student.cart
    

@router.post("/add_cart/")
async def add_cart(course_id: int,username:str):
    for user in user_collection.users:
        if user.username == username:
            user.add_to_cart(course_id)
            return "success"
    return "Failed to add"
            

    
