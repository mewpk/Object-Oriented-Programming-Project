from fastapi import APIRouter, Body

from ..config.database import user_collection
from ..models.Order import Order


router = APIRouter()

@router.get("/order/{username}")
async def get_order(username):
    student = user_collection.get_user(username)
    return student.orders

@router.get("/order/view_refund/{username}")
async def get_order_view_refund(username):
    student = user_collection.get_user(username)
    return student.view_refunds()

@router.post("/order/")
async def create_order(order: dict = Body(...)):
    try:
        new_order = Order(order.get("id"), order.get("status"), order.get("date"))
        student = user_collection.get_user(order.get("username"))
        data = student.add_order(new_order)
        if new_order and data:
            return {"message": "success to add order", "user": data}
        else:
            return {"message": "Failed to add order"}
    except :
        return "please try again"
