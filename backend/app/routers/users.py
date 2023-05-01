from fastapi import APIRouter, Body

from ..models.Cart import Cart

# from ..services.services import users_service
from ..config.database import user_collection
from ..models.Users import Student,Instructor,Admin


router = APIRouter()

@router.get("/mockuser/student")
async def mockuser():
    for i in range(50):
        user_data1 ={
            "name" : f"name {i}",
            "username" : f"username{i}",
            "password" : f"password {i}",
            "language": "English",
            "email" : "123@email.com",
            "role" : "Student"
        }
        new_student= Student(
            user_data1.get("name"),
            user_data1.get("username"),
            user_collection.hash_password(user_data1.get("password")),
            user_data1.get("language"),
            user_data1.get("email"),
            user_data1.get("role")        
        )
        user_collection.add_user(new_student)
   
    for i in range(10):
        user_data2 ={
            "name" : f"name {i}",
            "username" : f"username{i+100}",
            "password" : f"password {i}",
            "language": "English",
            "email" : "123@email.com",
            "role" : "Instructor"
        }
        new_instructor = Instructor(
            user_data2.get("name"),
            user_data2.get("username"),
            user_collection.hash_password(user_data2.get("password")),
            user_data2.get("language"),
            user_data2.get("email"),
            user_data2.get("role")        
        )
        user_collection.add_user(new_instructor)
    for i in range(3):
        user_data3 ={
            "name" : f"name {i}",
            "username" : f"username{i+100}",
            "password" : f"password {i}",
            "language": "English",
            "email" : "123@email.com",
            "role" : "Admin"
        }
        new_admin = Admin(
            user_data3.get("name"),
            user_data3.get("username"),
            user_collection.hash_password(user_data3.get("password")),
            user_data3.get("language"),
            user_data3.get("email"),
            user_data3.get("role")        
        )
        user_collection.add_user(new_admin)
        return user_collection


@router.get("/users")
async def get_users():
    return  user_collection.users
    
@router.post("/user")
async def get_user(user_data: dict = Body(...)):
    return user_collection.get_user(user_data.get("username"))


@router.get("/unverified_instructors/")
async def get_unverified_instructors():
    return user_collection.get_unverified_instructors()


@router.post("/register/")
async def create_user(user_data: dict = Body(...)):
    # try :
        if user_collection.verify_username(user_data.get("username")) == True:
            if user_data.get("role") == "Student":
                new_user = Student(user_data.get("name"), user_data.get("username"), user_collection.hash_password(user_data.get("password")), user_data.get("language"),user_data.get("email"), user_data.get("role"))
            elif user_data.get("role") == "Instructor":
                new_user = Instructor(user_data.get("name"), user_data.get("username"), user_collection.hash_password(user_data.get("password")), user_data.get("language"),user_data.get("email"), user_data.get("role"))
            elif user_data.get("role") == "Admin":
                new_user = Admin(user_data.get("name"), user_data.get("username"), user_collection.hash_password(user_data.get("password")), user_data.get("language"),user_data.get("email"), user_data.get("role"))
            else : 
                return {"message" : "Invalid Role"}
            data = user_collection.add_user(new_user)
            if new_user and data:
                return {"message": new_user.role +" created successfully", "user": data}
            else:
                return {"message": "Failed to create user"}
        else: return {"message": "Failed to create user"}
    # except :
    #     return "please try again"
        
    # ขยันน
@router.post("/login/")
async def login(user_data: dict = Body(...)):
    try:
        user = user_collection.verify_login(user_data)
        if user:
            return {"message": "Logged in successfully", "user": user , "status": True}
        else:
            return {"message": "Failed to login"}
    except:
        return "please try again"

@router.put("/verify_instructors/")
async def verify_instructors(user_data: dict = Body(...)):
    try:
        user = user_collection.verify_instructors(user_data.get("username"))
        if user:
            return {"message": "Verified successfully","username" : user_data.get("username") ,"verify": user}
        else:
            return {"message": "Failed to verify"}
    except:
        return "please try again"
    
@router.put("/edit_profile/")
async def edit_profile(user_data: dict = Body(...)):
    try:
        user = user_collection.edit_profile(user_data.get("username"),user_data.get("name"),user_data.get("language") , user_data.get("email"),user_data.get("about"))
        if user:
            return {"message": "Edit profile successfully","profile" : user}
        else:
            return {"message": "Failed to Edit profile"}
    except:
        return "please try again"
