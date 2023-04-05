from fastapi import APIRouter, Body

from ..services.services import users_service


router = APIRouter()

@router.get("/users")
async def get_users():
    return  users_service.get_users()

@router.post("/users/")
async def create_user(user_data: dict = Body(...)):
    new_user = users_service.add_user(user_data)
    if new_user:
        return {"message": "User created successfully", "user": new_user}
    else:
        return {"message": "Failed to create user"}
