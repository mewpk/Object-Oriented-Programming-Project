from fastapi import APIRouter, Body

from ..config.database import studentcourse_collection,user_collection
# from ..models.StudentCourse import StudentCourse


router = APIRouter()

@router.post("/studentcourse")
async def get_studentcourse(data: dict = Body(...)):
    student = user_collection.get_user(data.get("username"))
    return  student.student_course

@router.post("/learning")
async def change_progress(data: dict = Body(...)):
    student = user_collection.get_user(data.get("username"))
    for course in student.student_course.courses:
        if course.studentcourse_id == data.get("studentcourse_id"):
            for chapter in course.chapters:
                if chapter.id == data.get("chapter_id"):
                    chapter.progress = 100
            all_progress = course.calculate_progress()
    return  {"all_progress" : all_progress}

# @router.post("/studentcourse")
# async def add_to_studentcourse(data: dict = Body(...)):
#     user = user_collection.get_user(data.get("username"))
#     user.add_to_student_course




