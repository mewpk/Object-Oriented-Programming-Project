from fastapi import APIRouter, Body

from ..config.database import course_collection
from ..models.Course import Course


router = APIRouter()

@router.get("/course")
async def get_course():
    return  course_collection.get_courses()

@router.post("/course/")
async def create_course(course_data: dict = Body(...)):
    new_course = Course(course_data["id"],course_data["name"],course_data["short_description"],course_data["date"],course_data["language"]
                         ,course_data["purpose"],course_data["chapter"],course_data["requirement"],course_data["description"],course_data["target"]
                         ,course_data["price"],course_data["promotion"],course_data["info"],course_data["categories"],course_data["instructor"])
    data = course_collection.add_course(new_course)
    if new_course and data:
        return {"message": "Course created successfully", "course": data}
    else:
        return {"message": "Failed to create course"}
    
@router.get("/course/search_bytructor/{instructor_name}")
async def search_by_instructor(instructor_name):
    return course_collection.search_by_instructor(instructor_name)

@router.get("/course/search_by_course/{course_name}")
async def search_by_course(course_name):    
    return course_collection.search_by_course(course_name)

@router.get("/course/search_by_category/{category}")
async def search_by_category(category_name):    
    return course_collection.search_by_category(category_name)


