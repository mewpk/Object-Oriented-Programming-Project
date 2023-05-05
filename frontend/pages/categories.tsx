import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";
import Image from "next/image";
import Modal from "react-modal";
import CourseList from "../components/CourseList";

export default function Categories() {
  const [cookies] = useCookies(["user"]);
  const [categories, setCategories] = useState([]);


  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isCourseOpen, setIsCourseOpen] = useState(false);
  const getCategories = async () => {
    const res = await fetch("http://localhost:8000/category");
    const data = await res.json();
    console.log(data);
    setCategories(data);
  };

  const handleCategoryClick = (category) => {
    setIsModalOpen(true);
    getData(category);
  };

  useEffect(() => {
    getCategories();
  }, []);

  const [data, setData] = useState([]);
  const getData = async (category) => {
    const res = await fetch("http://localhost:8000/course/search_by_category", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        category_name: category,
      }),
    });
    let dataRes = await res.json();
    setData(dataRes);
    console.log(dataRes);
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="max-w-200 mx-auto">
        <h1 className="text-3xl font-bold mt-6 mb-6">Categories</h1>
        <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
          {categories.map((category) => (
            <div
              key={category._Categories__name}
              className="bg-white shadow-lg rounded-lg overflow-hidden hover:shadow-xl cursor-pointer p-3 text-center"
              onClick={() => handleCategoryClick(category._Categories__name)}
            >
              <div className="relative h-56 w-56 mx-auto">
                <div className="category-image">
                  <Image
                    src="https://cdn.iconscout.com/icon/free/png-256/free-documents-390-1120791.png"
                    alt={`${category._Categories__name} category image`}
                    layout="fill"
                    objectFit="cover"
                  />
                </div>
              </div>
              <div className="py-4 px-6">
                <h2 className="text-lg font-semibold">
                  {category._Categories__name}
                </h2>
              </div>
            </div>
          ))}
        </div>
      </div>
      {isModalOpen && (
        <Modal
          isOpen={isModalOpen}
          onRequestClose={() => {
            setIsModalOpen(false);
            setIsCourseOpen(false);
          }}
          className="w-auto  bg-white grid h-screen place-items-center"
          
        >
          <div onClick={() => setIsCourseOpen(true)} >
            <CourseList courses={data} />
          </div>
          <button
              onClick={() => {
                setIsModalOpen(false)
              }}
              type="button"
              className={`hover:animate-pulse w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-10 py-5 bg-red-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:ml-3 sm:w-auto sm:text-sm `}
            >
              Close
            </button>
        </Modal>
      )}
    </div>
  );
}
