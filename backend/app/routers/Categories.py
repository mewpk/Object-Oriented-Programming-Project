from fastapi import APIRouter, Body

# from ..services.Categories import CategoriesService


router = APIRouter()

@router.get("/category")
async def get_categories():
    # return  CategoriesService.get_categories()
    return

@router.post("/category/")
async def create_categories(category_data: dict = Body(...)):
    # new_category = CategoriesService.add_categories(category_data)
    # if new_category:
    #     return {"message": "Category created successfully", "category": new_category}
    # else:
    #     return {"message": "Failed to create category"}
    return
