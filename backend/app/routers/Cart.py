from fastapi import APIRouter, Body

from ..config.database import cart_collection,course_collection,user_collection,coupon_collection
from ..models.Course import Course
from ..models.Users import Student

router = APIRouter()

@router.post("/cart/")
async def get_cart(data : dict = Body(...)):
    for user in user_collection.users:
        if user.username == data.get("username"):
            student = user
            return student.cart
    

@router.post("/add_cart/")
async def add_cart(data: dict = Body(...)):
    try:
        student = user_collection.get_user(data.get("username"))
        for course in course_collection.courses:
            if course.id == data.get("course_id"):
                if student.check_course_in_cart(course) == True:
                    student.add_to_cart(course)
                    return "success to add"
                else: 
                    student.remove_from_cart(course)
                    return "success to remove"
        return "Failed to add"
    except:
        return "please try again"

@router.post("/cart/total_price/")
async def get_total_price(username : str):
    try:
        student = user_collection.get_user(username)
        return student.view_total_price()
    except:
        return "please try again"
    
@router.post("/cart/apply_coupon")
async def apply_coupon(data: dict=Body(...)):
    try:
        student = user_collection.get_user(data.get("username"))
        coupon = coupon_collection.get_coupon_by_passcode(data.get("passcode"))
        return coupon_collection.use_coupon(coupon,student.cart,student.view_total_price)
    except:
        return "invalid coupon / does not meet the conditions of coupon"

            

    
