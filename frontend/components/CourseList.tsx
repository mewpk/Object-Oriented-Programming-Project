import { useEffect, useState } from "react";
import Image from "next/image";
import { StarIcon ,HeartIcon } from "@heroicons/react/solid";
import { useCookies } from "react-cookie";
import { useRouter } from "next/navigation";

function CourseCard({ course, onCardClick }: any) {
  const [cookies, setCookie, removeCookie] = useCookies(["user","role"]);
  const [checkWishList, setCheckWishList] = useState(false);
  const getData = async () => {
    const res = await fetch("http://localhost:8000/check_course_in_favorite", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user,
        course_id: course._id,
      }),
    });
    let dataRes = await res.json();
    if(cookies.user){
      setCheckWishList(dataRes.status);
    }
    
    console.log(dataRes);
  };

  useEffect(() => {
    getData();
  }, []);


  
  return (
    <div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl hover:shadow-xl  hover:scale-105 duration-500">
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
            {course._average_rating == 0 && (
              <>
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400" />
              </>
            )}
            {course._average_rating > 0 && course._average_rating <= 1 && (
              <>
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400" />
              </>
            )}
            {course._average_rating > 1 && course._average_rating <= 2 && (
              <>
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400" />
              </>
            )}
            {course._average_rating > 2 && course._average_rating <= 3 && (
              <>
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400" />
              </>
            )}
            {course._average_rating > 3 && course._average_rating <= 4 && (
              <>
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400" />
              </>
            )}
            {course._average_rating > 4 && (
              <>
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500" />
              </>
            )}

            <span className="ml-2">{course._review.length} reviews</span>
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
           <HeartIcon className={`${ cookies.role === "Student" && cookies.user && checkWishList ? "h-8 w-8 text-red-400 ml-auto" : `h-8 w-8 text-gray-400 ml-auto` }`} />
          </div>
        </div>
      </div>
    </div>
  );
}

function CourseModal({ course, onClose, AddToCart }) {
  const [cookies, setCookie, removeCookie] = useCookies(["user","role"]);
  const [checkCourse, setCheckCourse] = useState(null);
  const [checkWishList, setCheckWishList] = useState(null);
  const router = useRouter();

  const check_course_in_cart = async () => {
    const res = await fetch("http://localhost:8000/check_course_in_cart", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user,
        course_id: course._id,
      }),
    });
    let dataRes = await res.json();
    setCheckCourse(dataRes.status);
    console.log(dataRes);
  };

  const check_course_in_favorite = async () => {
    const res = await fetch("http://localhost:8000/check_course_in_favorite", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user,
        course_id: course._id,
      }),
    });
    let dataRes = await res.json();
    setCheckWishList(dataRes.status);
    console.log(dataRes);
  };

  const sendDataCart = async () => {
    const res = await fetch("http://localhost:8000/remove_course_from_cart", {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user,
        course_id: course._id,
      }),
    });
    let dataRes = await res.json();
    setCheckCourse(dataRes);
    console.log(dataRes);
  };

  const sendDataWishList = async () => {
    const res = await fetch("http://localhost:8000/add_to_favorite", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user,
        course_id: course._id,
      }),
    });
    let dataRes = await res.json();
    setCheckWishList(dataRes.status);
    console.log(dataRes);
    router.refresh();
  };
 

  const removeCorseInCart = () => {
    if (!checkCourse) {
      sendDataCart();
    }
  };
 

  useEffect(() => {
    check_course_in_favorite();
    check_course_in_cart();
  }, []);



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
                  className="text-lg leading-6 font-medium text-gray-900 flex"
                  id="modal-headline"
                >
                  {course._name}
                  <HeartIcon onClick={sendDataWishList} className={`hover:animate-pulse duration-500 hover:-translate-y-1 hover:scale-110 ${ cookies.role === "Student" && cookies.user && checkWishList ?  "h-8 w-8 text-red-400 ml-auto " : `h-8 w-8 text-gray-400 ml-auto`} ${cookies.role === "Student" && cookies.user ? "block" : "hidden"}`} />
                  
                </h3>
                <div className="mt-2">
                  <p className="text-sm text-gray-500 ">
                    {course._categories[0]}
                   
                  </p>
                  
                  <div className="mt-2 flex items-center text-sm text-gray-500">
                  {course._average_rating == 0 && (
              <>
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400" />
              </>
            )}
            {course._average_rating > 0 && course._average_rating <= 1 && (
              <>
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400" />
              </>
            )}
            {course._average_rating > 1 && course._average_rating <= 2 && (
              <>
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400" />
              </>
            )}
            {course._average_rating > 2 && course._average_rating <= 3 && (
              <>
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400" />
              </>
            )}
            {course._average_rating > 3 && course._average_rating <= 4 && (
              <>
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-gray-400" />
              </>
            )}
            {course._average_rating > 4 && (
              <>
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
                <StarIcon className="h-5 w-5 text-yellow-500" />
              </>
            )}
                    <span className="ml-2">
                      {course._review.length} reviews
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
              className="hover:animate-pulse w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto sm:text-sm"
            >
              Close
            </button>

            <button
              onClick={() => {
                onClose();
                AddToCart(course._id);
              }}
              type="button"
              className={`hover:animate-pulse w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm ${
                cookies.role === "Student" && cookies.user && checkCourse ? "block" : "hidden"
              }`}
            >
              Add To Cart
            </button>
            <button
              onClick={() => {
                onClose();
                removeCorseInCart();
              }}
              type="button"
              className={`hover:animate-pulse w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-red-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:ml-3 sm:w-auto sm:text-sm ${
                cookies.role === "Student" && cookies.user && !checkCourse ? "block" : "hidden"
              }`}
            >
              Remove From Cart
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

  const addToCart = (course_id) => {
    fetchData(course_id);
  };

  const fetchData = async (course_id) => {
    const res = await fetch("http://localhost:8000/add_cart", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user,
        course_id: course_id,
      }),
    });
    const data = await res.json();
    console.log(data);
  };

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
        <CourseModal
          course={selectedCourse}
          onClose={handleCloseModal}
          AddToCart={addToCart}
        />
      )}
    </div>
  );
}
