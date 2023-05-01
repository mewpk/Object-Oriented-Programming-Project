import React, { useEffect, useState } from "react";
import Image from "next/image";
import { useCookies } from "react-cookie";
import Router from "next/router";

export default function Profile() {
  const [cookies, setCookie, removeCookie] = useCookies(["user"]);
  const [username, setUsername] = useState(null);
  const [isEditing, setIsEditing] = useState(false);

  const [user, setUser] = useState({
    _name: "Anonymous",
    _language: "Anonymous",
    _about: "Anonymous",
  });

  const [name, setName] = useState(user._name);
  const [language, setLanguage] = useState(user._language);
  const [about, setAbout] = useState(user._about);

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
    if (data) {
      setUser(data);
      setName(data._name);
      setLanguage(data._language);
      setAbout(data._about);
    }
  };

  const handleEditProfile = () => {
    setIsEditing(true);
  };

  const handleSaveProfile = async () => {
    const res = await fetch("http://localhost:8000/edit_profile", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user,
        name,
        language,
        about,
      }),
    });
    const data = await res.json();
    console.log(data);
    if (data) {
      setUser({
        _name: name,
        _language: language,
        _about: about,
      });
      setIsEditing(false);
    }
  };

  useEffect(() => {
    setUsername(cookies.user);
  }, [cookies]);

  useEffect(() => {
    getUserProfile();
  }, [username]);

  useEffect(() => {
    if (!cookies.user) {
      Router.push("/");
    }
  });

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="max-w-sm w-2/4  mx-auto bg-white shadow-lg rounded-lg overflow-hidden p-10  pt-10 hover:shadow-xl">
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
          {isEditing ? (
            <>
              <div className="flex flex-col mb-4">
                <label
                  className="font-semibold text-gray-600 text-sm"
                  htmlFor="name"
                >
                  Name
                </label>
                <input
                  className="border border-gray-400 p-2 rounded-lg"
                  type="text"
                  name="name"
                  id="name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                />
              </div>
              <div className="flex flex-col mb-4">
                <label
                  className="font-semibold text-gray-600 text-sm"
                  htmlFor="language"
                >
                  Language
                </label>
                <input
                  className="border border-gray-400 p-2 rounded-lg"
                  type="text"
                  name="language"
                  id="language"
                  value={language}
                  onChange={(e) => setLanguage(e.target.value)}
                />
              </div>
              <div className="flex flex-col mb-4">
                <label
                  className="font-semibold text-gray-600 text-sm"
                  htmlFor="about"
                >
                  About
                </label>
                <textarea
                  className="border border-gray-400 p-2 rounded-lg"
                  name="about"
                  id="about"
                  value={about}
                  onChange={(e) => setAbout(e.target.value)}
                ></textarea>
              </div>
            </>
          ) : (
            <>
              <h1 className="text-2xl font-bold">Name : {user._name}</h1>
              <h2 className="text-lg font-semibold text-gray-600">
                Language : {user._language}
              </h2>
              <p className="text-gray-700 mt-2">About : {user._about}</p>
            </>
          )}
        </div>
        <div className="py-2 px-4 flex justify-center">
          {isEditing ? (
            <>
              <button
                className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mr-2"
                onClick={handleSaveProfile}
              >
                Save
              </button>
              <button
                className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
                onClick={() => setIsEditing(false)}
              >
                Cancel
              </button>
            </>
          ) : (
            <button
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
              onClick={handleEditProfile}
            >
              Edit Profile
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
