
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
    for payment in student.payment_method:
        if payment.type == data.get("type"):
            return "fail to add payment method"
    new_payment = Payment(data.get("name"),data.get("amount"),data.get("type"))
    student.add_payment_method(new_payment)
    return {"messege" : "Method added" , "New method" : new_payment} 

@router.post("/make_payment/")
async def make_payment(data : dict = Body(...)):
    student = user_collection.get_user(data.get("username"))
    payment = student.get_payment_by_type(data.get("type")) 
    print("amount : ",payment.amount)
    print("net price : ",student.cart.net_price)
    net_price = student.cart.net_price
    if payment.amount >= student.cart.net_price:
        payment.amount -= student.cart.net_price
        student.close_order()
        student.student_course.add_course_to_StudentCourse
        student.cart.clear_cart()
        return {"messege" : "Payment successfully" , "Net Price" : net_price ,"Money left :" : payment.amount}
    else:
        return "not enough money"