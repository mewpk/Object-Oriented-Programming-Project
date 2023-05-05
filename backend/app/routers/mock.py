from fastapi import APIRouter, Body
from ..config.database import user_collection,coupon_collection,course_collection,studentcourse_collection
from ..models.Users import Student,Instructor,Admin
from ..models.Coupon import Coupon,CouponCourse,CouponInstructor
from ..models.Order import Order
from ..models.Course import Course
from random import random,randint

router = APIRouter()

@router.get("/mock/")
async def mock_everything_except_course():
   for i in range(50):
      #mock Student
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
   
   #mock Instructor
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

   #mock Admin
   for i in range(3):
      user_data3 ={
         "name" : f"name {i}",
         "username" : f"username{i+1000}",
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

   #mock coupon ALL
   for i in range(1,6):
      data = {
         "passcode" : f"311{i}",
         "start_date" : "14/09/2022",    
         "end_date" : "13/09/2023",
         "type" : "All",
         "condition" : f"buy at least {i}00 baht",
         "at_least" : i*100,
         "discounted_price" : 0,
         "discounted_percent" : i*5,
      }
      new_coupon = Coupon(
         data["passcode"],
         data["start_date"],
         data["end_date"],
         data["type"],
         data["condition"],
         data["at_least"],
         data["discounted_price"],
         data["discounted_percent"],
      )
      coupon_collection.add_coupon(new_coupon)
    
   for i in range(6,10):
      data = {
         "passcode" : f"311{i}",
         "start_date" : "14/09/2022",
         "end_date" : "13/09/2023",
         "type" : "All",
         "condition" : f"buy at least {i}00 baht",
         "at_least" : i*100,
         "discounted_price" : 100+i*10,
         "discounted_percent" : 0
      }
      new_coupon = Coupon(
         data["passcode"],
         data["start_date"],
         data["end_date"],
         data["type"],
         data["condition"],
         data["at_least"],
         data["discounted_price"],
         data["discounted_percent"],
      )
      coupon_collection.add_coupon(new_coupon)

   #mock Coupon Instructor
   coupon_instructor1 = CouponInstructor(
      passcode = "2222",
      start_date = "14/09/2022",
      end_date = "13/09/2023",
      type = "Instructor",
      condition = "buy at least 300 baht",
      at_least = 300,
      discounted_price = 0,
      discounted_percent = 20,
      instructor_name = "Pookkie Eiei")
   coupon_collection.add_coupon(coupon_instructor1)

   coupon_instructor2 = CouponInstructor(
      passcode = "2223",
      start_date = "01/01/2022",
      end_date = "08/06/2023",
      type = "Instructor",
      condition = "buy at least 100 baht",
      at_least = 100,
      discounted_price = 50,
      discounted_percent = 0,
      instructor_name = "Nong Preawa")
   coupon_collection.add_coupon(coupon_instructor2)

   coupon_instructor3 = CouponInstructor(
      passcode = "2224",
      start_date = "14/09/2022",
      end_date = "13/09/2023",
      type = "Instructor",
      condition = "buy at least 100 baht",
      at_least = 200,
      discounted_price = 0,
      discounted_percent = 20,
      instructor_name = "lnw Pat")
   coupon_collection.add_coupon(coupon_instructor3)

   coupon_instructor4 = CouponInstructor(
      passcode = "2225",
      start_date = "30/04/2023",
      end_date = "30/05/2023",
      type = "Instructor",
      condition = "buy at least 500 baht",
      at_least = 500,
      discounted_price = 0,
      discounted_percent = 40,
      instructor_name = "Mew kuki")
   coupon_collection.add_coupon(coupon_instructor4)

   #mock Coupon Course
   for i in range(6):
      data = {
         "passcode" : f"111{i}",
         "start_date" : "14/09/2022",
         "end_date" : "13/09/2023",
         "type" : "Course",
         "condition" : "buy at least 200 baht",
         "at_least" : 200,
         "discounted_price" : 0,
         "discounted_percent" : 10,
         "course_id" : i
      }
      new_coupon = CouponCourse(
         data["passcode"],
         data["start_date"],
         data["end_date"],
         data["type"],
         data["condition"],
         data["at_least"],
         data["discounted_price"],
         data["discounted_percent"],
         data["course_id"]
      )
      coupon_collection.add_coupon(new_coupon)
        
   for i in range(6,10):
      data = {
         "passcode" : f"111{i}",
         "start_date" : "14/09/2022",
         "end_date" : "13/09/2023",
         "type" : "Course",
         "condition" : "buy at least 200 baht",
         "at_least" : 200,
         "discounted_price" : 50,
         "discounted_percent" : 0,
         "course_id" : i
      }
      new_coupon = CouponCourse(
         data["passcode"],
         data["start_date"],
         data["end_date"],
         data["type"],
         data["condition"],
         data["at_least"],
         data["discounted_price"],
         data["discounted_percent"],
         data["course_id"]
        )
      coupon_collection.add_coupon(new_coupon)

   # for i in range(50):
   #    student = user_collection.get_user(f"username{i}")
   #    course_id = randint(1, 12)
   #    course = course_collection.get_course(course_id)
   #    student.student_course.add_student_course(course)
   #    new_order = Order(len(student.orders)+1,"Purchased",course,course.price,course.price)
   #    student.add_order(new_order)
   
   return "Mock info successful"
   