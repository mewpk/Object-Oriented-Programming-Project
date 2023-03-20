class Course():
    def __init__(self,id,name,short_description,date,language,purpose,chapter,requirement,description,target,price,promotion,info,categories):
        self._id = id
        self._name = name
        self._short_description = short_description
        self._date = date
        self._language = language
        self._purpose = purpose
        self._chapter = chapter
        self._requirement = requirement
        self._description = description
        self._target = target
        self._price = price
        self._promotion = promotion
        self._info = info
        self._categories = categories
    def check_course_review(course_id):
        pass
    def calculate_promotion():
        pass
    def check_categories(course_id):
        pass
    def check_student_course(student_id,course_id):
        pass
    def search_name(keyword):
        pass

course1 = Course{
    id = "11111111"
    name = "Learn Game Development with JavaScript"
    short_description = "Make your own animated 2D games"
    date = "10/2565"
    language = "English"
    purpose = "Build 2d games with HTML, CSS & JavaScript, no frameworks and no libraries"
    chapter = 4
    requirement = "Basic knowledge of HTML, CSS & JavaScript is needed to follow this course"
    description = " Let's practise object oriented programming and use HTML, CSS and plain vanilla JavaScript to build a game. There will be no frameworks and no libraries, because we want deep understanding of how things work under the hood."
    target = "Beginner front end web developers curious about animation and 2D games"
    price = 599
    promotion = 0
    info = "3 hours on-demand video , Access on mobile and TV , Certificate of completion"
    categories = [Development,Web Development,JavaScript]
}

course2 = Course{
    id = "11111112"
    name = "Build 13 Projects with PHP MySQL Bootstrap and PDO"
    short_description = "Build Amazing Projects with PHP MySQL Bootstrap and PDO and Take your Web Development Skills to the Next Level"
    date = "3/2566"
    language = "English"
    purpose = "Learn to Work with APIs"
    chapter = 3
    requirement = "Basic PHP, MySQL and PDO knowledge"
    description = "This course is very digestible and informative and it was created specifically to enhance your coding skills and knowledge not just in PHP and MySQL, but overall in developing web projects."
    target = "Every PHP and MySQL developer who want to advance their skills"
    price = 599
    promotion = 0
    info = "10.5 hours on-demand video,Certificate of completion"
    categories = [Development,Web Development,Bootstrap]
}
