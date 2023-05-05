import React, { useEffect, useState } from "react";
import CourseList from "../components/CourseList";
import { useCookies } from "react-cookie";
import  Router  from "next/router";

export default function mycourse() {
  const [data, setData] = useState([]);
  const [cookies, setCookie, removeCookie] = useCookies(["user" , "role"]);
  const getData = async () => {
    try {
      const res = await fetch("http://localhost:8000/studentcourse/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: cookies.user
        }),
      });
      let dataRes = await res.json();
      console.log(dataRes);
      setData(dataRes._StudentCourseCollection__courses)
    } catch (error) {
      console.log(error);
    }
  };
  useEffect(() => {
    getData();
  }, []);
  useEffect(()=>{
    if (!cookies.user || cookies.role !== "Student"){
      Router.push("/")
    }
  })
  
  return (
    <div className="container mx-auto p-10">
      <CourseList courses={data} />
    </div>
  );
}
