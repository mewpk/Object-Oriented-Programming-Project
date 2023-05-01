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


@router.post("/check_course_in_cart")
async def check_course_in_cart(data: dict = Body(...)):
    try:
        student = user_collection.get_user(data.get("username"))
        for course in course_collection.courses:
            if course.id == data.get("course_id"):
                if student.check_course_in_cart(course) == True:
                    return { "status": True }
                else: 
                    return  { "status": False }
        return "Failed to add"
    except:
        return "please try again"  



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
                    # student.remove_from_cart(course)
                    return "course already in cart"
        return "Failed to add"
    except:
        return "please try again"  

@router.post("/remove_course_from_cart/")
async def remove_cart(data: dict = Body(...)):
    try:
        student = user_collection.get_user(data.get("username"))
        for course in course_collection.courses:
            if course.id == data.get("course_id"):
                if student.check_course_in_cart(course) == False:
                    student.remove_from_cart(course)
                    return "success to remove"
                else: 
                    return "this course is not in the cart"
        return "Fail to remove"
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
        cart = student.cart
        total_price = student.view_total_price()
        return coupon_collection.use_coupon(coupon,cart,total_price)
    except:
        return "invalid coupon / does not meet the conditions of coupon"
    
@router.post("/cart/apply_coupon/make_payment")
async def payment(payment_data: dict=Body(...)):
    try:
        user = user_collection.get_user(payment_data.get("username"))
        user.make_payment()
        return "payment successful" 
    except :
        return "try again"

    
