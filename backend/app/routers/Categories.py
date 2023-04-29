from fastapi import APIRouter, Body

from ..config.database import categories_collection
from ..models.Categories import Categories


router = APIRouter()

@router.get("/category")
async def get_category():
    return  categories_collection.get_categories()

@router.post("/category/")
async def create_categories(category: dict = Body(...)):
    try:
        new_category = Categories(category.get("id"),category.get("name"))
        data = categories_collection.add_categories(new_category)
        if new_category and data:
            return {"message": "Category created successfully", "category": new_category}
        else:
            return {"message": "Failed to create category"}
    except:
        return "please try again"