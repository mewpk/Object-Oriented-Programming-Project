from fastapi import APIRouter, Body

from ..config.database import user_collection
from ..models.Order import Order


router = APIRouter()

@router.get("/order/{username}")
async def get_order(username):
    student = user_collection.get_user(username)
    return student.view_orders(username)

@router.get("/order/view_refund/{username}")
async def get_order_view_refund(username):
    student = user_collection.get_user(username)
    return student.view_refunds(username)

@router.post("/order/")
async def create_order(order: dict = Body(...)):
    new_order = Order(order["id"], order["status"], order["date"])
    student = user_collection.get_user(order["username"])
    data = student.add_order(order["username"],new_order)
    if new_order and data:
        return {"message": "Course created successfully", "user": data}
    else:
        return {"message": "Failed to create course"}
