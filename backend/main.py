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
print("Account : ", Account.student1)
print("--------------------------------------------------------\n")
print("Course : ", Course.course1)
print("--------------------------------------------------------\n")
print("Course Review : ", Course.course1.check_course_review())
print("--------------------------------------------------------\n")
# add 
Account.instrutor1.add_course("11111111","Learn Game Development with JavaScript", "Make your own animated 2D games", "10/2565", "English", "Build 2d games with HTML, CSS & JavaScript, no frameworks and no libraries", 4, "Basic knowledge of HTML, CSS & JavaScript is needed to follow this course", " Let's practise object oriented programming and use HTML, CSS and plain vanilla JavaScript to build a game. There will be no frameworks and no libraries, because we want deep understanding of how things work under the hood.", "Beginner front end web developers curious about animation and 2D games", 599, 0, "3 hours on-demand video , Access on mobile and TV , Certificate of completion", ["Development", "Web Development", "JavaScript"])
Account.instrutor1.add_course("11111111","Learn Game Development with JavaScript", "Make your own animated 2D games", "10/2565", "English", "Build 2d games with HTML, CSS & JavaScript, no frameworks and no libraries", 4, "Basic knowledge of HTML, CSS & JavaScript is needed to follow this course", " Let's practise object oriented programming and use HTML, CSS and plain vanilla JavaScript to build a game. There will be no frameworks and no libraries, because we want deep understanding of how things work under the hood.", "Beginner front end web developers curious about animation and 2D games", 599, 0, "3 hours on-demand video , Access on mobile and TV , Certificate of completion", ["Development", "Web Development", "JavaScript"])
print(Course.Course.instances)
