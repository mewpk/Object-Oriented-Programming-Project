from fastapi import APIRouter, Body
from ..models.Payment import Payment
from ..config.database import user_collection,payment_collection
router = APIRouter()

@router.get("/payment_method")
async def payment_method():
    return payment_collection.payment_method

@router.post("/payment/")
async def get_payment(data : dict = Body(...)):
    student = user_collection.get_user(data.get("username"))
    return student.payment_method.payment

@router.post("/add_payment_method/")
async def add_payment_method(data : dict = Body(...)):
    student = user_collection.get_user(data.get("username"))
    for payment in student.payment_method.payment:
        if payment.type == data.get("type") and payment.name == data.get("name"):
            return "fail to add payment method"
    new_payment = Payment(data.get("name"),data.get("amount"),data.get("type"))
    student.add_payment_method(new_payment)
    return {"messege" : "Method added" , "New method" : new_payment} 

@router.post("/make_payment/")
async def make_payment(data : dict = Body(...)):
    student = user_collection.get_user(data.get("username"))
    payment = student.get_payment_method(data.get("type"),data.get("name"))
    order = student.get_order_by_id(data.get("order_id"))
    # net_price = student.cart.net_price
    if int(payment.amount) >= int(order.net_price):
        student.close_order(order,payment)
        return {"messege" : "Payment successfully" , "Net Price" : order.net_price ,"Money left :" : payment.amount}
    else:
        return "not enough money"