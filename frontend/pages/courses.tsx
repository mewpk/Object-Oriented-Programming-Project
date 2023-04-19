
import CourseList from "../components/CourseList";
import { useEffect, useState } from "react";

export default function Course() {
  const [data, setData] = useState("");
  const getData = async () => {
    const res = await fetch("http://localhost:8000/course", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });
    let dataRes = await res.json();
    setData(dataRes);
    console.log(dataRes);
  };
  useEffect(() => {
    getData();
  }, []);
  return (
    <div  className="container mx-auto p-10">
    <CourseList courses={data} />
    </div>
  )
}
