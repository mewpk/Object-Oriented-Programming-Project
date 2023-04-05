from fastapi import APIRouter, Body

from ..services.Course import CourseService


router = APIRouter()

@router.get("/course")
async def get_course():
    return  CourseService.get_course()

@router.post("/course/")
async def create_course(course_data: dict = Body(...)):
    new_course = CourseService().add_course(course_data)
    if new_course:
        return {"message": "Course created successfully", "user": new_course}
    else:
        return {"message": "Failed to create course"}
