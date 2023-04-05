from fastapi import APIRouter, Body

from ..services.services import coupon_service


router = APIRouter()

@router.get("/coupon")
async def get_coupon():
    return  coupon_service.get_coupon()

@router.post("/coupon/")
async def create_coupon(coupon_data: dict = Body(...)):
    new_coupon = coupon_service.add_coupon(coupon_data)
    if new_coupon:
        return {"message": "Coupon created successfully", "coupon": new_coupon}
    else:
        return {"message": "Failed to create coupon"}
