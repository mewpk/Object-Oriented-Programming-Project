from fastapi import APIRouter, Body

# from ..services.services import users_service
from ..config.database import user_collection
from ..models.Users import Student,Instructor,Admin


router = APIRouter()

@router.get("/users")
async def get_users():
    return  user_collection.get_users()

@router.post("/register/")
async def create_users(user_data: dict = Body(...)):
    if user_collection.verify_username(user_data["username"]) == True:
        if user_data["role"] == "Student":
            new_user = Student(user_data["name"], user_data["username"], user_data["password"], user_data["language"],user_data["email"], user_data["role"],"", "")
        elif user_data["role"] == "Instructor":
            new_user = Instructor(user_data["name"], user_data["username"], user_data["password"], user_data["language"],user_data["email"], user_data["role"],"", "")
        elif user_data["role"] == "Admin":
            new_user = Admin(user_data["name"], user_data["username"], user_data["password"], user_data["language"],user_data["email"], user_data["role"],"", "")
        user_hash_password =user_collection.hash_password(new_user)
        data = user_collection.add_user(user_hash_password)
        if new_user and data:
            return {"message": new_user.role +" created successfully", "user": data}
        else:
            return {"message": "Failed to create "+ new_user.role}
    else: return {"message": "Failed to create user"}
    
    
@router.post("/login/")
async def login(user_data: dict = Body(...)):
    user = user_collection.verify_login(user_data)
    if user != False:
        return {"message": "Logged in successfully", "user": user}
    else:
        return {"message": "Failed to login"}
