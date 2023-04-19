from .Users import UsersCollection
from .Categories import CatagoriesCollection
from .Coupon import CouponCollection
from .Course import CourseCollection
from .StudentCourse import StudentCourseCollection
# from .CourseViewChapter import CoursesViewChaptersCollection
from .Review import ReviewCollection
# from .WishList import WishListCollection

user_collection = UsersCollection()
course_collection = CourseCollection()
categories_collection = CatagoriesCollection()
coupon_collection = CouponCollection()
studentcourse_collection = StudentCourseCollection()
review_collection = ReviewCollection()
