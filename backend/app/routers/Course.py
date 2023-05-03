from fastapi import APIRouter, Body
from ..config.database import course_collection
from ..models.Course import Course 
from ..models.CourseChapter import CourseChapter
from ..models.Promotion import Promotion
from datetime import datetime

router = APIRouter()
@router.get("/mockcourse")
async def mock_course():
    categories = {
    "0": "OOP",
    "1": "Algorithms",
    "2": "Data Structures",
    "3": "Artificial Intelligence",
    "4": "Machine Learning",
    "5": "Deep Learning",
    "6": "Computer Vision",
    "7": "Natural Language Processing",
    "8": "Neural Networks",
    "9": "Big Data",
    "10": "JavaScript",
    "11": "Python",
    "12": "C",
    "13": "Data Science",
    "14": "Blockchain",
    "15": "Cybersecurity",
    "16": "Ethical Hacking",
    "17": "Penetration Testing",
    "18": "Computer Networking",
    "19": "Cloud Computing",
    "20": "DevOps",
    "21": "Docker",
    "22": "C++",
    "23": "Linux",
    "24": "Unix",
    "25": "Windows Server",
    "26": "Database Design",
    "27": "SQL",
    "28": "Oracle",
    "29": "MySQL",
    "30": "PostgreSQL",
    "31": "MongoDB",
    "32": "Cryptography",
    "33": "Operating Systems",
    "34": "Virtualization",
    "35": "CompTIA",
    "36": "Cisco",
    "37": "Microsoft",
    "38": "Java",
    "39": "Web development",
    "40": "IT Certification",
    "41": "Software Engineering",
    "42": "App development",
    "43": "Scrum",
    "44": "Project Management",
    "45": "Business Analysis",
    "46": "Data Analysis",
    "47": "Excel",
    "48": "Power BI",
    "49": "Tableau",
    "50": "SAP",
    }
    course_1 =Course(
    id = len(course_collection.courses)+1,  
    name = "Introduction to Cybersecurity",
    short_description="Learn the basics of cybersecurity",    
    date = datetime.now(),
    language="English",
    purpose="The purpose of this course is to provide an introduction to the world of cybersecurity and to teach students about the various threats that exist in the digital world.",
    chapters  = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="No prior knowledge required",
    description="This course covers the basics of cybersecurity and is intended for anyone who wants to learn more about this field.",
    target="The target audience for this course is anyone who wants to learn about cybersecurity.",
    price=199,
    info="This course covers the fundamentals of cybersecurity.",
    categories=["Cybersecurity","Cryptography","Penetration Testing"],
    instructor="Pookkie Eiei"
    )
    course_collection.add_course(course_1)

    course_2 = Course( 
    id = len(course_collection.courses)+1,
    name = "Machine Learning for Business",
    short_description="Learn how to use machine learning in business",   
    date = datetime.now(),
    language="English",
    purpose="The purpose of this course is to teach students how to use machine learning techniques to solve business problems.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="Basic programming knowledge is required",
    description="This course covers the basics of machine learning and how it can be applied in a business context.",
    target="The target audience for this course is business professionals who want to learn how to use machine learning in their work.",
    price=299,
    info="This course covers the basics of machine learning in a business context.",
    categories=["Machine Learning", "Business"],
    instructor="Pookkie Eiei"
    )
    course_collection.add_course(course_2)

    course_3 = Course(
    id = len(course_collection.courses)+1,
    name="Introduction to SQL",
    short_description="Learn the basics of SQL",
    date = datetime.now(),
    language="English",
    purpose="The purpose of this course is to teach students the basics of SQL, including how to query a database and manipulate data.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="No prior knowledge required",
    description="This course covers the basics of SQL and is intended for anyone who wants to learn how to work with databases.",
    target="The target audience for this course is anyone who wants to learn about SQL and how to work with databases.",
    price=149,
    info="This course covers the fundamentals of SQL.",
    categories=["SQL", "Database Design"],
    instructor="Pookkie Eiei"   
    )
    course_collection.add_course(course_3)

    course_4 = Course(
    id = len(course_collection.courses)+1,
    name="Introduction to JavaScript",
    short_description="Learn the basics of JavaScript",
    date = datetime.now(),
    language="English",
    purpose="The purpose of this course is to teach students the basics of JavaScript, including how to write scripts and manipulate the DOM.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="No prior knowledge required",
    description="This course covers the basics of JavaScript and is intended for anyone who wants to learn how to add interactivity to websites.",
    target="The target audience for this course is anyone who wants to learn about JavaScript and how to add interactivity to websites.",
    price=99,
    info="This course covers the fundamentals of JavaScript.",
    categories=["JavaScript", "Web Development"],
    instructor="lnw Pat"
    )
    course_collection.add_course(course_4)

    course_5 = Course(
    id = len(course_collection.courses)+1,
    name="Introduction to Artificial Intelligence",
    short_description="Learn the basics of AI",
    date = datetime.now(),
    language="English",
    purpose="This course will teach you the fundamental concepts of artificial intelligence, including machine learning and natural language processing.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="Basic knowledge of a programming language and mathematics",
    description="In this course, you will learn how to use machine learning and natural language processing techniques to create intelligent systems.",
    target="This course is suitable for beginner and intermediate programmers who want to learn about artificial intelligence.",
    price=200,
    info="This course covers the essential concepts of artificial intelligence.",
    categories=["Artificial Intelligence", "Machine Learning", "Natural Language Processing", "Python"],
    instructor="lnw Pat"
    )
    course_collection.add_course(course_5)


    course_6 = Course(
    id = len(course_collection.courses)+1,
    name="Introduction to Object-Oriented Programming",
    short_description="Learn the basics of OOP",
    date = datetime.now(),
    language="English",
    purpose="This course will teach you the fundamental concepts of object-oriented programming, including encapsulation, inheritance, and polymorphism.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="Basic knowledge of a programming language",
    description="In this course, you will learn how to write code using the principles of object-oriented programming, and how to create classes and objects that represent real-world entities.",
    target="This course is suitable for beginner and intermediate programmers who want to learn OOP.",
    price=150,
    info="This course covers the essential concepts of object-oriented programming.",
    categories=["OOP", "Java", "Python"],
    instructor="Mew kuki"
    )
    course_collection.add_course(course_6)

    course_7 = Course(
    id = len(course_collection.courses)+1,
    name="Algorithms and Data Structures",
    short_description="Learn to design and analyze algorithms and data structures",
    date = datetime.now(),
    language="English",
    purpose="This course will teach you how to design and analyze algorithms and data structures using a variety of techniques.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="Basic knowledge of a programming language and mathematics",
    description="In this course, you will learn how to design and analyze algorithms and data structures using a variety of techniques, including dynamic programming, greedy algorithms, and divide-and-conquer.",
    target="This course is suitable for intermediate and advanced programmers who want to learn more about algorithms and data structures.",
    price=250,
    info="This course covers the essential concepts of algorithms and data structures.",
    categories=["Algorithms", "Data Structures", "Java", "Python"],
    instructor="Mew kuki")
    course_collection.add_course(course_7)

    course_8 = Course(
    id = len(course_collection.courses)+1,
    name="The Basics of C++ Programming",
    short_description="Learn the basics of C++ programming language and its applications",
    date = datetime.now(),
    language="English",
    purpose="The purpose of this course is to introduce students to the C++ programming language and its applications in various fields.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="Basic knowledge of a programming language",
    description="In this course, you will learn the basics of C++ programming language, including data types, control structures, functions, arrays, pointers, and object-oriented programming concepts.",
    target="This course is suitable for beginners who want to learn the basics of C++ programming language.",
    price=150,
    info="This course covers the essential concepts of C++ programming language.",
    categories=["C++", "Programming Languages"],
    instructor="Mew kuki"
    )
    course_collection.add_course(course_8)
    
    course_9 = Course(
    id = len(course_collection.courses)+1,
    name="Big Data Analytics",
    short_description="Learn techniques and tools for analyzing large datasets",
    date = datetime.now(),
    language="English",
    purpose="This course will teach you the techniques and tools used to analyze large datasets and extract useful insights.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="Basic knowledge of programming and statistics",
    description="In this course, you will learn how to work with big data and use tools like Hadoop, Spark, and Hive to analyze large datasets. You will also learn about data mining, machine learning, and other techniques for extracting useful insights from big data.",
    target="This course is suitable for anyone interested in working with big data, including data analysts, data scientists, and software engineers.",
    price=300,
    info="This course covers the essential techniques and tools for analyzing big data.",
    categories=["Big Data", "Data Analysis"],
    instructor="Mew kuki"
    )
    course_collection.add_course(course_9)

    course_10 = Course(
    id = len(course_collection.courses)+1,
    name="Introduction to Cloud Computing",
    short_description="Get an overview of cloud computing and its applications",
    date = datetime.now(),
    language="English",
    purpose="This course will provide you with an overview of cloud computing concepts and services and their applications in various fields.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="Basic knowledge of computer networks and operating systems",
    description="In this course, you will learn about the basics of cloud computing, including its history, deployment models, and service models. You will also learn about popular cloud providers, such as Amazon Web Services, Microsoft Azure, and Google Cloud Platform.",
    target="This course is suitable for anyone interested in learning about cloud computing and its applications, including IT professionals and business leaders.",
    price=200,
    info="This course covers the fundamental concepts of cloud computing and its applications.",
    categories=["Cloud Computing"],
    instructor="Mew kuki"
    )
    course_collection.add_course(course_10)

    course_11 = Course(
    id = len(course_collection.courses)+1,
    name="Cybersecurity Fundamentals",
    short_description="Learn the fundamentals of cybersecurity",
    date = datetime.now(),
    language="English",
    purpose="This course will teach you the fundamental concepts and principles of cybersecurity, including threat intelligence, security policies, and risk management.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="Basic knowledge of computer systems and networks",
    description="In this course, you will learn about the different types of cyber threats and attacks, as well as the methods and technologies used to defend against them. You will also gain an understanding of security policies, risk management strategies, and compliance requirements.",
    target="This course is suitable for anyone interested in learning the fundamentals of cybersecurity, including IT professionals, business leaders, and individuals interested in pursuing a career in cybersecurity.",
    price=400,
    info="This course covers the fundamental concepts and principles of cybersecurity.",
    categories=["Cybersecurity","Ethical Hacking","Cryptography"],
    instructor="Mew kuki"
    )
    course_collection.add_course(course_11)

    course_12 = Course(
    id = len(course_collection.courses)+1,
    name="The Essentials of Computer Networking",
    short_description="Learn the basics of computer networking, including network architecture, protocols, and security.",
    date = datetime.now(),
    language="English",
    purpose="This course is designed to provide students with a solid understanding of computer networking, including the fundamentals of network architecture, protocols, and security.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="Basic knowledge of computer hardware and software",
    description="In this course, you will learn about the basics of computer networking, including network architecture, protocols, and security. You will gain an understanding of different types of networks, such as LANs, WANs, and WLANs, and learn how to set up and configure network devices. You will also learn about network security best practices and common threats, such as viruses, malware, and phishing attacks.",
    target="This course is suitable for anyone interested in learning about computer networking, including IT professionals, network administrators, and students pursuing a career in networking.",
    price=350,
    info="This course provides a solid foundation in the basics of computer networking.",
    categories=["Computer Networking"],
    instructor="Nong Preawa"
    )
    course_collection.add_course(course_12)

    course_13 = Course(
    id = len(course_collection.courses)+1,
    name="Advanced Data Science",
    short_description="Learn advanced techniques for data analysis and machine learning",
    date = datetime.now(),
    language="English",
    purpose="This course will teach you advanced techniques for data analysis and machine learning, including deep learning, natural language processing, and time series analysis.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="Proficiency in Python programming and basic understanding of data analysis and machine learning",
    description="In this course, you will learn advanced techniques for data analysis and machine learning, including deep learning, natural language processing, and time series analysis. You will also gain experience with tools such as TensorFlow and PyTorch, and apply these techniques to real-world datasets.",
    target="This course is suitable for experienced data analysts and machine learning engineers who want to take their skills to the next level.",
    price=500,
    info="This course covers advanced techniques for data analysis and machine learning.",
    categories=["Data Science", "Machine Learning", "Deep Learning", "Natural Language Processing"],
    instructor="Nong Preawa"
    )
    course_collection.add_course(course_13)

    course_14 = Course(
    id = len(course_collection.courses)+1,
    name="Excel for Business Professionals",
    short_description="Learn how to use Excel for business analysis and reporting",
    date = datetime.now(),
    language="English",
    purpose="This course will teach you how to use Excel to analyze and visualize business data. You will learn how to use advanced functions, create charts and pivot tables, and build interactive dashboards.",
    chapters = [CourseChapter(0,"First step ", "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0, "EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,"EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,"EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,"EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,"EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. ", "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                    ],
    requirement="Basic computer skills and knowledge of spreadsheets",
    description="In this course, you will learn how to use Excel to manage, analyze, and visualize business data. You will learn how to use advanced Excel functions, create charts and pivot tables, and build interactive dashboards. You will also learn how to automate tasks with macros and VBA.",
    target="This course is suitable for business professionals who want to enhance their Excel skills and improve their data analysis and reporting capabilities.",
    price=350,
    info="This course covers the advanced Excel functions and techniques used for business data analysis and reporting.",
    categories=["Excel", "Business Analysis"],
    instructor="Nong Preawa"
    )
    course_collection.add_course(course_14)

    for i in range(10):
        course_data = {
            "id" : len(course_collection.courses)+1,
            "name": "Basic " + categories.get(str(i)),
            "short_description": "This is a short description",
            "date" : datetime.now(),
            "language": "English",
            "purpose": "The purpose of this Course is to teach all basic skills about "+ categories.get(str(i)),
            "chapters": [CourseChapter(0,"First step to " + categories.get(str(i)), "https://youtu.be/aZj6VL_9mXg"),
                        CourseChapter(0,categories.get(str(i)) +" EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
                        CourseChapter(0,categories.get(str(i)) +" EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
                        CourseChapter(0,categories.get(str(i)) +" EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
                        CourseChapter(0,categories.get(str(i)) +" EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
                        CourseChapter(0,categories.get(str(i)) +" EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
                        CourseChapter(0,"Final EP. of " + categories.get(str(i)) , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
                        ],
            "requirement": "don't have to learn anything before",
            "description": "This is the full description for " + categories.get(str(i)),
            "target": "The target audience for Course " + categories.get(str(i)) + "is",
            "price": 150,
            "info": "teach about " +categories.get(str(i)),
            "categories": [categories.get(str(i))],
            "instructor": "Nong Preawa"
        }
    
        new_course = Course(
            course_data["id"],
            course_data["name"],
            course_data["short_description"],
            course_data["date"],
            course_data["language"],
            course_data["purpose"],
            course_data["chapters"],
            course_data["requirement"],
            course_data["description"],
            course_data["target"],
            course_data["price"],
            course_data["info"],
            course_data["categories"],
            course_data["instructor"]
        )
        course_collection.add_course(new_course)

    # for i in range(10,20):
    #     course_data = {
    #         "name": "Basic " + categories.get(str(i)),
    #         "short_description": "This is a short description ",
    #         "language": "English",
    #         "purpose": "The purpose of this Course is to teach all basic skills about "+ categories.get(str(i)),
    #         "chapters": [CourseChapter(0,"The Beginning of " + categories.get(str(i)), "https://youtu.be/aZj6VL_9mXg"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
    #                     CourseChapter(0,"Final EP. of " + categories.get(str(i)) , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
    #                     ],
    #         "requirement": "don't have to learn anything before",
    #         "description": "This is the full description for " + categories.get(str(i)),
    #         "target": "The target audience for Course " + categories.get(str(i)) + "is",
    #         "price": 250,
    #         "info": "teach about " +categories.get(str(i)),
    #         "categories": [categories.get(str(i))],
    #         "instructor": "Pookkie Eiei"
    #     }
    
    #     new_course = Course(
    #         course_data["name"],
    #         course_data["short_description"],
    #         course_data["language"],
    #         course_data["purpose"],
    #         course_data["chapters"],
    #         course_data["requirement"],
    #         course_data["description"],
    #         course_data["target"],
    #         course_data["price"],
    #         course_data["info"],
    #         course_data["categories"],
    #         course_data["instructor"]
    #     )
    #     course_collection.add_course(new_course)
    
    # for i in range(20,30):
    #     course_data = {
    #         "name": "Basic " + categories.get(str(i)),
    #         "short_description": "This is a short description",
    #         "language": "English",
    #         "purpose": "The purpose of this Course is to teach all basic skills about "+ categories.get(str(i)),
    #         "chapters": [CourseChapter(0,"The Beginning of " + categories.get(str(i)) , "https://youtu.be/aZj6VL_9mXg"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 1 " , "https://www.youtube.com/watch?v=5dU0tMIp5QM"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 2 " , "https://www.youtube.com/watch?v=2_b9ejo5c-Q"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 6 " , "https://www.youtube.com/watch?v=zC_0xOSX1dY&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 7 " , "https://www.youtube.com/watch?v=kC3Szw7b154&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=2"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 8 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
    #                     CourseChapter(0,"The last EP. of " + categories.get(str(i)) , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
    #                     ],
    #         "requirement": "don't have to learn anything before",
    #         "description": "This is the full description for " + categories.get(str(i)),
    #         "target": "The target audience for Course " + categories.get(str(i)) + "is",
    #         "price": 200,
    #         "info": "teach about " +categories.get(str(i)),
    #         "categories": [categories.get(str(i))],
    #         "instructor": "Mew kuki"
    #     }
    
    #     new_course = Course(
    #         course_data["name"],
    #         course_data["short_description"],
    #         course_data["language"],
    #         course_data["purpose"],
    #         course_data["chapters"],
    #         course_data["requirement"],
    #         course_data["description"],
    #         course_data["target"],
    #         course_data["price"],
    #         course_data["info"],
    #         course_data["categories"],
    #         course_data["instructor"]
    #     )
    #     course_collection.add_course(new_course)
    # for i in range(30,50):
    #     course_data = {
    #         "name": "Basic " + categories.get(str(i)),
    #         "short_description": f"This is a short description for Course {i}.",
    #         "language": "English",
    #         "purpose": "The purpose of this Course is to teach all basic skills about "+ categories.get(str(i)),
    #         "chapters": [CourseChapter(0, "Introduction to " + categories.get(str(i)), "https://youtu.be/aZj6VL_9mXg"),
    #                     CourseChapter(0, categories.get(str(i)) +" EP. 1 ","https://www.youtube.com/watch?v=zC_0xOSX1dY&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W"),
    #                     CourseChapter(0, categories.get(str(i)) +" EP. 2 " , "https://www.youtube.com/watch?v=kC3Szw7b154&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=2"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 3 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 4 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 5 " , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 6 " , "https://www.youtube.com/watch?v=zC_0xOSX1dY&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 7 " , "https://www.youtube.com/watch?v=kC3Szw7b154&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=2"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 8 " , "https://www.youtube.com/watch?v=EhQasD1B_6o&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=3"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 9 " , "https://www.youtube.com/watch?v=DePYgzAhKeI&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=4"),
    #                     CourseChapter(0,categories.get(str(i)) +" EP. 10" , "https://www.youtube.com/watch?v=nRrNES7DO14&list=PLoTScYm9O0GEvHKqqib-AdVFwVe_2ln8W&index=5")
    #                     ],
    #         "requirement": "don't have to learn anything before",
    #         "description": "This is the full description for " + categories.get(str(i)),
    #         "target": "The target audience for Course " + categories.get(str(i)) + "is",
    #         "price": 400,
    #         "info": "teach about " +categories.get(str(i)),
    #         "categories": [categories.get(str(i))],
    #         "instructor": "lnw Pat"
    #     }
    
    #     new_course = Course(
    #         course_data["name"],
    #         course_data["short_description"],
    #         course_data["language"],
    #         course_data["purpose"],
    #         course_data["chapters"],
    #         course_data["requirement"],
    #         course_data["description"],
    #         course_data["target"],
    #         course_data["price"],
    #         course_data["info"],
    #         course_data["categories"],
    #         course_data["instructor"]
    #     )
    #     course_collection.add_course(new_course)
    return course_collection


@router.get("/course")
async def get_course():
    return  course_collection.courses


@router.post("/course/")
async def create_course(course_data: dict = Body(...)):
    try:
        all_chapters = []
        for chapter in course_data.get("chapters"):
            new_chapter = CourseChapter(0,chapter.name,chapter.video)
            all_chapters.append(new_chapter)

        new_course = Course(course_data.get("name"),course_data.get("short_description"),course_data.get("date"),course_data.get("language")
                            ,course_data.get("purpose"),all_chapters,course_data.get("requirement"),course_data.get("description"),course_data.get("target")
                        ,course_data.get("price"),course_data.get("promotion"),course_data.get("info"),course_data.get("categories"),course_data.get("instructor"))
        data = course_collection.add_course(new_course)
        if new_course and data:
            return {"message": "Course created successfully", "course": data}
        else:
            return {"message": "Failed to create course"}
    except:
        return "please try again"
    
@router.post("/course/add_chapter")
async def create_chapter(data: dict = Body(...)):
    try:
        course = course_collection.get_course(data.get("course_id"))
        new_chapter = CourseChapter(0,data.get("name"),data.get("video"))
        course.add_chapter(new_chapter)
        course.promotion.net_promotion_price(course.price)
        return "added chapter successfully"
    except:
        return "please try again"
    
@router.post("/course/add_promotion")
async def create_promotion(data: dict = Body(...)):
    try:
        course = course_collection.get_course(data.get("course_id"))
        new_promotion = Promotion(data.get("percent"),data.get("start_date"),data.get("end_date"),' ')
        course.add_promotion(new_promotion)
        course.promotion.net_promotion_price(course.price)
        return "added promotion successfully"
    except:
        return "please try again"
    
@router.get("/course/search_by_instructor")
async def search_by_instructor(data: dict = Body(...)):
    return  course_collection.search_by_instructor(data.get("instructor_name"))

@router.get("/course/search_by_course")
async def search_by_course(data: dict = Body(...)):    
    return course_collection.search_by_course(data.get("course_name"))

@router.get("/course/search_by_category")
async def search_by_category(data: dict = Body(...)):    
    return course_collection.search_by_category(data.get("category_name"))

@router.get("/home")
async def home():
    return course_collection.sort_by_rating()

