from .Users import UsersCollection
from .Categories import CategoriesCollection
from .Coupon import CouponCollection
from .Course import CourseCollection
from .StudentCourse import StudentCourseCollection
from .Review import ReviewCollection
from .Payment import PaymentCollection

user_collection = UsersCollection()
course_collection = CourseCollection()
categories_collection = CategoriesCollection()
coupon_collection = CouponCollection()
studentcourse_collection = StudentCourseCollection()
review_collection = ReviewCollection()
payment_collection = PaymentCollection()

