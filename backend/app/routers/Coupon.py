from fastapi import APIRouter, Body

from ..config.database import coupon_collection
from ..models.Coupon import Coupon,CouponCourse,CouponInstructor

from datetime import datetime

router = APIRouter()

@router.get("/coupon")
async def get_coupon():
    return  coupon_collection.get_coupon()

@router.post("/coupon/")
async def create_coupon(coupon: dict = Body(...)):
    try:
        if Coupon.get("type") == "Instructor":
            new_coupon = CouponInstructor(coupon.get("id"),coupon.get("passcode"),coupon.get("start_date"),coupon.get("end_date"),coupon.get("type"),coupon.get("condition"),
                        coupon.get("at_least"),coupon.get("discounted_price"),coupon.get("discount_percent"),coupon.get("instructor_name"))
        elif Coupon.get("type") == "Course":
            new_coupon = CouponCourse(coupon.get("id"),coupon.get("passcode"),coupon.get("start_date"),coupon.get("end_date"),coupon.get("type"),coupon.get("condition"),
                        coupon.get("at_least"),coupon.get("discounted_price"),coupon.get("discount_percent"),coupon.get("course_id"))
        else:
            new_coupon = Coupon(coupon.get("id"),coupon.get("passcode"),coupon.get("start_date"),coupon.get("end_date"),coupon.get("type"),coupon.get("condition"),
                        coupon.get("at_least"),coupon.get("discounted_price"),coupon.get("discount_percent"))
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
