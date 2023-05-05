from fastapi import APIRouter, Body
from ..config.database import coupon_collection
from ..models.Coupon import Coupon,CouponCourse,CouponInstructor
from datetime import datetime

router = APIRouter()

@router.get("/coupon")
async def get_coupon():
    return  coupon_collection.coupons

@router.post("/coupon/")
async def create_coupon(coupon: dict = Body(...)):
    try:
        if coupon.get("type") == "Instructor":
            new_coupon = CouponInstructor(coupon.get("passcode"),coupon.get("start_date"),coupon.get("end_date"),coupon.get("type"),coupon.get("condition"),
                        coupon.get("at_least"),coupon.get("discounted_price"),coupon.get("discounted_percent"),coupon.get("instructor_name"))
        elif coupon.get("type") == "Course":
            new_coupon = CouponCourse(coupon.get("passcode"),coupon.get("start_date"),coupon.get("end_date"),coupon.get("type"),coupon.get("condition"),
                        coupon.get("at_least"),coupon.get("discounted_price"),coupon.get("discounted_percent"),coupon.get("course_id"))
        elif coupon.get("type") == "All":
            new_coupon = Coupon(coupon.get("passcode"),coupon.get("start_date"),coupon.get("end_date"),coupon.get("type"    ),coupon.get("condition"),
                        coupon.get("at_least"),coupon.get("discounted_price"),coupon.get("discounted_percent"))
        else : 
            return {"message" : "invailed Coupon Type !"}
        
        data = coupon_collection.add_coupon(new_coupon)
        if new_coupon and data:
            return {"message": "Coupon created successfully", "coupon": new_coupon}
        else:   
            return {"message": "Failed to create coupon"}
    except: 
        return "please try again"
    
@router.get("/update_coupon")
async def update_coup():
    return str(coupon_collection.expire_coupon(datetime.now()))

@router.get("/mock_couponAll")
async def mock_couponsAll():
    for i in range(1,6):
        data = {
        "passcode" : f"311{i}",
        "start_date" : "14/09/2022",    
        "end_date" : "13/09/2023",
        "type" : "All",
        "condition" : f"buy at least {i}00 baht",
        "at_least" : i*100,
        "discounted_price" : 0,
        "discounted_percent" : i*5,
        }
        new_coupon = Coupon(
            data["passcode"],
            data["start_date"],
            data["end_date"],
            data["type"],
            data["condition"],
            data["at_least"],
            data["discounted_price"],
            data["discounted_percent"],
        )
        coupon_collection.add_coupon(new_coupon)
    
    for i in range(6,10):
        data = {
        "passcode" : f"311{i}",
        "start_date" : "14/09/2022",
        "end_date" : "13/09/2023",
        "type" : "All",
        "condition" : f"buy at least {i}00 baht",
        "at_least" : i*100,
        "discounted_price" : 100+i*10,
        "discounted_percent" : 0
        }
        new_coupon = Coupon(
            data["passcode"],
            data["start_date"],
            data["end_date"],
            data["type"],
            data["condition"],
            data["at_least"],
            data["discounted_price"],
            data["discounted_percent"],
        )
        coupon_collection.add_coupon(new_coupon)
    return coupon_collection.show_coupon_type("All")

@router.get("/mock_couponInstructor")
async def mock_couponsInstructor():
    coupon_instructor1 = CouponInstructor(
        passcode = "2222",
        start_date = "14/09/2022",
        end_date = "13/09/2023",
        type = "Instructor",
        condition = "buy at least 300 baht",
        at_least = 300,
        discounted_price = 0,
        discounted_percent = 20,
        instructor_name = "Pookkie Eiei")
    coupon_collection.add_coupon(coupon_instructor1)

    coupon_instructor2 = CouponInstructor(
        passcode = "2223",
        start_date = "01/01/2022",
        end_date = "08/06/2023",
        type = "Instructor",
        condition = "buy at least 100 baht",
        at_least = 100,
        discounted_price = 50,
        discounted_percent = 0,
        instructor_name = "Nong Preawa")
    coupon_collection.add_coupon(coupon_instructor2)

    coupon_instructor3 = CouponInstructor(
        passcode = "2224",
        start_date = "14/09/2022",
        end_date = "13/09/2023",
        type = "Instructor",
        condition = "buy at least 100 baht",
        at_least = 200,
        discounted_price = 0,
        discounted_percent = 20,
        instructor_name = "lnw Pat")
    coupon_collection.add_coupon(coupon_instructor3)

    coupon_instructor4 = CouponInstructor(
        passcode = "2225",
        start_date = "30/04/2023",
        end_date = "30/05/2023",
        type = "Instructor",
        condition = "buy at least 500 baht",
        at_least = 500,
        discounted_price = 0,
        discounted_percent = 40,
        instructor_name = "Mew kuki")
    coupon_collection.add_coupon(coupon_instructor4)
    return coupon_collection.show_coupon_type("Instructor")




@router.get("/mock_couponCourse")
async def mock_couponsCourse():
    for i in range(6):
        data = {
        "passcode" : f"111{i}",
        "start_date" : "14/09/2022",
        "end_date" : "13/09/2023",
        "type" : "Course",
        "condition" : "buy at least 200 baht",
        "at_least" : 200,
        "discounted_price" : 0,
        "discounted_percent" : 10,
        "course_id" : i
        }
        new_coupon = CouponCourse(
            data["passcode"],
            data["start_date"],
            data["end_date"],
            data["type"],
            data["condition"],
            data["at_least"],
            data["discounted_price"],
            data["discounted_percent"],
            data["course_id"]
        )
        coupon_collection.add_coupon(new_coupon)
        
    for i in range(6,10):
        data = {
        "passcode" : f"111{i}",
        "start_date" : "14/09/2022",
        "end_date" : "13/09/2023",
        "type" : "Course",
        "condition" : "buy at least 200 baht",
        "at_least" : 200,
        "discounted_price" : 50,
        "discounted_percent" : 0,
        "course_id" : i
        }
        new_coupon = CouponCourse(
            data["passcode"],
            data["start_date"],
            data["end_date"],
            data["type"],
            data["condition"],
            data["at_least"],
            data["discounted_price"],
            data["discounted_percent"],
            data["course_id"]
        )
        coupon_collection.add_coupon(new_coupon)

    return coupon_collection.show_coupon_type("Course")
