import Course
import Categories
import Account
print("Course Category : ",Course.course1.check_categories())
print("--------------------------------------------------------\n")
print("Categories : ",[category.name for category in Categories.Categories.instances])
print("--------------------------------------------------------\n")
print("Purchase history : ",Account.Student.request_history('finish'))