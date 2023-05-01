from fastapi import APIRouter, Body

from ..config.database import studentcourse_collection,user_collection
# from ..models.StudentCourse import StudentCourse


router = APIRouter()

@router.get("/studentcourse")
async def get_studentcourse():
    return  studentcourse_collection.get_studentcourse()

# @router.post("/studentcourse")
# async def add_to_studentcourse(data: dict = Body(...)):
#     user = user_collection.get_user(data.get("username"))
#     user.add_to_student_course


