from fastapi import APIRouter

router = APIRouter()

@router.get("/orders")
async def get_orders():
    # return orders
    pass

@router.post("/orders")
async def create_order():
    # create a new order
    pass
