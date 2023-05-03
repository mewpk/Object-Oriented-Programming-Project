from fastapi import APIRouter, Body

from ..config.database import user_collection

from ..models.Order import Order


router = APIRouter()

@router.post("/order/")
async def get_order(data : dict = Body(...)):
    user = user_collection.get_user(data.get("username"))
    return user.orders

@router.get("/order/view_refund/")
async def get_order_view_refund(data : dict = Body(...)):
    user = user_collection.get_user(data.get("username"))
    return user.view_refunds()

@router.post("/add_order/")
async def add_order(data : dict = Body(...)):
    try:
        student = user_collection.get_user(data.get("username"))
        # print("to order")
        # total_price = student.cart.price
        # net_price = student.cart.net_price
        # print("pp")
        # print(total_price,net_price)
        new_order = Order("Pending",student.cart.course,student.cart.price,student.cart.net_price)      
        student.add_order(new_order)
        return "success to add"
    except:
        return "try again"
    