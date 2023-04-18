from fastapi import APIRouter

router = APIRouter()

@router.get("/products")
async def get_products():
    # return products
    pass

@router.post("/products")
async def create_product():
    # create a new product
    pass
