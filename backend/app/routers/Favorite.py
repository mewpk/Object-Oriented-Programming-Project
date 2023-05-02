from fastapi import APIRouter, Body

from ..config.database import course_collection,user_collection


router = APIRouter()

@router.post("/favorite/")
async def get_favorite(data: dict = Body(...)):
    student = user_collection.get_user(data.get("username"))
    return  student.favorite

@router.post("/check_course_in_favorite/")
async def check_course_in_favorite(data: dict = Body(...)):
    try:
        student = user_collection.get_user(data.get("username"))
        favorite = student.favorite
        for course in course_collection.courses:
            if course.id == data.get("course_id"):
                if favorite.check_course_in_favorite(course.id) == True:
                    return {"message": "check_course_in_favorite" , "status": True , "Course": course.id}
                else: 
                    return {"message": "check_course_in_favorite" ,"status": False , "Course": course.id}
        return "error"
    except:
        return "please try again"


@router.post("/add_to_favorite/")
async def add_to_favorite(data: dict = Body(...)):
    try:
        student = user_collection.get_user(data.get("username"))
        favorite = student.favorite
        for course in course_collection.courses:
            if course.id == data.get("course_id"):
                if favorite.check_course_in_favorite(course.id) == True:
                    student.favorite.remove_from_favorite(course)
                    return {"message": "add_to_favorite"  , "status": True , "Course": course.id}
                else: 
                    favorite.add_to_favorite(course)
                    return {"message": "add_to_favorite","status": False , "Course": course.id}
        return "error"
    except:
        return "please try again"
