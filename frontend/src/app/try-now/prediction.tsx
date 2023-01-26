"use client";

import Image from "next/image";
import React, { useState, useRef, useEffect } from "react";

export default function Prediction() {
  const formRef = useRef(null);
  const [path, setPath] = useState(null);
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);


  useEffect(() => {
    if (file) {
      setPath(URL.createObjectURL(file));
    }
  }, [file])

  const handleImageChange = (e) => {
    setFile(e.target.files[0])
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true)
    const formData = new FormData();

    formData.append(
      "file",
      file,
      file.name
    );

    try {
      const response = await fetch(process.env.NEXT_PUBLIC_API_URL + "/api/v1/predict", {
        method: "POST",
        body: formData,
      });
      const json = await response.json();
      console.log(json);
      setLoading(false);
      setResults(json)
    } catch (error) {
      console.error(error);
    }
  };
  const handleClear = () => {
    setResults(null)
    setPath(null)
    formRef.current.reset();
  }

  return (
    <div className="">
      <form
        onSubmit={handleSubmit}
        ref={formRef}
        className="space-y-4 flex flex-col max-w-sm justify-center items-center"
      >
        {path ? (
          <div className="flex flex-col space-y-2">
            <h3 className="text-center text-sky-600">Image Preview</h3>
            <div className="flex w-64 h-48 relative">
              <Image
                className=" object-cover  rounded "
                src={path}
                alt="Preview"
                fill
              />
            </div>
          </div>
        ) : (
          <label
            id="label"
            className="w-64 h-48 justify-center flex flex-col items-center px-4 py-6 bg-white rounded-md shadow-md tracking-wide border border-sky cursor-pointer hover:bg-sky-500 hover:text-white text-sky-500 ease-linear transition-all duration-150"
          >
            <svg
              className="w-10 h-10"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M5.5 13a3.5 3.5 0 01-.369-6.98 4 4 0 117.753-1.977A4.5 4.5 0 1113.5 13H11V9.413l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 001.414 1.414L9 9.414V13H5.5z"></path>
              <path d="M9 13h2v5a1 1 0 11-2 0v-5z"></path>
            </svg>
            <span className="mt-2 text-sm">Select a CXR image file</span>

            <input
              type="file"
              className="hidden"
              name="file"
              required
              onChange={handleImageChange}
              accept="image/png, image/jpeg"
            />
          </label>
        )}

        {
          results ?
            <div className="flex flex-col space-y-4">
              <div className="flex flex-col text-center space-y-1">
                <h4 className="font-bold text-sky-700 py-1">Prediction Results</h4>
                <p><span className="capitalize" >Class name:</span><span className=" text-sky-600"> {results?.predictions?.class_name}</span></p>
                <p><span className="capitalize" >Confidence: </span><span className=" text-sky-600">{results?.predictions?.confidence} %</span></p>
                <p><span className="capitalize" >Inference time:</span><span className=" text-sky-600"> {results?.inference_time}</span></p>
              </div>
              <button
                onClick={handleClear}
                className="bg-sky-600 rounded-full px-10 py-2 text-white hover:bg-sky-700 hover:shadow-sm transition-all cursor-pointer"
              > Clear </button>
            </div>
            :
            <button
              type="submit"
              className="bg-sky-600 rounded-full px-10 py-2 text-white hover:bg-sky-700 hover:shadow-sm transition-all cursor-pointer"
            >          <div className="flex shrink-0 items-center space-x-2">
                {loading ? (
                  <svg
                    className="h-4 w-4 animate-spin text-white"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <circle
                      className="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      strokeWidth="4"
                    ></circle>
                    <path
                      className="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                    ></path>
                  </svg>
                ) : (
                  ""
                )}
                <span>Submit</span>
              </div>

            </button>

        }

      </form>
    </div>
  );
}
