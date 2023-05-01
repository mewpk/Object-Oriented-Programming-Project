from fastapi import APIRouter, Body

from ..config.database import categories_collection
from ..models.Categories import Categories


router = APIRouter()
@router.get("/mockcategories")
async def mock_categories():

    for i in range(50):
        category_data = {
            "name": f"Category {i}",
        }
        new_category = Categories(
            category_data.get("name")
        )
        categories_collection.add_category(new_category)
    return categories_collection


@router.get("/category/")
async def get_category():
    return  categories_collection.categories

@router.post("/category/")
async def create_category(category: dict = Body(...)):
    try:
        new_category = Categories(category.get("id"),category.get("name"))
        data = categories_collection.add_category(new_category)
        if new_category and data:
            return {"message": "Category created successfully", "category": new_category}
        else:
            return {"message": "Failed to create category"}
    except:
        return "please try again"