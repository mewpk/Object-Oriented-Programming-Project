from fastapi import APIRouter, Body

from ..models.Course import Course
from ..models.Users import Student
from ..models.Payment import Payment

router = APIRouter()

@router.post("/payment/")
async def create_payment(data : dict = Body(...)):
    new_payment = Payment(data.get("country"),data.get("method"),"Pending")
    