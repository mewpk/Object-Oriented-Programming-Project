import { useState } from "react";
import Image from "next/image";
import { StarIcon } from "@heroicons/react/solid";
import { useCookies } from "react-cookie";

function CourseCard({ course, onCardClick }: any) {
  return (
    <div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
      <div>
        <button
          className="w-full h-48 focus:outline-none"
          // onClick={() => onCardClick(course)}
        >
          <Image
            className="h-full w-full object-cover"
            src={course._image}
            alt={course._name}
            width={1000}
            height={1000}
          />
        </button>
        <div className="p-8">
          <div className="uppercase tracking-wide text-sm text-indigo-500 font-semibold">
            {course._categories[0]}
          </div>
          <a
            href="#"
            className="block mt-1 text-lg leading-tight font-medium text-black hover:underline"
          >
            {course._name}
          </a>
          <div className="mt-2 flex items-center text-sm text-gray-500">
            <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
            <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
            <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
            <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
            <StarIcon className="h-5 w-5 text-gray-400" />
            <span className="ml-2">
              {Math.floor(Math.random() * 100)} reviews
            </span>
          </div>
          <p className="mt-2 text-gray-500">{course._short_description}</p>
          <div className="mt-3 flex items-center">
            <span className="text-gray-500 text-sm font-medium">
              ${course._price.toFixed(2)}
            </span>
            {course._promotion && (
              <span className="ml-2 bg-green-100 text-green-800 text-xs font-medium px-2 py-1 rounded-full">
                On Sale
              </span>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

function CourseModal({ course, onClose , AddToCart }) {
  const [cookies, setCookie, removeCookie] = useCookies(["user"]);
  return (
    <div className="fixed z-10 inset-0 overflow-y-auto">
      <div className="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div className="fixed inset-0 transition-opacity">
          <div className="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>
        <span className="hidden sm:inline-block sm:align-middle sm:h-screen"></span>
        <div
          className="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"
          role="dialog"
          aria-modal="true"
          aria-labelledby="modal-headline"
        >
          <div className="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div className="sm:flex sm:items-start">
              <div className="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                <h3
                  className="text-lg leading-6 font-medium text-gray-900"
                  id="modal-headline"
                >
                  {course._name}
                </h3>
                <div className="mt-2">
                  <p className="text-sm text-gray-500">
                    {course._categories[0]}
                  </p>
                  <div className="mt-2 flex items-center text-sm text-gray-500">
                    <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                    <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                    <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                    <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                    <StarIcon className="h-5 w-5 text-gray-400" />
                    <span className="ml-2">
                      {Math.floor(Math.random() * 100)} reviews
                    </span>
                  </div>
                  <p className="mt-3 text-base text-gray-500">
                    {course._description}
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div className="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button
              onClick={onClose}
              type="button"
              className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto sm:text-sm"
            >
              Close
            </button>
          
            <button
              onClick={()=>{
                onClose()
                AddToCart(course._id);
              }}
              type="button"
              className={`w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto sm:text-sm ${ cookies.user ? "block" : "hidden"}`}
            >
              Add To Cart
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
export default function CourseList({ courses }) {
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [cookies, setCookie, removeCookie] = useCookies(["user"]);

  const handleCardClick = (course) => {
    setSelectedCourse(course);
  };

  const handleCloseModal = () => {
    setSelectedCourse(null);
  };
  
  const addToCart = (course_id)=>{
    fetchData(course_id)
  }

  const fetchData = async (course_id) => {
    const res = await fetch("http://localhost:8000/add_cart", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user,
        course_id : course_id
      }),
    });
    const data = await res.json();
    console.log(data);
  }

  return (
    <div className="grid grid-cols-1 gap-10 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
      {courses &&
        courses.map((course) => (
          <div
            key={course._id}
            onClick={() => handleCardClick(course)}
            className="cursor-pointer"
          >
            <CourseCard course={course} />
          </div>
        ))}
      {selectedCourse && (
        <CourseModal course={selectedCourse} onClose={handleCloseModal} AddToCart={addToCart} />
      )}
    </div>
  );
}
