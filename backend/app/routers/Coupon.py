from fastapi import APIRouter, Body

from ..config.database import coupon_collection
from ..models.Coupon import Coupon

router = APIRouter()

@router.get("/coupon")
async def get_coupon():
    return  coupon_collection.get_coupon()

@router.post("/coupon/")
async def create_coupon(coupon: dict = Body(...)):
    new_coupon = Coupon(coupon["id"],coupon["passcode"],coupon["start_date"],coupon["end_date"],coupon["type"],coupon["condition"])
    data = coupon_collection.add_coupon(new_coupon)
    if new_coupon and data:
        return {"message": "Coupon created successfully", "coupon": new_coupon}
    else:
        return {"message": "Failed to create coupon"}