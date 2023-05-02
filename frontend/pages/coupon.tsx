import React, { useEffect, useState } from "react";
import CouponCard from "../components/CouponCard";



export default function coupon() {
    const [data, setData] = useState([]);
    const getData = async () => {
      const res = await fetch("http://localhost:8000/coupon", {
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
    <div className="bg-gray-100 min-h-screen py-8">
      <div className="container mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {data.map((coupon) => (
          < CouponCard
            key={coupon._passcode}
            title={coupon._condition}
            description={coupon._type}
            code={coupon._passcode}
            start_date = {coupon._start_date}
            end_date= {coupon._end_date}
            percent ={coupon._discounted_percent}
          />
        ))}
      </div>
    </div>
  );
}
