import Account
import Cart
import Categories
import Coupon
import CouponList
import Course
import CourseViewChapter
import Notification
import Order
import Payment
import Promotion
import Review
import StudentCourse
print("-----------------------Program Starting-------------------")
print("--------------------------------------------------------\n")
print("Preview : ",Course.course1.request_preview())
print("--------------------------------------------------------\n")
print("Course : ",Course.course1)
print("--------------------------------------------------------\n")
print("Add payment method : ",Payment.payment1.add_payment_method('cash'))
print("--------------------------------------------------------\n")
print("New Payment : ",Payment.payment1)