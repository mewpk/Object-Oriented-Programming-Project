import Image from "next/image";
import { StarIcon } from "@heroicons/react/solid";

function CourseCard({ course }) {
  return (
    <div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
      <div>
        <div>
          <Image
            className="h-48 w-full object-cover"
            src="https://fireship.io/courses/react-next-firebase/img/featured.png"
            alt={course._name}
            width={1000}
            height={1000}
          />
        </div>
        <div className="p-8">
          <div className="uppercase tracking-wide text-sm text-indigo-500 font-semibold">
            {course._categories[0]}
          </div>
          <a href="#" className="block mt-1 text-lg leading-tight font-medium text-black hover:underline">
            {course._name}
          </a>
          <div className="mt-2 flex items-center text-sm text-gray-500">
            <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
            <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
            <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
            <StarIcon className="h-5 w-5 text-yellow-500 mr-1" />
            <StarIcon className="h-5 w-5 text-gray-400" />
            <span className="ml-2">{Math.floor(Math.random() * 100)} reviews</span>
          </div>
          <p className="mt-2 text-gray-500">{course._short_description}</p>
          <div className="mt-3 flex items-center">
            <span className="text-gray-500 text-sm font-medium">${course._price.toFixed(2)}</span>
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

export default function CourseList( props) {
    const courses = props.courses
  return (
    <div className="grid grid-cols-1 gap-10 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
      {courses && courses.map((course) => (
        <CourseCard key={course._id} course={course} />
      ))}
    </div>
  );
}
