import { useEffect, useState } from 'react';
import Image from "next/image";
import { useCookies } from 'react-cookie';
import Router from "next/router";


const AccountCard = ({ account }) => {
  const [showDetails, setShowDetails] = useState(false);

  const handleToggleDetails = () => {
    setShowDetails(!showDetails);
  };

  return (
    <main className="container mx-auto p-10">
    <div className="bg-white shadow-md rounded-lg p-4 mb-4 hover:shadow-xl  hover:scale-105 duration-500">
      <div className="flex items-center justify-between mb-2">
      <div className="relative h-20 w-20">
          <div className="avatar ">
            <Image
              src="https://img.freepik.com/free-icon/user_318-159711.jpg"
              alt={`${account._name}'s profile picture`}
              layout="fill"
              objectFit="contain"
            />
          </div>
        </div>
        <h2 className="text-lg font-semibold">{account._username}</h2>
        <button
          className="text-gray-500 hover:text-gray-700"
          onClick={handleToggleDetails}
        >
          {showDetails ? 'Hide details' : 'Show details'}
        </button>
      </div>
      {showDetails && (
        <div className='p-10'>
          <p className="text-gray-600 mb-2">Username : {account._username}</p>
          <p className="text-gray-600 mb-2">Name : {account._name}</p>
          <p className="text-gray-600 mb-2">Email : {account._email}</p>
          <p className="text-gray-600 mb-2">Language : {account._language}</p>
          <p className="text-gray-600 mb-2">About : {account._about}</p>
          <p className="text-gray-600 mb-2">Role : {account._role}</p>
          <p className="text-gray-600">Active : {account._active ? "Active" : "Inactive"}</p>
        </div>
      )}
    </div>
    </main>
  );
};

const AllAccounts = () => {
    const [data, setData] = useState([]);
    const [cookies, setCookie, removeCookie] = useCookies(["user" , "role"]);
    const getData = async () => {
      const res = await fetch("http://localhost:8000/users", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
      });
      let dataRes = await res.json();
      setData(dataRes);
      console.log(dataRes);
    };
    useEffect(() => {
      getData();
      if (!cookies.user || cookies.role !== "Admin") {
        Router.push("/");
      }
    }, []);
    
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
      {data.map((account) => (
        <AccountCard key={account._username} account={account} />
      ))}
    </div>
  );
};

export default AllAccounts;
