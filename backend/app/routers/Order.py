from fastapi import APIRouter

from ..config.database import user_collection


router = APIRouter()

@router.get("/order/{username}")
async def get_order(username):
    user = user_collection.get_user(username)
    return user.orders

@router.get("/order/view_refund/{username}")
async def get_order_view_refund(username):
    user = user_collection.get_user(username)
    return user.view_refunds()
