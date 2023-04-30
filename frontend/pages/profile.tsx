import React, { useEffect, useState } from "react";
import Image from "next/image";
import { useCookies } from "react-cookie";
import Router from "next/router";
export default function Profile() {
  const [cookies, setCookie, removeCookie] = useCookies(["user"]);
  const [username, setUsername] = useState(null);

  const [user, setUser] = useState({
    _name: "",
    _language: "",
    _about: "",
  });

  const getUserProfile = async () => {
    const res = await fetch("http://localhost:8000/user", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user,
      }),
    });
    const data = await res.json();
    console.log(data);
    setUser(data);
  };

  useEffect(() => {
    setUsername(cookies.user);
  }, [cookies]);

  useEffect(() => {
    getUserProfile();
  }, [username]);

  useEffect(()=>{
    if (!cookies.user){
      Router.push("/")
    }
  })
  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="max-w-sm mx-auto bg-white shadow-lg rounded-lg overflow-hidden  pt-10 hover:shadow-xl">
        <div className="relative h-40 w-full">
          <div className="avatar ">
            <Image
              src="https://img.freepik.com/free-icon/user_318-159711.jpg"
              alt={`${user._name}'s profile picture`}
              layout="fill"
              objectFit="contain"
            />
          </div>
        </div>
        <div className="py-6 px-4">
          <h1 className="text-2xl font-bold">Name : {user._name}</h1>
          <h2 className="text-lg font-semibold text-gray-600">
            Language : {user._language}
          </h2>
          <p className="text-gray-700 mt-2">About : {user._about}</p>
        </div>
        <div className="py-2 px-4 flex justify-center">
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
            // onClick={handleEditProfile}
          >
            Edit Profile
          </button>
        </div>
      </div>
    </div>
  );
}
