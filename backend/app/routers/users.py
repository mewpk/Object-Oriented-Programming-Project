from fastapi import APIRouter, Body

# from ..services.services import users_service
from ..config.database import user_collection
from ..models.Users import Student


router = APIRouter()

@router.get("/users")
async def get_users():
    return  user_collection.get_users()

@router.post("/users/")
async def create_student(user_data: dict = Body(...)):
    new_student = Student(user_data["id"], user_data["name"], user_data["username"], user_data["password"], user_data["language"],user_data["email"], user_data["role"], user_data["about"], user_data["review"])
    data = user_collection.add_user(new_student)
    if new_student and data:
        return {"message": "Student created successfully", "user": data}
    else:
        return {"message": "Failed to create Student"}
    
@router.post("/login/")
async def login(user_data: dict = Body(...)):
    user = user_collection.login(user_data["username"], user_data["password"])
    if user:
        return {"message": "Logged in successfully", "user": user}
    else:
        return {"message": "Failed to login"}
