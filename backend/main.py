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
import WishList
print("-----------------------Program Starting-------------------")
print("--------------------------------------------------------\n")
print("Account : ",Account.student1)
print("--------------------------------------------------------\n")
print("Course : ",Course.course1)
print("--------------------------------------------------------\n")
print("Course Review : ",Course.course1.check_course_review())
print("--------------------------------------------------------\n")
print("Wishlist :" ,Account.student1.add_to_wishlist(id_course = '11111111'))
print("--------------------------------------------------------\n")
print("Wishlist :" ,Account.student1.add_to_wishlist(id_course = '11111112'))
print("--------------------------------------------------------\n")
print("View_wishlist : ",",".join([ str(course) for course in WishList.Wishlist.list_wishlist]))
print("--------------------------------------------------------\n")
print("remove_wishlist : ",Account.student1.remove_from_wishlist(id_course = '11111111'))
print("--------------------------------------------------------\n")
print("View_wishlist : ",",".join([ str(course) for course in WishList.Wishlist.list_wishlist]))
print("--------------------------------------------------------\n")
print("Refund history : ",Account.student2.request_history('refund'))
print("--------------------------------------------------------\n")
# print(Account.instrutor1.edit_course('11111111','new_name','new_promotion','new_description','new_price'))