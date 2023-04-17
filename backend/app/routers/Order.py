from fastapi import APIRouter, Body

from ..config.database import user_collection
from ..models.Order import Order


router = APIRouter()

@router.get("/order/{student_id}")
async def get_order(student_id):
    student = user_collection.get_user(student_id)
    return student.view_orders(student_id)

@router.get("/order/view_refund/{student_id}")
async def get_order_view_refund(student_id):
    student = user_collection.get_user(student_id)
    return student.view_refunds(student_id)

@router.post("/order/")
async def create_order(order: dict = Body(...)):
    new_order = Order(order["id"], order["status"], order["date"])
    student = user_collection.get_user(order["student_id"])
    data = student.add_order(order["student_id"],new_order)
    if new_order and data:
        return {"message": "Course created successfully", "user": data}
    else:
        return {"message": "Failed to create course"}
