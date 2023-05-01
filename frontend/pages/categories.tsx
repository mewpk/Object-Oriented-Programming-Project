import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";
import Image from "next/image";
import Modal from "react-modal";


export default function Categories() {
  const [cookies] = useCookies(["user"]);
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const modalStyles = {
    content: {
      top: "50%",
      left: "50%",
      right: "auto",
      bottom: "auto",
      marginRight: "-50%",
      transform: "translate(-50%, -50%)",
    },
  };

  const [isModalOpen, setIsModalOpen] = useState(false);

  const getCategories = async () => {
    const res = await fetch("http://localhost:8000/category");
    const data = await res.json();
    console.log(data);
    setCategories(data);
  };

  const   handleCategoryClick = (category) => {
    setSelectedCategory(category);
    setIsModalOpen(true);
  };


  useEffect(() => {
    getCategories();
  }, []);

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="max-w-200 mx-auto">
        <h1 className="text-3xl font-bold mt-6 mb-6">Categories</h1>
        <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
          {categories.map((category) => ( 
            <div
              key={category._Categories__name}
              className="bg-white shadow-lg rounded-lg overflow-hidden hover:shadow-xl cursor-pointer p-3 text-center"
              onClick={() => handleCategoryClick(category)}
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
                <h2 className="text-lg font-semibold">{category._Categories__name}</h2>
              </div>
            </div>
          ))}
        </div>
      </div>
      {isModalOpen && (
        <Modal
          isOpen={isModalOpen}
          onRequestClose={() => setIsModalOpen(false)}
          style={modalStyles}
        >
          <h2>Modal Title</h2>
          <p>Modal content goes here.</p>
          <button onClick={() => setIsModalOpen(false)}>Close Modal</button>
        </Modal>
      )}
    </div>
  );
}
