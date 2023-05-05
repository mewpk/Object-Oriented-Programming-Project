import React from "react";

interface CouponCardProps {
  title: string;
  description: string;
  code: string;
  start_date: string;
  end_date: string;
  percent: number;
}

const CouponCard: React.FC<CouponCardProps> = ({
  title,
  description,
  code,
  start_date,
  end_date,
  percent
}) => {
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl  hover:scale-105 duration-500 ">
      <div className="px-4 py-5 sm:p-6">
        <div className="flex items-center">
          <div className="flex-shrink-0 bg-indigo-500 rounded-md p-3">
            <svg
              className="h-6 w-6 text-white"
              fill="none"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path d="M9 19h6a2 2 0 002-2V7a2 2 0 00-2-2H9a2 2 0 00-2 2v10a2 2 0 002 2z" />
              <path d="M15 13l-3-3m0 0l-3 3m3-3v8" />
            </svg>
          </div>
          <div className="ml-5">
            <h3 className="text-lg leading-6 font-medium text-gray-900">
              {title}
            </h3>
            <p className="mt-2 text-base leading-6 text-gray-500">
            percent : {percent}%
            </p>
            <p>
            <span className="font-medium bg-slate-200">code : {code}</span>
            </p>
            <p className="text-base leading-6 text-gray-500">
            type : {description}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CouponCard;
