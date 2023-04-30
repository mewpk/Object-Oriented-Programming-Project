import Link from 'next/link';
import { useEffect, useState } from 'react';
import { useCookies } from 'react-cookie';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [cookies, setCookie, removeCookie] = useCookies(['user']);
  const [username , setUsername] = useState("")
  
  useEffect(()=>{
    setUsername(cookies.user)
  })
    return (
        <nav className="bg-gray-900 shadow">
            <div className="container mx-auto px-6 py-4">
                <div className="flex items-center justify-between">
                    <div className="hidden md:flex ">
                        <Link legacyBehavior href="/">
                            <a className="text-gray-200 text-sm hover:font-bold hover:text-yellow-200  py-2 px-4 mr-4">Udemy</a>
                        </Link>
                        <Link legacyBehavior href="/courses">
                            <a className="text-gray-200 hover:text-yellow-200  hover:font-bold text-sm py-2 px-4">Courses</a>
                        </Link>
                        <Link legacyBehavior href="/categories">
                            <a className="text-gray-200 hover:text-yellow-200  hover:font-bold text-sm py-2 px-4">Categories</a>
                        </Link>
                        <Link legacyBehavior href="/cart">
                            <a className="text-gray-200 hover:text-yellow-200  hover:font-bold text-sm py-2 px-4">Cart</a>
                        </Link>
                        <Link legacyBehavior href="/mycourse">
                            <a className="text-gray-200 hover:text-yellow-200  hover:font-bold text-sm py-2 px-4">My Courses</a>
                        </Link>
                        <Link legacyBehavior href="/addcourse">
                            <a className="text-gray-200 hover:text-yellow-200  hover:font-bold text-sm py-2 px-4">Add Courses</a>
                        </Link>
                    </div>
                    <div className="md:hidden">
            <button
              type="button"
              className="block text-gray-800 hover:text-gray-700 focus:text-gray-700 focus:outline-none"
              aria-label="toggle menu"
              onClick={() => setIsOpen(!isOpen)}
            >
              <svg viewBox="0 0 24 24" className="h-6 w-6 fill-current">
                <path
                  fillRule="evenodd"
                  clipRule="evenodd"
                  d="M3 6C2.44772 6 2 6.44772 2 7C2 7.55228 2.44772 8 3 8H21C21.5523 8 22 7.55228 22 7C22 6.44772 21.5523 6 21 6H3ZM3 12C2.44772 12 2 12.4477 2 13C2 13.5523 2.44772 14 3 14H21C21.5523 14 22 13.5523 22 13C22 12.4477 21.5523 12 21 12H3ZM3 18C2.44772 18 2 18.4477 2 19C2 19.5523 2.44772 20 3 20H21C21.5523 20 22 19.5523 22 19C22 18.4477 21.5523 18 21 18H3Z"
                />
              </svg>
            </button>
          </div>
                    <div className="hidden md:flex">
                        <Link legacyBehavior href="/login">
                            <a className={`text-gray-200 hover:text-yellow-200  hover:font-bold text-sm py-2 px-4 ${!username ? 'block' : 'hidden'}`}>Log in</a>
                        </Link>
                        <Link legacyBehavior href="/register">
                            <a className={`bg-yellow-400 hover:bg-yellow-500 text-gray-200 hover:font-bold text-sm py-2 px-4 rounded ml-4 ${!username ? 'block' : 'hidden'}`}>
                                Sign up
                            </a>
                        </Link>
                    </div>
                </div>
            </div>
            <div className={`md:hidden ${isOpen ? 'block' : 'hidden'}`}>
                <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                    <Link legacyBehavior href="/">
                        <a className="text-gray-200 hover:text-yellow-200  hover:font-bold text-sm block py-2 px-4">Home</a>
                    </Link>
                    <Link legacyBehavior href="/courses">
                        <a className="text-gray-200 hover:text-yellow-200  hover:font-bold text-sm block py-2 px-4">Courses</a>
                    </Link>
                    <Link legacyBehavior href="/categories">
                        <a className="text-gray-200 hover:text-yellow-200  hover:font-bold text-sm block py-2 px-4">Categories</a>
                    </Link>
                    <Link legacyBehavior href="/cart">
                        <a className="text-gray-200 hover:text-yellow-200  hover:font-bold text-sm block py-2 px-4">Cart</a>
                    </Link>
                    <Link legacyBehavior href="/mycourse">
                        <a className="text-gray-200 hover:text-yellow-200  hover:font-bold text-sm block py-2 px-4">My Courses</a>
                    </Link>
                    <hr className="border-t border-gray-200 my-3" />
                    <Link legacyBehavior href="/login">
                        <a className={`text-gray-200 hover:text-yellow-200  hover:font-bold text-sm block py-2 px-4 ${!username ? 'block' : 'hidden'}`}>Log in</a>
                    </Link>
                    <Link legacyBehavior href="/register">
                        <a className={`bg-yellow-600 hover:bg-yellow-500 text-white hover:text-gray-300 hover:font-bold text-sm block py-2 px-4 rounded ${!username ? 'block' : 'hidden'}`}>
                            Sign up
                        </a>
                    </Link>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;  
