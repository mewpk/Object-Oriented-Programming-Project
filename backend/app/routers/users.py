from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def get_users():
    # return users
    pass

@router.post("/users")
async def create_user():
    # create a new user
    pass
