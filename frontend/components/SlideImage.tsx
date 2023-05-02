import Image from "next/image";
import { useState, useEffect } from "react";

const SlideImage = ({ images, autoSlideDelay = 5000 }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const length = images.length;

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCurrentIndex((currentIndex) =>
        currentIndex === length - 1 ? 0 : currentIndex + 1
      );
    }, autoSlideDelay);

    return () => clearInterval(intervalId);
  }, [length, autoSlideDelay]);

  const nextSlide = () => {
    setCurrentIndex((currentIndex) =>
      currentIndex === length - 1 ? 0 : currentIndex + 1
    );
  };

  const prevSlide = () => {
    setCurrentIndex((currentIndex) =>
      currentIndex === 0 ? length - 1 : currentIndex - 1
    );
  };

  return (
    <div className="relative w-full h-96 ">
      {images.map((image, index) => (
        <div
          key={index}
          className={`absolute top-0 left-0 h-full w-full  transition-opacity duration-500 bg-gray-900 ${
            index === currentIndex ? "opacity-100" : "opacity-0" 
          } `}
        >
          <Image src={image.src} alt={image.alt} layout="fill" objectFit="contain" />
        </div>
      ))}
      <button
        className="absolute top-1/2 left-3 bg-white bg-opacity-50 text-gray-800 py-2 px-4 rounded-full transition-opacity duration-500 hover:bg-opacity-75 focus:outline-none"
        onClick={prevSlide}
      >
        &#x2190;
      </button>
      <button
        className="absolute top-1/2 right-3 bg-white bg-opacity-50 text-gray-800 py-2 px-4 rounded-full transition-opacity duration-500 hover:bg-opacity-75 focus:outline-none"
        onClick={nextSlide}
      >
        &#x2192;
      </button>
    </div>
  );
};

export default SlideImage;
