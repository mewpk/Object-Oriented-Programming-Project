from fastapi import APIRouter, Body

from ..config.database import course_collection,user_collection,coupon_collection
from ..models.Course import Course
from ..models.Users import Student

router = APIRouter()

@router.post("/cart/")
async def get_cart(data : dict = Body(...)):
    for user in user_collection.users:
        if user.username == data.get("username"):
            student = user
            return student.cart


# @router.post("/check_course_in_cart")
# async def check_course_in_cart(data: dict = Body(...)):
#     try:
#         student = user_collection.get_user(data.get("username"))
#         for course in course_collection.courses:
#             if course.id == data.get("course_id"):
#                 if student.check_course_in_cart(course) == True:
#                     return { "status": True }
#                 else: 
#                     return  { "status": False }
#         return "Failed to add"
#     except:
#         return "please try again"  



@router.post("/add_cart/")
async def add_cart(data: dict = Body(...)):
    try:
        student = user_collection.get_user(data.get("username"))
        for course in course_collection.courses:
            if course.id == data.get("course_id"):
                if student.check_course_in_cart(course) == True :
                    if student.student_course.check_course(course.id) == True :
                        student.add_to_cart(course)
                    else : return "you already have this course"
                    return "success to add"
                else: 
                    # student.remove_from_cart(course)
                    return "course already in cart"
        return "Failed to add"
    except:
        return "please try again"  

@router.delete("/remove_course_from_cart/")
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
        return student.cart.total_price()
    except:
        return "please try again"
    
@router.post("/cart/total_promotion")
async def get_total_promotion(data: dict=Body(...)):
    try:
        student = user_collection.get_user(data.get("username"))
        student.cart.total_promotion()
        return student.cart.net_promotion
    except:
        return "please try again"

@router.post("/cart/apply_coupon")
async def apply_coupon(data: dict=Body(...)):
    try:
        student = user_collection.get_user(data.get("username"))
        coupon = coupon_collection.get_coupon_by_passcode(data.get("passcode"))
        cart = student.cart
        promotion = student.cart.total_promotion()  
        coupon_collection.use_coupon(coupon,cart,promotion)
        # price_after_coupon = student.cart.price_after_coupon(total_coupon)
        print(student.cart.net_price)
        return cart.net_coupon
    except:
        return "invalid coupon / does not meet the conditions of coupon"
    


    
