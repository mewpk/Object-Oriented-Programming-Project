import Router from "next/router";
import { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

const PaymentPage = () => {
  const [selectedPaymentMethod, setSelectedPaymentMethod] = useState("");

  const [data, setData] = useState([{ _Order__course: [], _Order__id: 0 ,_Order__net_price : 0}]);
  const [paymentMethod, setPaymentMethod] = useState([]);
  const [cookies, setCookie, removeCookie] = useCookies(["user", "role"]);
  const [name, setName] = useState("");
  const [amount, setAmount] = useState(0);
  const [type, setType] = useState(["ATM"]);
  const [listType, setListType] = useState([]);

  const getDataPaymentMethodType = async () => {
    try {
      const res = await fetch("http://localhost:8000/payment_method", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
      });
      let dataRes = await res.json();
      setListType(dataRes);
      console.log(dataRes);
    } catch (error) {
      console.log(error);
    }
  };

  const getDataOrder = async () => {
    try {
      const res = await fetch("http://localhost:8000/all_pending_order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: cookies.user,
        }),
      });
      let dataRes = await res.json();
      setData(dataRes);
      console.log(dataRes);
    } catch (error) {
      console.log(error);
    }
  };
  const getDataPaymentMethod = async () => {
    try {
      const res = await fetch("http://localhost:8000/payment", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: cookies.user,
        }),
      });
      let dataRes = await res.json();
      setPaymentMethod(dataRes);
      console.log(dataRes);
    } catch (error) {
      console.log(error);
    }
  };
  const sendDataPaymentMethod = async () => {
    try {
      const res = await fetch("http://localhost:8000/add_payment_method/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: cookies.user,
          type: type[0],
          amount: Number(amount),
          name: name,
        }),
      });
      let dataRes = await res.json();
      setPaymentMethod(dataRes);
      console.log(dataRes);
    } catch (error) {
      console.log(error);
    }
  };

  const sendDataMakePayment = async (order_id) => {
    try {
      const res = await fetch("http://localhost:8000/make_payment/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: cookies.user,
          type: paymentMethod[0]._Payment__type,
          name: paymentMethod[0]._Payment__name,
          order_id: order_id,
        }),
      });
      let dataRes = await res.json();
      console.log(dataRes);
    } catch (error) {
      console.log(error);
    }
  };

  const createPaymentMethod = (e) => {
    e.preventDefault();
    sendDataPaymentMethod();
    Router.reload();
  };
  useEffect(() => {
    if (!cookies.user || cookies.role !== "Student") {
      Router.push("/");
    }
    getDataOrder();
    getDataPaymentMethodType();
    getDataPaymentMethod();
  }, []);

  const handlePaymentMethodChange = (e) => {
    setSelectedPaymentMethod(e.target.value);
  };

  const handleSubmit = (e, order_id) => {
    e.preventDefault();
    // Submit the payment form
    console.log(
      JSON.stringify({
        username: cookies.user,
        type: paymentMethod[0]._Payment__type,
        name: paymentMethod[0]._Payment__name,
        order_id: order_id,
      })
    );
Router.push("/mycourse")
    sendDataMakePayment(order_id);
  };

  return (
    <>
      <div className="flex justify-center items-center min-h-screen bg-gray-100">
        <div className="max-w-200 mx-auto">
          <h1 className="text-3xl font-bold mt-6 mb-6">Payment</h1>
          {data &&
            data.map((orders) => (
              <div className="container mx-auto p-10" key={orders._Order__id}>
                <div className="mb-4">
                  <h2 className="text-lg font-bold mb-2">Order Summary</h2>
                  <table className="w-full border-collapse">
                    <thead>
                      <tr className="border-b">
                        <th className="text-left py-2 px-4">Img</th>
                        <th className="text-left py-2 px-4">Name</th>
                        <th className="text-left py-2 px-4">Price</th>
                      </tr>
                    </thead>
                    <tbody>
                      {orders._Order__course &&
                        orders._Order__course.map((order) => (
                          <tr key={order._id} className="border-b">
                            <td className="py-2 px-4">
                              <img
                                className="h-20 w-20 rounded-full object-cover "
                                src={order._image}
                                alt={order._title}
                              />
                            </td>

                            <td className="py-2 px-4">{order._name}</td>
                            <td className="py-2 px-4">${order._price}</td>
                          </tr>
                          
                        ))}
                    </tbody>
                  </table>
                </div>
                <h2 className="text-lg mb-2 text-right">Total : {orders._Order__net_price}</h2>
                <div className="mb-4">
                  <h2 className="text-lg font-bold mb-2">Payment Method</h2>
                  {paymentMethod && paymentMethod.length == 0 ? (
                    <div className="bg-white py-10 px-6 shadow sm:rounded-lg sm:px-10">
                      <form onSubmit={createPaymentMethod}>
                        <div className="mb-6">
                          <label
                            htmlFor="name"
                            className="block font-bold mb-1"
                          >
                            Name
                          </label>
                          <input
                            type="text"
                            id="name"
                            name="name"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            className="block w-full border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                            required
                          />
                        </div>
                        <div className="mb-6">
                          <label
                            htmlFor="Type"
                            className="block font-bold mb-1"
                          >
                            Type
                          </label>
                          <select
                            id="type"
                            name="type"
                            value={type}
                            onChange={(e) =>
                              setType(
                                Array.from(
                                  e.target.selectedOptions,
                                  (option) => option.value
                                )
                              )
                            }
                            className="block w-full border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                            required
                            defaultValue={"ATM"}
                          >
                            {listType &&
                              listType.map((type) => (
                                <option value={type}>{type}</option>
                              ))}
                          </select>
                        </div>
                        <div className="mb-6">
                          <label
                            htmlFor="amount"
                            className="block font-bold mb-1"
                          >
                            amount
                          </label>
                          <input
                            type="text"
                            id="amount"
                            name="amount"
                            value={amount}
                            onChange={(e) => setAmount(Number(e.target.value))}
                            className="block w-full border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                            required
                          />
                        </div>
                        <button
                          type="submit"
                          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                        >
                          Submit Create Payment Method
                        </button>
                      </form>
                    </div>
                  ) : (
                    <form onSubmit={(e) => handleSubmit(e, orders._Order__id)}>
                      {paymentMethod &&
                        paymentMethod.length >= 1 &&
                        paymentMethod.map((paymentMethod) => (
                          <div className="flex items-center mb-2 ">
                            <input
                              type="radio"
                              id={paymentMethod._Payment__type}
                              name={paymentMethod._Payment__name}
                              value={paymentMethod._Payment__name}
                              checked={
                                selectedPaymentMethod ===
                                paymentMethod._Payment__name
                              }
                              onChange={handlePaymentMethodChange}
                              className="mr-2"
                            />
                            <h3 className="text-lg leading-6 font-medium text-gray-900">
                              {paymentMethod._Payment__name}
                            </h3>

                            <h3 className="text-lg leading-6 font-medium text-gray-900 ml-10">
                              Amount : {paymentMethod._Payment__amount} $
                            </h3>
                            <h3 className="text-lg leading-6 font-medium text-gray-900 ml-10">
                              Type : {paymentMethod._Payment__type}
                            </h3>
                          </div>
                        ))}
                      <button
                        type="submit"
                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                        disabled={!selectedPaymentMethod}
                      >
                        Submit Payment
                      </button>
                    </form>
                  )}
                </div>
              </div>
            ))}
        </div>
      </div>
    </>
  );
};

export default PaymentPage;
