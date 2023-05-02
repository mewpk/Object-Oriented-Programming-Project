import Router from "next/router";
import { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

const AdminVerifyInstructor = () => {
  const [instructors, setInstructors] = useState([]);
  const [cookies, setCookie, removeCookie] = useCookies(["user" , "role"]);
  const getData = async () => {
    const res = await fetch("http://localhost:8000/instructors", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });
    let dataRes = await res.json();
    console.log(dataRes);
    try {
      setInstructors(dataRes);
    } catch (error) {
      console.log(error);
    }
  };

  const sendData1 = async (username) => {
    const res = await fetch("http://localhost:8000/verify_instructor", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: username,
        
      }),

    });
    let dataRes = await res.json();
    console.log(dataRes);
  };
  const sendData2 = async (username) => {
    const res = await fetch("http://localhost:8000/unverify_instructor", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: username,
        
      }),

    });
    let dataRes = await res.json();
    console.log(dataRes);
  };

  useEffect(() => {
    getData();
    if (!cookies.user || cookies.role !== "Admin") {
        Router.push("/");
      }
  }, []);

  const handleVerify = (username) => {
    // Call API to update instructor verification status
    console.log(username)
    sendData1(username)
    getData();
  };

  const handleUnverify = (username) => {
    // Call API to update instructor verification status
    console.log(username)
    sendData2(username)
    getData();
  };

  return (
    <div className="container mx-auto p-10">
      <h1 className="text-3xl font-bold mt-6 mb-6 text-center">Admin Verify Instructor</h1>
      <div className="bg-white shadow-md rounded-lg p-4">
        {instructors &&
          instructors.map((instructor) => {
            return (
              <div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl hover:shadow-xl  hover:scale-105 duration-500 p-10 mb-10" key={instructor._username}>
                <h2 className="text-lg font-semibold mb-2">
                  {instructor._name}
                </h2>
                <p className="text-gray-600 mb-4">{instructor._email}</p>
                {instructor._Instructor__verify ? (
                  <div className="flex items-center">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      className="h-6 w-6 text-green-500 mr-2"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2}
                        d="M5 13l4 4L19 7"
                      />
                    </svg>
                    <p className="text-green-500">Verified Instructor</p>
                    <button
                      className="ml-auto px-2 py-1 rounded-lg bg-red-500 text-white"
                      onClick={()=>{
                        handleUnverify(instructor._username)
                    }}
                    >
                      Unverify
                    </button>
                  </div>
                ) : (
                  <div className="flex items-center">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      className="h-6 w-6 text-gray-500 mr-2"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2}
                        d="M5 13l4 4L19 7"
                      />
                    </svg>
                    <p className="text-gray-500">Not Verified</p>
                    <button
                      className="ml-auto px-2 py-1 rounded-lg bg-green-500 text-white"
                      onClick={()=>{
                        handleVerify(instructor._username)
                    }}
                    >
                      Verify
                    </button>
                  </div>
                )}
              </div>
            );
          })}
      </div>
    </div>
  );
};

export default AdminVerifyInstructor;
