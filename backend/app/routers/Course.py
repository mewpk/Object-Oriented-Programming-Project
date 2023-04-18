from fastapi import APIRouter, Body

from ..config.database import course_collection
from ..models.Course import Course


router = APIRouter()
@router.get("/mockcourse")
async def mock_course():
    for i in range(50):
        course_data = {
            "id": f"course_{i}",
            "name": f"Course {i}",
            "short_description": f"This is a short description for Course {i}.",
            "date": "2023-04-19",
            "language": "English",
            "purpose": f"The purpose of Course {i} is to teach students about...",
            "chapter": f"Chapter {i}",
            "requirement": f"Requirement {i}",
            "description": f"This is the full description for Course {i}.",
            "target": f"The target audience for Course {i} is...",
            "price": 19.99,
            "promotion": False,
            "info": f"Info {i}",
            "categories": ["Category 1", "Category 2"],
            "instructor": "John Doe"
        }
        new_course = Course(
            course_data["id"],
            course_data["name"],
            course_data["short_description"],
            course_data["date"],
            course_data["language"],
            course_data["purpose"],
            course_data["chapter"],
            course_data["requirement"],
            course_data["description"],
            course_data["target"],
            course_data["price"],
            course_data["promotion"],
            course_data["info"],
            course_data["categories"],
            course_data["instructor"]
        )
        course_collection.add_course(new_course)
    return course_collection
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


