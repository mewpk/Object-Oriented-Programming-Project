from fastapi import APIRouter, Body

from ..config.Course import CourseCollection
from ..models.Course import Course


router = APIRouter()

@router.get("/course")
async def get_course():
    return  CourseCollection.courses()

@router.post("/course/")
async def create_course(course_data: dict = Body(...)):
    course_data = Course(course_data["id"],course_data["name"],course_data["short_description"],course_data["date"],course_ddlanguage,purpose,chapter,requirement,description,target,price,promotion,info,categories,instructor)
    new_course = CourseCollection().add_course(course_data)
    if new_course:
        return {"message": "Course created successfully", "user": new_course}
    else:
        return {"message": "Failed to create course"}
