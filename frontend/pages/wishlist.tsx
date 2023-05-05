import { useCookies } from "react-cookie";
import CourseList from "../components/CourseList";
import { useEffect, useState } from "react";
import Router from "next/router";

export default function WishList() {
  const [data, setData] = useState("");
  const [cookies, setCookie, removeCookie] = useCookies(["user","role"]);
  const getData = async () => {
    try {
      const res = await fetch("http://localhost:8000/favorite", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: cookies.user,
        }),
      });
      let dataRes = await res.json();
      setData(dataRes._Favorite__favorite);
      console.log(dataRes);
    } catch (error) {
      console.log(error);
    }
  };
  useEffect(() => {
    getData();
    if (!cookies.user || cookies.role !== "Student") {
      Router.push("/");
    }
  }, []);

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="max-w-200 mx-auto">
        <h1 className="text-3xl font-bold mt-6 mb-6">WishList</h1>
        <CourseList courses={data} />
      </div>
    </div>
  );
}
