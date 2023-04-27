from .Users import UsersCollection
from .Categories import CategoriesCollection
from .Coupon import CouponCollection
from .Course import CourseCollection
from .StudentCourse import StudentCourseCollection
# from .CourseViewChapter import CoursesViewChaptersCollection
from .Review import ReviewCollection
from .WishList import WishListCollection
from .Cart import CartCollection


user_collection = UsersCollection()
course_collection = CourseCollection()
categories_collection = CategoriesCollection()
coupon_collection = CouponCollection()
studentcourse_collection = StudentCourseCollection()
review_collection = ReviewCollection()
cart_collection = CartCollection()
wishlist_collection = WishListCollection()

