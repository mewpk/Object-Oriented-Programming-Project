from fastapi import APIRouter, Body

from ..models.Course import Course
from ..models.Users import Student
from ..models.Payment import Payment

from ..config.database import user_collection
router = APIRouter()

@router.post("/payment/")
async def get_payment(data : dict = Body(...)):
    student = user_collection.get_user(data.get("username"))
    return student.payment_method

@router.post("/add_payment/")
async def add_payment(data : dict = Body(...)):
    student = user_collection.get_user(data.get("username"))
    new_payment = Payment(data.get("name"),data.get("amount"),data.get("type"))
    return student.add_payment_method(new_payment)