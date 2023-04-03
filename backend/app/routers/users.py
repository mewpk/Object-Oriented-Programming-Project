from fastapi import APIRouter
from ..services.Users import UsersService

router = APIRouter()

@router.get("/users")
async def get_users():
    return  UsersService.get_users()

@router.post("/users")
async def create_user():
    # create a new user
    pass
