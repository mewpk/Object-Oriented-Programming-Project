from fastapi import APIRouter, Body

from ..config.database import user_collection

from ..models.Order import Order


router = APIRouter()

@router.get("/order/")
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
        user = user_collection.get_user(data.get("username"))
        print("to order")
        new_order = Order("Paiding",user.cart.course,user.cart.price,user.cart.net_price)
        print(new_order)
        user.add_order(new_order)
        return "success to add"
    except:
        return "try again"