from fastapi import APIRouter, Body
from ..config.database import categories_collection
from ..models.Categories import Categories


router = APIRouter()
@router.get("/mockcategories")
async def mock_categories():
    categories = {
    "0": "OOP",
    "1": "Algorithms",
    "2": "Data Structures",
    "3": "Artificial Intelligence",
    "4": "Machine Learning",
    "5": "Deep Learning",
    "6": "Computer Vision",
    "7": "Natural Language Processing",
    "8": "Neural Networks",
    "9": "Big Data",
    "10": "JavaScript",
    "11": "Python",
    "12": "C",
    "13": "Data Science",
    "14": "Blockchain",
    "15": "Cybersecurity",
    "16": "Ethical Hacking",
    "17": "Penetration Testing",
    "18": "Computer Networking",
    "19": "Cloud Computing",
    "20": "DevOps",
    "21": "Docker",
    "22": "C++",
    "23": "Linux",
    "24": "Unix",
    "25": "Windows Server",
    "26": "Database Design",
    "27": "SQL",
    "28": "Oracle",
    "29": "MySQL",
    "30": "PostgreSQL",
    "31": "MongoDB",
    "32": "Cryptography",
    "33": "Operating Systems",
    "34": "Virtualization",
    "35": "CompTIA",
    "36": "Cisco",
    "37": "Microsoft",
    "38": "Java",
    "39": "Web development",
    "40": "IT Certification",
    "41": "Software Engineering",
    "42": "App development",
    "43": "Scrum",
    "44": "Project Management",
    "45": "Business Analysis",
    "46": "Data Analysis",
    "47": "Excel",
    "48": "Power BI",
    "49": "Tableau",
    "50": "SAP",
}

    for i in range(50):
        category_data = {
            "name": categories.get(str(i))
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
        new_category = Categories(category.get("name"))
        data = categories_collection.add_category(new_category)
        if new_category and data:
            return {"message": "Category created successfully", "category": new_category}
        else:
            return {"message": "Failed to create category"}
    except:
        return "please try again"