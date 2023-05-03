from fastapi import APIRouter, Body

from ..config.database import studentcourse_collection,user_collection
# from ..models.StudentCourse import StudentCourse


router = APIRouter()

@router.post("/studentcourse")
async def get_studentcourse(data: dict = Body(...)):
    student = user_collection.get_user(data.get("username"))
    return  student.student_course

# @router.post("/studentcourse")
# async def add_to_studentcourse(data: dict = Body(...)):
#     user = user_collection.get_user(data.get("username"))
#     user.add_to_student_course




