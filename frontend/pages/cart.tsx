import Router  from "next/router";
import { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

export default function Cart() {
  const [couponCode, setCouponCode] = useState("");
  const [cartCourse, setCartCourse] = useState([]);
  const [cookies, setCookie, removeCookie] = useCookies(["user" , "role"]);
  const [username, setUsername] = useState(null);
  const [data , setData ] = useState({
    _Cart__course : [],
    _Cart__net_price : 0,
    _Cart__net_coupon : 0,
    _Cart__net_promotion : 0,
    _Cart__price : 0
  });
  useEffect(()=>{
    if (!cookies.user || cookies.role !== "Student"){
      Router.push("/")
    }
  })
  const handleApplyCoupon = () => {
    // Call an API or do something else to check if the coupon is valid
    sendDataCoupon();
    getData();
  

  };
  const sendDataPayment = async () => {
    const res = await fetch("http://localhost:8000/add_order", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user
      }),
    });
    let dataRes = await res.json();
    try {
      setCartCourse(dataRes._Cart__course);
      setData(dataRes)
      console.log(dataRes);
    } catch (error) {
      console.log(error)
    }
  };
  const handleProceedToPayment = () => {
    sendDataPayment()
    Router.push("/payment")
  };

  

  const getData = async () => {
    const res = await fetch("http://localhost:8000/cart", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user,
        
      }),
    });
    let dataRes = await res.json();
    try {
      setCartCourse(dataRes._Cart__course);
      setData(dataRes)
      console.log(dataRes);
    } catch (error) {
      console.log(error)
    }
    
  };

  const sendDataCoupon = async () => {
    const res = await fetch("http://localhost:8000/cart/apply_coupon", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: cookies.user,
        passcode : couponCode
        
      }),
    });
    let dataRes = await res.json();
    try {
      setCartCourse(dataRes._Cart__course);
      setData(dataRes)
      console.log(dataRes);
    } catch (error) {
      console.log(error)
    }
  };
  useEffect(() => {
    getData();
  }, []);

  useEffect(() => {
    setUsername(cookies.user);
  }, [cookies]);

const removeCorseInCart =async (course_id: string) => {
  const res = await fetch("http://localhost:8000/remove_course_from_cart", {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: cookies.user,
      course_id: course_id,
    }),
  });
  let dataRes = await res.json();
  console.log(dataRes);
  getData();
}



  return (
    <main className="container mx-auto p-10">
      <div className="flex flex-col justify-center items-center">
        <h1 className="text-3xl font-bold mb-4">Your Cart</h1>
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th
                scope="col"
                className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Course
              </th>
              <th
                scope="col"
                className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Description
              </th>
              <th
                scope="col"
                className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Instructor
              </th>
              
              <th
                scope="col"
                className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Price
              </th>
              <th
                scope="col"
                className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Remove
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {cartCourse && cartCourse.map((course) => (
              <tr key={course._id}>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="flex items-center">
                    <div className="flex-shrink-0 h-20 w-20">
                      <img
                        className="h-20 w-20 rounded-full object-cover"
                        src={course._image}
                        alt={course._title}
                      />
                    </div>
                    <div className="ml-4">
                      <div className="text-sm font-medium text-gray-900">
                        {course._title}
                      </div>
                    </div>
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm text-gray-900">{course._description}</div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
              <div className="text-sm text-gray-900">{course._instructor}</div>
            </td>
            <td className="px-6 py-4 whitespace-nowrap text-right">
              <div className="text-sm text-gray-900">${course._price}</div>
            </td>
            <td  className="px-6 py-4 whitespace-nowrap text-right">
            <button
              onClick={() => {
                removeCorseInCart(course._id);
              }}
              type="button"
              className={`hover:animate-pulse w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-red-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:ml-3 sm:w-auto sm:text-sm `}
            >
              Remove From Cart
            </button>
            </td>
          </tr>
        ))}
        <tr className="bg-gray-50">
          <td colSpan={3} className="px-6 py-4 text-right text-sm font-medium text-gray-900 uppercase">
            Total Price
          </td>
          <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium text-gray-900">
            ${data._Cart__net_price}
          </td>
        </tr>
      </tbody>
    </table>
    <div className="flex flex-col mt-4">
      <label htmlFor="coupon" className="text-sm font-medium text-gray-900 mb-2">
        Coupon Code
      </label>
      <div className="flex items-center">
        <input
          type="text"
          id="coupon"
          name="coupon"
          className="border-gray-300 border rounded-md py-2 px-3 mr-2 w-1/2"
          value={couponCode}
          onChange={(e) => setCouponCode(e.target.value)}
        />
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          onClick={handleApplyCoupon}
        >
          Apply
        </button>
      </div>
    </div>
    <button
      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
      onClick={handleProceedToPayment}
    >
      Proceed to Payment
    </button>
   
  </div>
</main>
);
}
