from fastapi import APIRouter, Body

from ..config.database import studentcourse_collection
# from ..models.StudentCourse import StudentCourse


router = APIRouter()

@router.get("/studentcourse")
async def get_studentcourse():
    return  studentcourse_collection.get_studentcourse()

