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
        new_order = Order(len(student.orders)+1,"Pending",student.cart.course,student.cart.price,student.cart.net_price) 
        student.add_order(new_order)
        return "success to add"
    except:
        return "try again"
    
@router.post("/refund order/")
async def refund_order(data : dict = Body(...)):
    try :
        student = user_collection.get_user(data.get("username"))
        payment_method = student.get_payment_method("Wallet",data.get("name"))
        print("p")
        if student.refund_order(data.get("order_id"),payment_method) :
            print("pp")
            return {"messege" : "Refund successfully" , "Money left :" : payment_method.amount}
        else : return "unsuccessful refund due to purcheased this order for more than 7 days"    
    except :
        return "fail to refund"

    