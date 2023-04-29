from fastapi import APIRouter, Body

from ..config.database import course_collection,user_collection

router = APIRouter()

@router.get("/wishlist")
async def get_wishlist(username : str):
    student = user_collection.get_user(username)
    return  student.get_wishlist()

@router.post("/add_to_wishlist/")
async def add_to_wishlist(data: dict = Body(...)):
    try:
        student = user_collection.get_user(data.get("username"))
        for course in course_collection.courses:
            if course.id == data.get("course_id"):
                if student.check_course_in_wishlist(course.id) == True:
                    student.remove_from_wishlist(course)
                    return "remove success"
                else: 
                    student.add_to_wishlist(course)
                    return "add success"
        return "error"
    except:
        return "please try again"
